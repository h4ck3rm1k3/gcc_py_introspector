"""
Take a file and extract the lines that are sources
"""
from cache._00013930 import data
from subgraph import *

g = Graph(data)

class SrcP :
    def __init__(self, data):
        self.data =data

seen = {} 

for n in g.nodes(): # todo sort topologically
    #print n.typename()
    for f in n.val_fields():
        if f.name() == 'srcp':
            v = f.value()
            if v not in seen:
                seen[v]=1
#                print f.name(), f.value()

for x in sorted(seen.keys()):
    print x
