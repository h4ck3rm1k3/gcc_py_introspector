class TNode :
    def __init__(self, node_id, node_type, o):
        self.node_id=node_id
        self.node_type=node_type
        #self.o=o
    def nid(self):
        return self.node_id.n

    def pstack(self):
        r = ""
        debug( "Stack:%s" % pprint2.pformat(self.o.stack))
        #debug(pprint2.pformat(dir(self.o)))
        #debug(pprint2.pformat(self.o.__dict__))
        for s in self.o.stack:
            if s.type == '$end':
                pass
            else:
                s1= "pstack[type:%s t2:%s value:%s]," % (s.type, type(s.value), s.value.node_id)
                r = r + s1
                debug( "Stack",s,pprint2.pformat(s))
                #debug( "Stack",s,pprint2.pformat(dir(s)))
                debug( "Stack",s,pprint2.pformat(s.__dict__))
        return r
            
    def __repr__(self):
        return "!TNode:id='%s',type:'%s'!" % (
            self.node_id.n,
            self.node_type,
            #'pstack'
            #self.pstack()
            #pprint2.pformat(self.o.__dict__)
        )
