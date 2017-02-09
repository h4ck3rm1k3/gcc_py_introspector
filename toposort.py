def toposort(g):
    # L = Empty list that will contain the sorted elements
    L=[]
    # S = Set of all nodes with no incoming edges
    S={}
    incoming = {}

    # now collect all incoming edge count
    for n in g.nodes(): # 
        nid = n.node_id()
        tn= n.typename()

        for f in n.fields():
            m = f.value()
            fn = f.name()

            skip = 0 
            #print "seen ",tn, nid, fn, n.pos
            if tn in ('function_decl', 'type_decl', 'var_decl', 'template_decl', 'namespace_decl', 'const_decl', 'using_decl' ) :
                if fn in  'chain' : 
                    #print "skip", tn, fn
                    skip = 1

            if fn in ( 
                    'type',
                    'scpe',  # scope creates a loop
                    'unql') : # unql also
                skip = 1

            if skip == 0 :
                if m in incoming :
                    if nid not in incoming[m]:
                        incoming[m][nid] = fn
                        #print 'incoming', fn, m, nid
                else:
                    incoming[m] = {}
                    incoming[m][nid] = fn
                    #print 'incoming', fn, m, nid

    print("Incoming:", pprint.pformat(incoming))

    for n in g.nodes():
        nid = n.node_id()
        if nid not in incoming:
            #print nid, "not in incoming"  # this should be only the entry points
            S[nid]=1
            # and here we remove the 
            # for f in n.fields():
            #     m = f.value()
            #     fn = f.name()
            #     #if fn == 'chan':
            #         print 'removing', m, nid
            #         del incoming[m][nid]
                
    while len(list(S.keys())):

        #print "Keys now",S.keys()
        #print "List now",L

        keys = list(S.keys())
        first = keys[0]
        del S[first]
        #remove a node n from S

        #add n to tail of L
        if first not in L :
            L.append(first)

            #  for each node m with an edge e from n to m do
            #print "Process %s " % first
            if first in g.idx :
                fid = g.idx[first]
                n = g.node(fid)

                #print "N:%s" % n.__dict__
                for m in n.fields():
                    assert(m)
                    #print "field", m.__dict__
                    v = m.value()
                    if v and v in g.idx:
                        mid = g.idx[v]
                        #print "check mid offset %s %s" % (v,mid)

                        # remove edge e from the graph
                        if v in incoming:
                            if first in incoming[v]:
                                #print "remove incoming",v,first
                                del incoming[v][first]

                                if len (list(incoming[v].keys())) == 0:
                                    del incoming[v]

                        #if m has no other incoming edges then
                        if v not in incoming:
                            # insert m into S
                            S[v] = 1    
                            #print "adding v to S", v 
                        else:
                            if len(incoming[v])> 0:
                                #print "v still in in incoming", v, incoming[v]
                                pass
                            else:
                                # insert m into S
                                S[v] = 1    
                                #print "adding v to S", v 
                    else:
                        #print m.__dict__
                        #print "v %s not in idx" % v
                        #S[v] = 1
                        pass
            else:
                print("first not in idx", first)

    #print "Leftover",S.keys()
    
    #print "check for left overs"
    if len(list(incoming.keys())):
        for k in list(incoming.keys()):
            if k :
                if len(incoming[k]) > 0 :
                    #print "Check :" , k, incoming[k]
                    raise Exception("cycle %s" % k)
        #     return error (graph has at least one cycle)
        
    return L # (a topologically sorted order)

def walk_topo(g):
    v = Visitor()   
    for x in toposort(g):
        v._print ("Next in visit %s" % x)
        v.enter()
        n = g.node_id(x)
        ns = n.specialize(v)
        ns.generate()
        v.leave()
