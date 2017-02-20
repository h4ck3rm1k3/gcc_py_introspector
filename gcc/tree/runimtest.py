import os
import sys
import pickle
import pprint

# The folder containing files.
directory = sys.argv[1]
print(('going to read %s' % (directory)))

# Get all files.
list = os.listdir(directory)

# Loop and add files to list.
pairs = []
for file in list:

    if (file.endswith(".tu") or file.endswith(".t")) and '#' not in file:
        # Use join to get full file path.
        location = os.path.join(directory, file)

        # Get size and add to list of tuples.
        size = os.path.getsize(location)
        pairs.append((size, file))

# Sort list of tuples by the first element, size.
pairs.sort(key=lambda s: s[0])
import subprocess
import os.path


# Display pairs.
import time
from threading import Thread
import gcc.tree.tuast 
all_nodes = {}
fields = {}
#fields2 = {}
maxlen={}
def getlen(v2):
    if isinstance(v2, str):    
        return len(v2)
    else:
        if (isinstance(v2,gcc.tree.tuast.String2)):
            #print (type(v2))
            #pprint.pprint( v2.__dict__)
            #pprint.pprint(v2)
            return len(v2.val)
        else:
            raise Exception()
            
def proc(n):
    print ("running test %s" % n)

    f = "%s/%s.nodes.pickle" % (directory,n)
    if not os.path.isfile(f) :
        print ('skip'+f)
        return
    
    print (f)
    
    f2 = open (f,"rb")
    node_objs = pickle.load(f2)

    for x in node_objs.keys():

        d = node_objs[x]
        ntype = d['type']
        
        if ntype in fields :
            fields2 = fields[ntype]
        else:
            fields2 = {}
            
        for f in d:
            v = d[f]
            
            if isinstance(v, str):
                fl = len(v)
                if f in maxlen:
                    if fl > maxlen[f]:
                        maxlen[f]=fl
                    else:
                        pass
                else:
                    maxlen[f]=fl
                        
                if f not in fields2:
                    fields2[f]=1
                else:
                    fields2[f]=fields2[f]+1
                
            else:
                if f =='refs':
                    for f2 in v:

                        v2 = v[f2]
                        d2 = node_objs[v2]
                        ntype2 = d2['type']

                        if f2.startswith('E'):
                            f2='E'
                        f2=f2.replace(' ','')
                        f2=f2.replace(':','')
                        f3 = f + '_'+ f2
                        
                        if f3 in fields2:
                            if ntype2 in fields2[f3]:
                                fields2[f3][ntype2]= fields2[f3][ntype2] + 1
                            else:
                                fields2[f3][ntype2]= 1
                                
                        else:
                            fields2[f3]={ntype2:1}
                            
                else:
                    for f2 in v:
                        f3 = f + '_'+ f2
                        if f3 not in fields2:
                            fields2[f3]=1
                        else:
                            fields2[f3]=fields2[f3]+1
                        v2 = v[f2]
                        fl = getlen(v2)
                        if f2 in maxlen:
                            if fl > maxlen[f2]:
                                maxlen[f2]=fl
                            else:
                                pass
                        else:
                            maxlen[f2]=fl

                            
            fields[ntype]=fields2
            
    all_nodes[f]=node_objs

threads = []
for pair in pairs:

    n = pair[1]
    t = Thread(target=proc, args=(n,))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()
    
#pprint.pprint(fields)
pprint.pprint(maxlen)
