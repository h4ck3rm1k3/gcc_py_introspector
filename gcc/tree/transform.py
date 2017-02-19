import pickle
import gcc.tree.attributes
import gcc.tree.nodes
import gcc.tree.tuast
import sys
from gcc.tree.debug import debug, debug3, debug2
import pprint

class Resolver:

    @staticmethod
    def get_node_objs( x):
        d = gcc.tree.nodes.Nodes.get_node_objs(x)
        return d
    
    @staticmethod    
    def resolve2(x,seen, role, nt):
        debug({
            'phase':'resolve2',
            'x':x,
            'role':role,
            'nt':nt,
            'seen':seen,
        })
        if isinstance(x, str):
            #print ('instance %s' % x)
            return x

        if isinstance(x, dict):
            if 'type' in x:
                #print  ('resolving dict %s' % pprint.pformat(x))
                return Resolver.resolve2( x['type'],seen, role, nt)
            else:
                #print('resolving dict %s' % pprint.pformat(x))
                raise Exception()
        skip = ('min','max','size', 'bpos')
        if role in skip:
            if len(seen['stack']) > 3:
                return 'short'

        if isinstance(x,tuast.Node):
            return Resolver.resolve(Resolver.get_node_objs(x.nid()),seen,role)
        if isinstance(x,nodes.Node):
            return Resolver.resolve(Resolver.get_node_objs(x.nid()),seen,role)
        if isinstance(x,attributes.TNode):
            return Resolver.resolve(Resolver.get_node_objs(x.nid()),seen,role)

        t = type(x)
        print('trying to resolve %s' % t)
        print('resolving obj %s' % pprint.pformat(x))
        raise Exception(x)

    @staticmethod
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
        #v = Resolver.resolve2(val,seen, name, nt)
        v = Resolver.resolve(Resolver.get_node_objs(val),seen,name)
        return { 'name': name , 'val' : v}

    @staticmethod
    def process( x,nt, seen):
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
                v = Resolver.resolve2(val,seen, name, nt)
                return { 'name': name , 'val' : v}

        if 'type' in x:
            t = x['type']
            if isinstance(t, str):
                v = x['val']
                x = Resolver.resolve2(v,seen, 'type', nt)
                return { 'name': 'type', 'val' : x}
            else:
                #print  'resolving  %s' %
                x = Resolver.resolve2(t,seen,'type', nt)
                return { 'name': 'type', 'val' : x}
        if 'string' in x:
            #return x['string']
            return { 'name': 'string', 'val' : x['string']}
        if 'addr' in x:
            return { 'name': 'addr', 'val' : x['addr']}
        if 'note' in x:
            return { 'name': 'note', 'val' : x['note']}

        raise Exception(  ' process %s' % pprint.pformat(x))

    @staticmethod
    def resolve_name( x):

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

    @staticmethod
    def resolve( d,seen, role):
        debug({
            'phase':'resolve',
            'd':d,
            'role':role,
            'seen':seen,
        })
        #nt = seen['node_type']

        if 'node' not in d:
            return None
        
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
                v = Resolver.process( x, nt, seen)
                if v:
                    t [v['name']]=v['val']

        if 'stack' in d:
            for x in d['stack']:
                name = x[0]
                val = x[1]
                v = Resolver.process_stack( name, val, nt, seen)
                if v:
                    t [v['name']]=v['val']

        if role == 'name':
            #print ("role is name")
            if 'name' in t:
                print ("name role : %s" % t['name'])
                t=Resolver.resolve_name(t['name'])

        seen['seen'][nid]=t
        #print ( "done seen %s -> %s" % (nid, seen['seen'][nid]))
        return t

    @staticmethod
    def transform( x):
        #print x
        d = Resolver.get_node_objs(x)

        if d is None:
            return None
        
        # decl is set when the statement is finished
        if 'decl' not in d:
            ni = x
            #debug(gcc.tree.nodes.Nodes.nodes)
            #if 'node' in d:
            #    nt = 
            #debug(x)
            #raise Exception("not declared %s %s" % (x, d))
            #return None
        else:
            ni = d['nid']
        
            if isinstance(ni, str):
                #ni=
                pass
            else: 
                ni = d['decl'].node_id.nid()


            nt = d['decl']['type']

            #print (ni,nt)

            if 'node' in d:
                #del d['node'].refs
                d['node']._node_type = nt


            #if nt.endswith('_decl'):
            if True:

                d2 = Resolver.resolve(d,{'stack': [], 'seen': {}, 'node_type':nt, 'node_id': x },'start')
                #if 'name' in d2:
                    #print('name:',x, nt,d2['name'])


                debug3({
                    'phase':'resolved',
                    #'ni': ni,
                    #'nt': nt,
                    #'node': d['node'].__dict__,
                    'd': d,
                    'd2': d2
                })

