import sched_dep
import os
import pprint

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
    discovered = {}
    S =[]
    S.append(v)
    result = []
    while S:
        v = S.pop()
        if v not in discovered:
            discovered[v]=1
            if v not in G :
                print "missing %s" % v
                raise Exception("Missing %s" % v)
            else:
                es = G[v]
                if es :
                    typename = es[0]

                    #print es
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

                                    if skip == 0:
                                        if d not in discovered:
                                            S.append(d)                                    

                                    newdata = [e[0],e[1],G[d]]
                                    newlist.append(newdata)

                            newobj = [es[0],es[1],newlist,es[2]]
                            result.append(newobj)

    return result


k = sched_dep.data.keys()

#c = DFS2(sched_dep.data,"1")

g = Graph(sched_dep.data)


if not os.path.exists("cache"):
    os.makedirs("cache")

for x in k:

    n =  sched_dep.data[x]
    strings = []
    typename = n[0]
    #    if n[0].find('decl') >= 0:        
    if typename in ('function_decl', 'type_decl', 'var_decl', 'template_decl', 'namespace_decl', 'const_decl', 'using_decl' ) :
        data = {}
        data[x]=n
        S = DFS2(sched_dep.data,x)
        # if (len(S)>0):
        #     for y in S:
        #         if y:
        #             if y in sched_dep.data:
        #                 n2 = sched_dep.data[y]
        #                 # for st in n2[2] :
        #                 #     if st:
        #                 #         if st[0]=="String":
        #                 #             strings.append(st[1])
        #                 data[y]=n2
        filename = "cache/%s.py" % x
        o =open (filename,"w")
        o.write("data=%s" % pprint.pformat(S))
        o.close()
        print "wrote %s %s" % (filename, n[0])
    else:
        pass

