

class NodeBase:

    def __init__(self, nid, ntype, vals):
        self.node_id = nid
        self.node_type = ntype
        self.vals=vals

    def keys(self):
        
        if (self.vals):
            if isinstance(self.vals, list):
                return [x.keys() for x in self.vals if x.keys()]
            else:
                return self.vals.keys()
        
    def __str__(self):
        val=""
        if (self.vals):
            if isinstance(self.vals, list):
                #print "CHECK node type %s" % str(self.node_type)
                #print "CHECK node id %s" % str(self.node_id)
                #print "CHECK VALS %s" % str(self.vals)
                #print "CHECK VALS2 %s" % str( [attr.type for attr in self.vals]                )
                #print "CHECK VALS3 %s" % str( [str(attr) for attr in self.vals]               )
                
                #val="|".join(sorted([attr.type for attr in self.vals]))
                val="|".join(["Val:%s %s" % (str(attr.type), attr) for attr in self.vals])
            else:
                #print "CHECK VAL TYPE %s" % str(self.vals.type)
                val="Val %s %s" % (self.vals.type, self.vals),
        return "T|%s|%s"  % (self.node_type,val)

class Node(NodeBase):

    def __init__(self, ntype, nid, vals):
        NodeBase.__init__(self,nid, ntype, vals)

class ExprBase(Node):
    pass

class AddrExpr(ExprBase):
    def __init__(self, ntype, nid, op_0):
        ExprBase.__init__(self,ntype, nid,[])
        self.op_0=op_0

    def __str__(self):
#        return "T|%s|OP_0|%s"  % (self.node_type,self.op_0)
        return "T|%s|OP_0" % self.node_type

class AddrExprTyped(AddrExpr):
    def __init__(self, ntype, nid, op_0, expr_type):
        AddrExpr.__init__(self,ntype, nid, op_0)
        self.expr_type=expr_type

    def __str__(self):
        #return "T|%s|OP_0|%s|TYPE|%s"  % (self.node_type,self.op_0, self.expr_type)
        return "T|%s|OP_0|TYPE"  % (self.node_type)
    

class NodeConstructor(NodeBase):

    def __init__(self, ntype, nid, vals):
        NodeBase.__init__(self,nid, ntype, vals)


class Value(object):

    def __init__(self, v):
        self.val = v

    def keys(self):
        pass


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
        #assert(v)
        #print "create node ref %s" % v
        Value.__init__(self, v)

    def keys(self):
        return self.val



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

    @property
    def type(self):
        return "STR"


class Note(Value):

    def __init__(self, v):
        Value.__init__(self, v)


class FloatSpec(Float):

    def __init__(self, v, v2):
        self.spec = v2
        Float.__init__(self, v)


class AttrBase(object):

    @property
    def type(self):
        return "TODO(%s)" % self.__class__.__name__


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

    def keys(self):
        if isinstance(self.value, str):
            #return "Str: "+ self.value
            #return "Str: "+ self.value
            return None
        else:
            return self.value.keys()

    @property
    def type(self):
        return self.name


class EmptyAttr(AttrBase):
    pass


class SpecAttrBase(AttrBase):

    @property
    def type(self):
        return "spec"

class SpecAttr2(SpecAttrBase):

    def __init__(self, value, value2):
        self.name = 'spec'
        self.value = value
        self.value2 = value2

    @property
    def type(self):
        return self.name


class SpecAttr(SpecAttrBase):

    def __init__(self, name, value, value2):
        self.name = name
        self.value = value
        self.value2 = value2


class FilePos(Attr):

    def __init__(self, value):
        Attr.__init__(self, 'file', value)


class FileBuiltin(AttrBase):
    pass
