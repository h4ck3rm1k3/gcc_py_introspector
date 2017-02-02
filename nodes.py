import pprint
import ply.lex as lex
import pdb; 
stack = []
astack = []

nodes = {}

class Node :
    def __init__(self, n):
        self.n = n
        self.refs = []
        
    def value(self):
        return self.n

    def format_refs(self):
        #r = ""
        r = "refs %s" % len(self.refs)
        # for s in self.refs:
        #     r = r + s[1] + ':'+ s[0]
            
        return r
    
    def __repr__(self):
        #return "Node : %s Refs: %s" % (self.n,len(self.refs))
        return "!Node:id='%s',refs:'%s'!" % (self.n, self.format_refs())
    
    #def ref(self, obj):
    #    self.refs.append(obj)
        
    def usedby(self, x, n):
        
        # print "USED:%s" % pprint.pformat({
        #     'node': self.n,
        #     'usedby':x,
        #     'usedby2':x.nid(),
        #     'role': n})
        self.refs.append([x.nid(),n])

def reference(n, name):
    global stack
    global astack

    
    #raise Exception('what')
    #pdb.set_trace()

    if isinstance(n,lex.LexToken):
        n = n.value
    if isinstance(name,lex.LexToken):
        name = name.value
        
    stack.append([name,n])
    #astack.append([name,n])

    #print "ref %s" % n
    
    if n not in nodes:
        nodes[n]= {'count':1, 'node' : Node(n) }
    else:
        if 'count' in  nodes[n]:
            nodes[n]['count'] = nodes[n]['count'] +1
            #nodes[n]['refs'].append(nd)
        else:
            nodes[n]['count'] = 1
            
    #nodes[n]['refs']= [  ]
    
    return nodes[n]['node']


def declare(n):

    if not isinstance(n, basestring):
        n = n.value

    #print "decl %s" % n
                
    if n not in nodes:
        nodes[n]= {'decl':1,
                   'node': Node(n)
        }
    else:
        if 'decl' in nodes[n] :
            nodes[n]['decl'] = nodes[n]['decl'] +1
        else:
            nodes[n]['decl'] = 1
        
    return nodes[n]['node']

def statement(x):
    #print "statement %s" % pprint.pformat(x)
    
    global stack
    global astack
    
    if x:
        nid = x.nid()
        #print 'Statement: %s' % nid
        
        #nid = "%s" % x.nid()
        

        #print "stmt %s" % nid
        
        #print "Debug",x,x.nid()
        #pprint.pprint(x)
        #pprint.pprint(x.__dict__)
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
            #print s,sn,x
            nodes[s]['node'].usedby(x,sn)
        
        stack=[]
        astack=[]        
        

def report():
    for n in nodes.keys():
        d = nodes[n]
        dc = None
        if 'decl' in d:
            dc=d['decl']

        # now we resolve the references
        
        pprint.pprint({
            #'tst':1,
            'n' : n,
            'data'  : d,
            'dcl': dc
        })
    
    
    
def attrs(v):
    #pprint.pprint(v)
    astack.append(v)
