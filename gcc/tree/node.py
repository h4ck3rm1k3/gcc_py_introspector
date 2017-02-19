import gcc.tree.nodes

class Node :
    def __init__(self, n):
        self.n = n
        self.refs = []
        self._node_type = 'unknown'
        
    def node_type(self):
        
        if 'decl' in gcc.tree.nodes.Nodes.nodes[self.n]:
            return gcc.tree.nodes.Nodes.nodes[self.n]['decl'].node_type
        else:
            return 'unknown'
    
    def nid(self):
        return self.n
    
    def value(self):
        return self.n

    def format_refs(self):
        #r = ""
        r = "refs %s" % len(self.refs)
        # for s in self.refs:
        #     r = r + s[1] + ':'+ s[0]
        return r
    #def default(self, x):
    #    return {}
    #def __repr__(self):
        #return "Node : %s Refs: %s" % (self.n,len(self.refs))
    #    return "!Node:id='%s',refs:'%s'!" % (self.n, self.format_refs())
    #def ref(self, obj):
    #    self.refs.append(obj)

    def usedby(self, x, n):
        self.refs.append([x.nid(),n])
