import pprint 

class Graph:

    def __init__(self, data):
        self.data = data

    def node(self, i):
        if i < len(self.data):
            es = self.data[i]
            if es :
                return Node(es, i)
        else:
            pprint.pprint(self.data)
            raise Exception("not in graph %s" % i )


    def nodes(self):
        
        return Nodes(self.data)


class Nodes:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return NodeIter(self.data, 0)

class NodeIter:
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
                #print "next", p, d
                return Node(d,p)
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

    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

    def node_id (self):
        return self.data[Node.NODEID]

    def typename (self):
        return self.data[Node.TYPENAME]

    def fields (self):
        #print(self.data)
        return Fields(self.data[Node.REFED_IDS])

    def val_fields (self):
        return Fields(self.data[Node.VALUE_FIELDS])

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
            #print d
            if d and len(d) > 1 :
                return Field(d)
            else:
                if (d):
                    return FieldTodo(d)
                else:
                    return FieldEmpty()
        else:
            raise StopIteration

class Field :
    def __init__(self, data):
        self.data = data
    NAME = 0
    VALUE = 1
    def name(self):
        return self.data[Field.NAME]

    def value(self):
        return self.data[Field.VALUE]

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

