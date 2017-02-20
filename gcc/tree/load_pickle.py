import pickle
#class SomeType:
#    def __call__(self):
#        pass
import gcc.tree.attributes
import gcc.tree.nodes
import gcc.tree.tuast
#from tinydb import TinyDB, where
import sys
f = open (sys.argv[1],"rb")
node_objs = pickle.load(f)

gcc.tree.nodes.Nodes.nodes=node_objs
import pprint

import gcc.tree.transform

pprint.pprint (node_objs)
    
#r = gcc.tree.transform.Resolver(node_objs)
        
#for x in sorted(list(node_objs.keys()), key=int):
    #pprint.pprint (x)
    #y = gcc.tree.transform.Resolver.transform(x)
    #pprint.pprint (y)

