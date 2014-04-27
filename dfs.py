import sched_dep


#print( )


#procedure DFS-iterative(G,v):
def DFS2(G,v):
    #let S be a stack
    discovered = {}
    S =[]
    S.append(v)
    count = 0
    while S:
        v = S.pop() 
        #if v is not labeled as discovered:
        if v not in discovered:
            #label v as discovered
            discovered[v]=1
            #for all edges from v to w in G.adjacentEdges(v) do
            #S.push(w)
            if v not in G :
                #print "missing %s" % v
                pass
            else:
                es = G[v]
                if es :
                    typename = es[0]
                    #print typename
                    if es :                    
                        for e in es[1]:
                            if e and len(e)> 1:
                                field = e[0]
                                d = e[1]
                                #print field 

                                skip = 0

                                if field == 'chain':
                                    if typename in ('function_decl', 'type_decl', 'var_decl', 'template_decl', 'namespace_decl', 'const_decl', 'using_decl' ) :
                                        skip =1
                                    elif typename in ('field_decl','parm_decl'):
                                        skip = 0
                                    else:
                                        print typename

                                if field == 'type':
                                    skip =1

                                if field == 'size':
                                    skip =1

                                if skip == 0:
                                    if d not in discovered:
                                        S.append(d)
                                        count = count +1
                            else:
                                #print e
                                pass
    return count


k = sched_dep.data.keys()
#c = DFS2(sched_dep.data,"1")
for x in k:
#    if x not in discovered:
        c = DFS2(sched_dep.data,x)
        if c >2000 :
            print "second pass %s %d" % (x,c)


