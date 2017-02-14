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

import gcc.tree.transform

r = gcc.tree.transform.Resolver(node_objs)
        
for x in ['1',]:#sorted(list(node_objs.keys()), key=int):
    r.transform(x)
