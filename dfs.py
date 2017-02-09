#import sched_dep
import os
import sys
import pprint


#procedure DFS-iterative(G,v):
def DFS2(G,v):
    discovered = {}
    S =[]
    S.append(v)
    result = []
    while S:
        v = S.pop()
        #print "eval %s" % v
        if v not in discovered:
            discovered[v]=1
            if v not in G :
                print("missing %s" % v)
                raise Exception("Missing %s" % v)
            else:
                es = G[v]
                if es :
                    typename = es[0]
                    if es:
                        if es[1]:
                            newlist = []
                            for e in es[1]:
                                if e and len(e)> 1:
                                    field = e[0]
                                    d = e[1]
                                    skip = 0
                                    # here we check if we want to skip the field
                                    if field == 'chain':
                                        if typename in ('function_decl', 'type_decl', 'var_decl', 'template_decl', 'namespace_decl', 'const_decl', 'using_decl' ) :
                                            skip =1
                                        elif typename in ('field_decl','parm_decl'):
                                            skip = 0
                                        elif n[0].find('decl') >= 0:        
                                            raise Exception(n[0])

                                    elif field in ('scpe','unql'):
                                        skip =1 # skip all the scope pointers for recursion, they create cycles

                                    if skip == 0:
                                        if d not in discovered:
                                            S.append(d)        

                                        # for skipped objects dont put the data pointer
                                        newdata = [field,d,[]
                                                   #G[d]
                                        ]
                                        newlist.append(newdata)
                                    else:
                                        #newdata = [field,d,[]]
                                        #newlist.append(newdata)
                                        pass

                            newobj = [v, es[0],es[1],
                                      #newlist
                                      []
                                      ,es[2]]
                            result.append(newobj)
                        else:
                            newobj = [v, es[0],es[1],
                                      #newlist
                                      []
                                      ,es[2]]
                            result.append(newobj)

                    else:
                        print("is empty %s" % v, es)
        else:
            #print "already discovered %s" % v
            pass
            
    return result




#c = DFS2(sched_dep.data,"1")
#g = Graph(sched_dep.data)


if not os.path.exists("cache"):
    os.makedirs("cache")

def main(input_data):
    k = list(input_data.data.keys())
    for x in k:
        n =  input_data.data[x]
        strings = []
        typename = n[0]
        #    if n[0].find('decl') >= 0:        
        if typename in ('function_decl', 'type_decl', 'var_decl', 'template_decl', 'namespace_decl', 'const_decl', 'using_decl' ) :
            data = {}
            data[x]=n
            S = DFS2(input_data.data,x)
            filename = "cache/_%0.8d.py" % int(x)
            o =open (filename,"w")
            o.write("data=%s" % pprint.pformat(S))
            o.close()
            print("wrote %s %s" % (filename, n[0]))
            #return
        else:
            pass

import importlib
if len(sys.argv) > 1 :
    name = sys.argv[1]
    module = importlib.import_module(name)
    main(module)
else:
    print("need module name")
