import pprint 

class Graph:

    def __init__(self, data):
        self.data = data
        self.idx = {}

        # create a node index
        for n in self.nodes(): # 
            nid = n.node_id()
            self.idx[nid]=n.pos

    def node(self, i):
        # based on offset
        if i < len(self.data):
            es = self.data[i]
            if es :
                return Node(es, i, self)
        else:
            pprint.pprint(sorted([x[0] for x in self.data]))
            raise Exception("not in graph %s" % i )

    def node_id(self, i):
        if i  in self.idx:
            j = self.idx[i]
            return self.node(j)

    def nodes(self):
        return Nodes(self.data, self)

class Nodes:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent

    def __iter__(self):
        return NodeIter(self.data, 0, self.parent)

class NodeIter:
    def __init__(self, data, pos, parent):
        self.data = data
        self.pos = pos
        self.l = len(data)
        self.parent = parent

    def next(self):
        p = self.pos
        self.pos = self.pos +1
        if p < self.l:
            d = self.data[p]
            if len(d) > 1 :
                #print "next", p, d
                return Node(d,p, self.parent)
        else:
            raise StopIteration

class Node :
    """
    Handle a node
    """
    NODEID=0
    TYPENAME=1
    REFED_IDS = 2
    REFED_OBJS = 3
    VALUE_FIELDS = 4

    TypeNames = {}

    def __init__(self, data, pos, parent):
        self.data = data
        self.pos = pos
        self.parent = parent

    @property
    def id(self):
        return self.node_id()

    def node_id (self):
        return self.data[Node.NODEID]

    def typename (self):
        return self.data[Node.TYPENAME]

    def fields (self):
        #print(self.data)
        return Fields(self.data[Node.REFED_IDS], self.parent)

    def val_fields (self):
        return Fields(self.data[Node.VALUE_FIELDS], self.parent)

    def specialize(self, visitor):
        tn = self.typename()
        if tn in self.TypeNames :
            return self.TypeNames[tn](self, visitor)
        else:

            n = "".join([f.title() for f in tn.split("_")])
                            
            print "    class %s(Base):" % n
            print "        CLASS='%s'\n" % tn
            print "        def generate(self):\n            print \"%s\"\n" % tn


            raise Exception( "missing %s " % tn)


class Fields :
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent

    def field(self, i):
        return Field(self.data[i], self.parent)

    def __iter__(self):
        return FieldIter(self.data, 0, self.parent)

class FieldIter:

    def __init__(self, data, pos, parent):
        self.data = data
        self.pos = pos
        self.l = len(data)
        self.parent = parent

    def next(self):
        p = self.pos
        self.pos = self.pos +1
        if p < self.l:
            d = self.data[p]
            #print d
            if d and len(d) > 1 :
                return Field(d, self.parent)
            else:
                if (d):
                    return FieldTodo(d)
                else:
                    return FieldEmpty()
        else:
            raise StopIteration

class Field :
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
    NAME = 0
    VALUE = 1

    def name(self):
        return self.data[Field.NAME]

    def value(self):
        return self.data[Field.VALUE]

    def resolve(self):
        return self.parent.node_id(self.value())

class FieldTodo :
    def __init__(self, data):
        assert(data)
        self.data = data

    def name(self):
        return "TODO"

    def value(self):
        print "value", self.data
        return self.data[Field.NAME]

class FieldEmpty :
    def name(self):
        return None

    def value(self):
        return None

