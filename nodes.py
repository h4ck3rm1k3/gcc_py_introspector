import pprint
import ply.lex as lex

stack = []


class Node :
    def __init__(self, n):
        self.n = n
        
    def value(self):
        return self.n
    
    def __repr__(self):
        return self.n
    
nodes = {}


def reference(n):
    global stack

    stack.append(n)
    
    if not isinstance(n, basestring):
        n = n.value
        
    if n not in nodes:
        nodes[n]= {'count':1}
    else:
        if 'count' in  nodes[n]:
            nodes[n]['count'] = nodes[n]['count'] +1
        else:
            nodes[n]['count'] = 1
        
        #nodes[n]=1
    return Node(n)


def declare(n):

    if not isinstance(n, basestring):
        n = n.value

    if n not in nodes:
        nodes[n]= {'decl':1}
    else:
        if 'decl' in nodes[n] :
            nodes[n]['decl'] = nodes[n]['decl'] +1
        else:
            nodes[n]['decl'] = 1
        
    return Node(n)

def statement(x):
    global stack
    
    if x:
        nid = "%s" % x.nid()
        #print 'Statement:', nid, stack

        #print "Debug",x,x.nid()
        #pprint.pprint(x)
        #pprint.pprint(x.__dict__)
        if nid in nodes:
            nodes[nid]['decl'] = x
        else:
            nodes[nid] = { 'decl' : x }

        nodes[nid]['stack'] =list(stack)
        stack=[]        
        

def report():
    pprint.pprint(nodes)
    #pass

    
