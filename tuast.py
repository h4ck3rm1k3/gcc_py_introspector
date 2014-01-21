

class NodeBase:

    def __init__(self, nid, ntype, vals):
        self.node_id = nid
        self.node_type = ntype
        
        if (vals):
            for attr in vals:
                print ("ATTR %s" % attr)

    def __str__(self):

        return "str %s %s"  % (self.node_type, self.node_id)

class Node(NodeBase):

    def __init__(self, ntype, nid, vals):
        NodeBase.__init__(self,nid, ntype, vals)


class NodeConstructor(NodeBase):

    def __init__(self, ntype, nid, vals):
        NodeBase.__init__(self,nid, ntype, vals)


class Value(object):

    def __init__(self, v):
        self.val = v


class Link(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class VConstructor(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Struct(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Signed(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Artificial(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Qual(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Lang(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class NodeRef(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class NodeRefSpec(NodeRef):

    def __init__(self, v, v2):
        NodeRef.__init__(self, v)
        self.spec = v2


class PseudoTempl(Value):

    def __init__(self, v, v2):
        Value.__init__(self, v)
        self.v2 = v2


class Op(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class AccVal(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class AccSpec(AccVal):

    def __init__(self, v, v2):
        AccVal.__init__(self, v)
        self.spec = v2


class Spec(Value):
    def __init__(self, v):
        Value.__init__(self, v)


class Member(Value):
    def __init__(self, v):
        Value.__init__(self, v)


class Float(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class String(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class Note(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class FloatSpec(Float):

    def __init__(self, v, v2):
        self.spec = v2
        Float.__init__(self, v)


class AttrBase(object):
    pass


class MemberAttr(AttrBase):

    def __init__(self, value):
        self.value = value


class NoteAttr(AttrBase):

    def __init__(self, value):
        self.value = value


class Attr(AttrBase):

    def __init__(self, name, value):
        self.name = name
        self.value = value


class EmptyAttr(AttrBase):
    pass


class SpecAttr2(AttrBase):

    def __init__(self, value, value2):
        self.name = 'spec'
        self.value = value
        self.value2 = value2


class SpecAttr(AttrBase):

    def __init__(self, name, value, value2):
        self.name = name
        self.value = value
        self.value2 = value2


class FilePos(Attr):

    def __init__(self, value):
        Attr.__init__(self, 'file', value)


class FileBuiltin(AttrBase):
    pass
