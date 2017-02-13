import pickle
#class SomeType:
#    def __call__(self):
#        pass
import attributes
import nodes
import tuast
#from tinydb import TinyDB, where
import sys
f = open (sys.argv[1],"rb")
node_objs = pickle.load(f)
nodes.nodes = node_objs
import pprint
#import shelve
#sd = shelve.open('example.shelve')
def debug(x):
    #pprint.pprint(x)
    pass

def debug2(x):
    #pprint.pprint(x)
    pass

def debug3(x):
    pprint.pprint(x)
    pass

def resolve2(x,seen, role, nt):
    debug({
        'phase':'resolve2',
        'x':x,
        'role':role,
        'nt':nt,
        'seen':seen,
    })
    if isinstance(x, str):
        print ('instance %s' % x)
        return x

    if isinstance(x, dict):
        if 'type' in x:
            #print  ('resolving dict %s' % pprint.pformat(x))
            return resolve2( x['type'],seen, role, nt)
        else:
            #print('resolving dict %s' % pprint.pformat(x))
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

def process_stack( name, val, nt, seen):

    if name == 'chain' and nt.endswith('_decl'): # dont chain decls
        return { 'name': 'chain', 'val': val }

    debug({
        'phase':'process_stack',
        'name':name,
        'val':val,
        'nt':nt,
        'seen':seen,
    })
    #v = resolve2(val,seen, name, nt)
    v = resolve(node_objs[val],seen,name)
    return { 'name': name , 'val' : v}
    
def process(x,nt, seen):
    debug2({
        'phase':'process',
        'x':x,
        'nt':nt,
        'seen':seen,
    })
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

    debug({
        'phase':'resolve_name',
        'x':x,
    })
    #if isinstance(x, basestring):
    #    print "\n\nRESOLVESTR '%s'\n\n" % x
    #    return x

    if isinstance(x, dict):
        if 'string' in x:
            #print "\n\nRESOLVE: %s\n" % x['string']
            return x['string']

    raise Exception(x)


def resolve(d,seen, role):
    debug({
        'phase':'resolve',
        'd':d,
        'role':role,
        'seen':seen,
    })
    #nt = seen['node_type']

    nid = d['node'].nid()

    nt = d['node'].node_type()

    if nid not in seen['seen'] :
        #print ('new %s %s %s\n' % (nid,role,nt))
        seen['seen'][nid]=1
        seen['stack'].append([nid,role,nt])
        #return
    else:
        #print( 'seen %s\n' % nid)
        return seen['seen'][nid]

    if len(seen['stack']) > 100:
        #debug(seen)
        return 'overflow'
    t = {
        '__nid__' : nid,
    }
    if 'astack' in d:
        for x in d['astack']:
            v = process( x, nt, seen)
            if v:
                t [v['name']]=v['val']
                
    if 'stack' in d:
        for x in d['stack']:
            name = x[0]
            val = x[1]
            v = process_stack( name, val, nt, seen)
            if v:
                t [v['name']]=v['val']

    if role == 'name':
        #print ("role is name")
        if 'name' in t:
            print ("name role : %s" % t['name'])
            t=resolve_name(t['name'])

    seen['seen'][nid]=t
    #print ( "done seen %s -> %s" % (nid, seen['seen'][nid]))
    return t


class TreeEncoder :
    def default(self, o):
        return {}
    
#db = TinyDB('empty.json',cls=TreeEncoder)

#debug(node_objs)
for x in ['1',]:#sorted(list(node_objs.keys()), key=int):
    #print x
    d = node_objs[x]

    ni = d['decl'].node_id
    if isinstance(ni, str):
        #ni=
        pass
    else: 
        ni = d['decl'].node_id.nid()
        
    if 'decl' in d:
        nt = d['decl'].node_type
        
        #print (ni,nt)
        del d['node'].refs
        d['node']._node_type = nt
        

        #if nt.endswith('_decl'):
        if True:
            
            d2 = resolve(d,{'stack': [], 'seen': {}, 'node_type':nt, 'node_id': x },'start')
            #if 'name' in d2:
                #print('name:',x, nt,d2['name'])


            debug3({
                'phase':'resolved',
                #'ni': ni,
                #'nt': nt,
                'node': d['node'].__dict__,
                'd': d,
                'd2': d2
            })
                        
            #debug(d2)
            #db.insert(d2)
            #sd["%s" % d2['name']['string']]=d2
