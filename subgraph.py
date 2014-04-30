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
                return Node(d)
        else:
            raise StopIteration

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

    def val_fields (self):
        return Fields(self.data[3])

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
        print "value", self.data
        return self.data[0]
