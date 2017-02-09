import pickle
#class SomeType:
#    def __call__(self):
#        pass
import attributes
import nodes
import tuast
from tinydb import TinyDB, where

f = open ("nodes.pickle","r")
node_objs = pickle.load(f)
nodes.nodes = node_objs
import pprint
import shelve
sd = shelve.open('example.shelve')

def resolve2(x,seen, role, nt):

    if isinstance(x, str):
        return x

    if isinstance(x, dict):
        if 'type' in x:
            #print  'resolving dict %s' % pprint.pformat(x)
            return resolve2( x['type'],seen, role, nt)
        else:
            print('resolving dict %s' % pprint.pformat(x))
            raise Exception()
    skip = ('min','max','size', 'bpos')
    if role in skip:
        if len(seen['stack']) > 3:
            return 'short'


    if isinstance(x,tuast.Node):
        return resolve(node_objs[x.nid()],seen,role)
    if isinstance(x,nodes.Node):
        return resolve(node_objs[x.nid()],seen,role)
    if isinstance(x,attributes.TNode):
        return resolve(node_objs[x.nid()],seen,role)

    t = type(x)
    print('trying to resolve %s' % t)
    print('resolving obj %s' % pprint.pformat(x))
    raise Exception(x)


def process(x,nt, seen):
    #nt = seen['node_type']
    if 'name' in x:
        val  = x['val']
        name = x['name']
        if name == 'chain' and nt.endswith('_decl'): # dont chain decls
            return { 'name': 'chain', 'val': val }
        else:
            v = resolve2(val,seen, name, nt)
            return { 'name': name , 'val' : v}

    if 'type' in x:
        t = x['type']
        if isinstance(t, str):
            v = x['val']
            x = resolve2(v,seen, 'type', nt)
            return { 'name': 'type', 'val' : x}
        else:
            #print  'resolving  %s' %
            x = resolve2(t,seen,'type', nt)
            return { 'name': 'type', 'val' : x}
    if 'string' in x:
        #return x['string']
        return { 'name': 'string', 'val' : x['string']}
    if 'addr' in x:
        return { 'name': 'addr', 'val' : x['addr']}
    if 'note' in x:
        return { 'name': 'note', 'val' : x['note']}

    raise Exception(  ' process %s' % pprint.pformat(x))

def resolve_name(x):

    #if isinstance(x, basestring):
    #    print "\n\nRESOLVESTR '%s'\n\n" % x
    #    return x

    if isinstance(x, dict):
        if 'string' in x:
            #print "\n\nRESOLVE: %s\n" % x['string']
            return x['string']

    raise Exception(x)


def resolve(d,seen, role):
    #nt = seen['node_type']

    nid = d['node'].nid()

    pprint.pprint(d['node'].__dict__)
    nt = d['node'].node_type()

    if nid not in seen['seen'] :
        #print 'new %s\n' % nid
        seen['seen'][nid]=1
        seen['stack'].append([nid,role,nt])
        #return
    else:
        #print 'seen %s\n' % nid
        return seen['seen'][nid]

    if len(seen['stack']) > 100:
        pprint.pprint(seen)
        return 'overflow'
    t = {
        '__nid__' : nid,
    }
    if 'astack' in d:
        for x in d['astack']:
            v = process( x, nt, seen)
            if v:
                #if isinstance(v, basestring):
                #    return v
                t [v['name']]=v['val']

    if role == 'name':
        if 'name' in t:
            t=resolve_name(t['name'])

    seen['seen'][nid]=t
    #print "done seen %s -> %s" % (nid, seen['seen'][nid])
    return t


class TreeEncoder :
    def default(self, o):
        return {}
    
db = TinyDB('empty.json',cls=TreeEncoder)

#pprint.pprint(node_objs)
for x in sorted(list(node_objs.keys()), key=int):
    #print x
    d = node_objs[x]
    #print d['decl'].node_id.nid
    if 'decl' in d:
        nt = d['decl'].node_type

        if nt.endswith('_decl'):
            d2 = resolve(d,{'stack': [], 'seen': {}, 'node_type':nt, 'node_id': x },'start')
            if 'name' in d2:
                print(x, nt,d2['name']['string'])
            #db.insert(d2)
            #sd["%s" % d2['name']['string']]=d2
