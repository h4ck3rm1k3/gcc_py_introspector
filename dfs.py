import sched_dep
import os

class Graph:

    def __init__(self, data):
        self.data = data

    def node(self, i):
        if i in self.data:
            es = self.data[i]
            if es :
                return Node(es)
        else:
            pass

class Node :
    """
    Handle a node
    """
    def __init__(self, data):
        self.data = data

    def typename (self):
        return self.data[0]

    def fields (self):
        return Fields(self.data[1])

class Fields :
    def __init__(self, data):
        self.data = data

    def field(self, i):
        return Field(self.data[i])

    def __iter__(self):
        return FieldIter(self.data, 0)

class FieldIter:
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
        self.l = len(data)

    def next(self):
        p = self.pos
        self.pos = self.pos +1
        if p < self.l:
            d = self.data[p]
            if len(d) > 1 :
                return Field(d)
            else:
                return FieldTodo(d)
        else:
            raise StopIteration

class Field :
    def __init__(self, data):
        self.data = data

    def name(self):
        return self.data[0]

    def value(self):
        return self.data[1]

class FieldTodo :
    def __init__(self, data):
        self.data = data

    def name(self):
        return "TODO"

    def value(self):
        return self.data[0]

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
                    if count == 0:
                        if typename not in ('function_decl', 'type_decl', 'var_decl', 'template_decl', 'namespace_decl', 'const_decl', 'using_decl', 'field_decl','parm_decl'):
                            return []

                    # print typename, count
                    if es:
                        for e in es[1]:
                            if e and len(e)> 1:
                                field = e[0]
                                d = e[1]
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
                                        # print field;
                                        S.append(d)
                                        count = count +1
                                else:
                                    discovered[d]=1
                            else:
                                #print e
                                pass
    return discovered.keys()


k = sched_dep.data.keys()

#c = DFS2(sched_dep.data,"1")

g = Graph(sched_dep.data)


if not os.path.exists("cache"):
    os.makedirs("cache")

for x in k:
    data = {}
    n =  sched_dep.data[x]
    data[x]=n
    S = DFS2(sched_dep.data,x)
    if (len(S)>0):
        for y in S:
            if y:
                if y in sched_dep.data:
                    n2 = sched_dep.data[y]
                    data[y]=n

    o =open ("cache/%s.py" % x,"w")
    o.write("data=%s" % data)
    o.close()
