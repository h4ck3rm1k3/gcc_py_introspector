import pdb
import ply.lex as lex
import pickle

from  gcc.tree.pprint2 import pformat, pformat2
import gcc.tree.tuast
import gcc
from gcc.tree.debug import debug    
import gcc.tree.transform
from gcc.tree.node import Node
import pprint

#Resolver
def testsize(x):
    return
    if x :
        l = len(x.keys())
        s = pprint.pformat(x)
        print ("debug:%s %s -> %0.1ad" % (
            l, len(s),
            len(s)/l
        ))
        #print ("debug:%s" % (s))
    
class Nodes:
#debug("Loading Nodes")
    nodes = {}
    #stack = []
    #astack = []
    aobj = {}
    aobj2 = {}
    
    #@staticmethod
    #def setup():
    #    from  gcc.tree.transform import Resolver
    #    r = Resolver()

    @staticmethod
    def usedby(nid, x, n):
        
        d = gcc.tree.nodes.Nodes.nodes[nid]
        # if 'refs' in d:
        #     d['refs'].append([x,n])
        # else:
        #     d['refs']=[[x,n]]
            
        #self.refs.append([x.nid(),n])

    @staticmethod
    def get_node_objs(x):
        if x in gcc.tree.nodes.Nodes.nodes:
            return gcc.tree.nodes.Nodes.nodes[x]
        else:
            debug({'cannot find':x, 'nodes': gcc.tree.nodes.Nodes.nodes })
            raise Exception(x)


def reference(n, name):
    debug(Nodes.nodes)
    #global stack
    #global Nodes.astack
    #global nodes
    debug("ref %s %s" % (n, name))
    #raise Exception('what')
    #pdb.set_trace()
    if isinstance(n,lex.LexToken):
        n = n.value
    if isinstance(name,lex.LexToken):
        name = name.value
    gcc.tree.nodes.Nodes.aobj2[name]=n
    #Nodes.astack.append([name,n])
    if n not in gcc.tree.nodes.Nodes.nodes:
        gcc.tree.nodes.Nodes.nodes[n]= {
            #'count':1,
                         #'node' : Node(n),
                         'nid': n }
    #else:
        #if 'count' in  gcc.tree.nodes.Nodes.nodes[n]:
        #    gcc.tree.nodes.Nodes.nodes[n]['count'] = gcc.tree.nodes.Nodes.nodes[n]['count'] +1
            #Nodes.nodes[n]['refs'].append(nd)
        #else:
        #    gcc.tree.nodes.Nodes.nodes[n]['count'] = 1
            
        #if 'node' not in gcc.tree.nodes.Nodes.nodes[n]:
        #    gcc.tree.nodes.Nodes.nodes[n]['node']= Node(n)
            
    debug(Nodes.nodes)
    return gcc.tree.nodes.Nodes.nodes[n]

def declare(n):
    #pickle.dumps(n)
    #global Nodes.nodes
    #debug(Nodes.nodes)
    if not isinstance(n, str):
        n = n.value
    debug("decl %s" % pformat(n))
    
    if n not in gcc.tree.nodes.Nodes.nodes:
        gcc.tree.nodes.Nodes.nodes[n]= {
            #'decl_count':1,
                         #'node': Node(n),
                   'nid': n
        }
        
    else:
        # if 'decl_count' in gcc.tree.nodes.Nodes.nodes[n] :
        #     debug(Nodes.nodes[n]['decl_count'])
        #     #raise Exception("Duplicate Decl %s" %n)
        #     gcc.tree.nodes.Nodes.nodes[n]['decl_count'] = n
        # else:
        #     gcc.tree.nodes.Nodes.nodes[n]['decl_count'] = 1
        pass
    n2 = gcc.tree.transform.Resolver.transform(n)
    #testsize(n2)
    #testsize(gcc.tree.nodes.Nodes.nodes)
    
    return n

def statement(x):
    #debug(Nodes.nodes)
    debug("statement %s" % pformat2(x))
    #pickle.dumps(x)
    #pickle.dumps(x)
    #global stack
    #global Nodes.astack
    #global Nodes.nodes
    if x:
        #pprint.pprint(x)
        nid = x['node_decl']
        
        #if nid in gcc.tree.nodes.Nodes.nodes:
        #    gcc.tree.nodes.Nodes.nodes[nid]['decl'] = x
        #else:
        gcc.tree.nodes.Nodes.nodes[nid]['type'] =  x['type']

        #gcc.tree.nodes.Nodes.nodes[nid]['stack'] =list(Nodes.stack)

        gcc.tree.nodes.Nodes.nodes[nid]['attrs'] =Nodes.aobj
        gcc.tree.nodes.Nodes.nodes[nid]['refs'] =Nodes.aobj2
        Nodes.aobj={}
        Nodes.aobj2={}

        #pprint.pprint(gcc.tree.nodes.Nodes.nodes[nid])
        #pprint.pprint(Nodes.aobj)

        # now each of these items
        #for sp in gcc.tree.nodes.Nodes.stack:
        #    sn = sp[0]
        #    s = sp[1]
        #    gcc.tree.nodes.Nodes.usedby(s,x,sn)
        #gcc.tree.nodes.Nodes.stack=[]
        gcc.tree.nodes.Nodes.aobj={}
        gcc.tree.nodes.Nodes.aobj2={}
        debug(gcc.tree.nodes.Nodes.nodes)
        n2 = gcc.tree.transform.Resolver.transform(nid)
        #testsize(n2)
        if n2 is None:
            debug ("expr be null %s" % nid)
    else:
        raise Exception("none")
    debug(gcc.tree.nodes.Nodes.nodes)

    n2 = gcc.tree.transform.Resolver.transform(nid)
    #testsize(n2)
    testsize(gcc.tree.nodes.Nodes.nodes)
    
def attrs(v):
    if type (v) == str:
        raise Exception(v)
        #v = {'unkown': v}
    if 'type' in v:
        if 'attrs' in v['type']:
            raise Exception('to complex')
    #pprint.pprint({'push':v})
    #pickle.dump(v,f)
    for x in v.keys():
        v2 = v[x]
        gcc.tree.nodes.Nodes.aobj[x]=v2

def report():
    print("Nodes.Nodes Report:")
    #b = pickledb.load('Nodes.nodes.db', False)
    f = open ("Nodes.nodes.pickle","wb")
    
    #gcc.tree.nodes.Nodes.nodes2= {}
    #testsize(gcc.tree.nodes.Nodes.nodes)
    
    # for n in gcc.tree.nodes.Nodes.nodes.keys():
    #     n2 = gcc.tree.transform.Resolver.transform(n)
    #     #testsize(n2)
    #     gcc.tree.nodes.Nodes.nodes2[n]=n2
    #     debug({'transform':n2})
        
    pickle.dump(Nodes.nodes,f)        
        
    #     dc = None
    #     if 'decl' in d:
    #         dc=d['decl']

    #     # now we resolve the references
    #     b.set(n,d)

    #     # pprintpprint({
    #     #     #'tst':1,
    #     #     'n' : n,
    #     #     'data'  : d,
    #     #     'dcl': dc
    #     # })
    # b.dump()
