import pprint2
import ply.lex as lex
import pdb
#import pickledb
import pprint
import tuast
import pickle
nodes = {}
stack = []
astack = []
import gcc
import gcc.tree.transform
r = gcc.tree.transform.Resolver(nodes)
    
import gcc.tree.transform
def debug(x):
    pass

def pprintpprint(x):
    pprint.pprint(x)

class Node :
    def __init__(self, n):
        self.n = n
        self.refs = []
        self._node_type = 'unknown'
        
    def node_type(self):
        if 'decl' in nodes[self.n]:
            return nodes[self.n]['decl'].node_type
        else:
            return 'unknown'
    
    def nid(self):
        return self.n
    
    def value(self):
        return self.n

    def format_refs(self):
        #r = ""
        r = "refs %s" % len(self.refs)
        # for s in self.refs:
        #     r = r + s[1] + ':'+ s[0]
        return r
    #def default(self, x):
    #    return {}
    #def __repr__(self):
        #return "Node : %s Refs: %s" % (self.n,len(self.refs))
    #    return "!Node:id='%s',refs:'%s'!" % (self.n, self.format_refs())
    #def ref(self, obj):
    #    self.refs.append(obj)

    def usedby(self, x, n):
        self.refs.append([x.nid(),n])

def reference(n, name):
    global stack
    global astack
    global nodes
    debug("ref %s %s" % (n, name))
    #raise Exception('what')
    #pdb.set_trace()
    if isinstance(n,lex.LexToken):
        n = n.value
    if isinstance(name,lex.LexToken):
        name = name.value
    stack.append([name,n])
    #astack.append([name,n])
    if n not in nodes:
        nodes[n]= {'count':1, 'node' : Node(n), 'nid': n }
    else:
        if 'count' in  nodes[n]:
            nodes[n]['count'] = nodes[n]['count'] +1
            #nodes[n]['refs'].append(nd)
        else:
            nodes[n]['count'] = 1
            
        if 'node' not in nodes[n]:
            nodes[n]['node']= Node(n)
            
    return nodes[n]['node']

def declare(n):
    #pickle.dumps(n)
    global nodes            
    if not isinstance(n, str):
        n = n.value
    debug("decl %s" % pprint.pformat(n))
    if n not in nodes:
        nodes[n]= {'decl':1,
                   'node': Node(n),
                   'nid': n
        }
    else:
        if 'decl' in nodes[n] :
            pprintpprint(nodes[n]['decl'])
            #raise Exception("Duplicate Decl %s" %n)
            nodes[n]['decl'] = n
        else:
            nodes[n]['decl'] = 1
    n2 = r.transform(n)    
    return nodes[n]['node']

def statement(x):
    debug("statement %s" % pprint2.pformat2(x))
    #pickle.dumps(x)
    #pickle.dumps(x)
    global stack
    global astack
    global nodes
    if x:
        nid = x.nid()
        
        if nid in nodes:
            nodes[nid]['decl'] = x
        else:
            nodes[nid] = { 'decl' : x }

        nodes[nid]['stack'] =list(stack)
        nodes[nid]['astack'] =list(astack)

        # now each of these items
        for sp in stack:
            sn = sp[0]
            s = sp[1]
            nodes[s]['node'].usedby(x,sn)
        stack=[]
        astack=[]
        n2 = r.transform(nid)

def attrs(v):
    if type (v) == str:
        raise Exception(v)
        #v = {'unkown': v}
        #pprintpprint({'push':v})
    #pickle.dump(v,f)
    astack.append(v)

def report():
    print("Nodes Report:")
    #b = pickledb.load('nodes.db', False)
    f = open ("nodes.pickle","wb")
    
    nodes2= {}
    
    for n in nodes.keys():
        n2 = r.transform(n)
        nodes2[n]=n2
        
    pickle.dump(nodes2,f)        
        
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
