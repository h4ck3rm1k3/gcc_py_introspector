import pprint
import ply.lex as lex

class Node :
    def __init__(self, n):
        self.n = n
        
    def value(self):
        return self.n
    
    def __repr__(self):
        return self.n
    
nodes = {}


def reference(n):

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

def report():
    pprint.pprint(nodes)
