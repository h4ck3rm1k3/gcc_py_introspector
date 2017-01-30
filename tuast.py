import re
from attributes import node_type
import pprint

class NodeBase:

    def __init__(self, nid, ntype):
        #print "node id %s" % nid
        self.node_id = nid
        self.node_type = ntype
        #self.vals=vals

    # def keys(self):
        
    #     if (self.vals):
    #         if isinstance(self.vals, list):
    #             return  [
    #                 self.node_type, 
    #                 [
    #                     x.keys() for x in self.vals if x.keys()
    #                 ], 
    #                 [
    #                     x.values() for x in self.vals if x.values()
    #                 ]
    #             ]
    #         else:
    #             return [
    #                 self.node_type, 
    #                 #[self.vals.keys()], 
    #                 #[self.vals.values()]
    #             ]
    #     else:
    #         return  [
    #             self.node_type, 
    #                 [], 
    #                 []
    #             ]
                
    # def __str__(self):
    #     val=""
    #     if (self.vals):
    #         if isinstance(self.vals, list):
    #             #print "CHECK node type %s" % str(self.node_type)
    #             #print "CHECK node id %s" % str(self.node_id)
    #             #print "CHECK VALS %s" % str(self.vals)
    #             #print "CHECK VALS2 %s" % str( [attr.type for attr in self.vals]                )
    #             #print "CHECK VALS3 %s" % str( [str(attr) for attr in self.vals]               )
                
    #             #val="|".join(sorted([attr.type for attr in self.vals]))
    #             val="|".join(["Val:%s %s" % (str(attr.type), attr) for attr in self.vals])
    #         else:
    #             #print "CHECK VAL TYPE %s" % str(self.vals.type)
    #             #val="Val %s %s" % (self.vals.type, self.vals),
    #             pass
    #     return "T|%s|%s"  % (self.node_type,val)

node_dict = {}

class Node(NodeBase):
    def __init__(self, nid, ntype ):
        NodeBase.__init__(self,nid, ntype)
        global node_dict
        # save the node dictionary
        node_dict[nid]=self


class ExprBase(Node):
    pass

# class AddrExpr(ExprBase):
#     def __init__(self, ntype, nid, op_0):
#         ExprBase.__init__(self,ntype, nid,[])
#         self.op_0=op_0

#     def __str__(self):
# #        return "T|%s|OP_0|%s"  % (self.node_type,self.op_0)
#         return "T|%s|OP_0" % self.node_type

# class AddrExprTyped(AddrExpr):
#     def __init__(self, ntype, nid, op_0, expr_type):
#         AddrExpr.__init__(self,ntype, nid, op_0)
#         self.expr_type=expr_type

#     def __str__(self):
#         #return "T|%s|OP_0|%s|TYPE|%s"  % (self.node_type,self.op_0, self.expr_type)
#         return "T|%s|OP_0|TYPE"  % (self.node_type)
    

# class NodeConstructor(NodeBase):

#     def __init__(self, ntype, nid, vals):
#         NodeBase.__init__(self,nid, ntype, vals)


class Value(object):
    """
    Base class for all field attributes
    """
    def __init__(self, v):
#        assert(v)
        self.val = v

    def keys(self):
        pass

    def values(self):
        return self.val

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

    def values(self):
        pass



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

    def keys(self):
        pass

    def values(self):
        return ["String",self.val]

class String2(Value):

    def __init__(self, v):
        m = re.match(r'(.*)lngt: (\d+)\s+addr:\s+([a-h0-9]+)$',v)
        if m :
            l = int(m.group(2))
            v2 = v[0:l]
            self.addr = m.group(3)
            Value.__init__(self, v2)
        else:
            Value.__init__(self, v)

    @property
    def type(self):
        return "STR"

    def keys(self):
        pass

    def values(self):
        return ["String",self.val]

    def __repr__(self):
        return "'%s'" % (self.val)

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

    def keys(self):
        pass

    def values(self):
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

    def keys(self):
        if isinstance(self.value, str):
            #return "Str: "+ self.value
            #return "Str: "+ self.value
            return None
        else:
            if self.value.keys():
                return [self.name, self.value.keys()]
            else:
                return None

    def values(self):
        if isinstance(self.value, str):
            return self.value
        else:
            if self.value.values():
                return [self.name, self.value.values()]
            else:
                return None

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

class SpecAttr3(SpecAttrBase):

    def __init__(self, value):
        self.name = 'spec'
        self.value = value

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

#  'addr_expr ': 335,
#  'array_ref': 61,
#  'array_type': 105,
#  'bind_expr': 66,
#  'bit_and_expr': 26,
#  'bit_field_ref': 1,
#  'bit_ior_expr': 31,
#  'bit_not_expr': 1,
#  'boolean_type': 1,
#  'call_expr': 201,
#  'case_label_expr': 47,
#  'complex_type': 5,
#  'component_ref': 107,
#  'compound_expr': 18,
#  'cond_expr': 292,
#  'const_decl': 578,
#  'convert_expr': 83,
#  'decl_expr': 83,
#  'enumeral_type': 44,
#  'eq_expr': 121,
#  'field_decl': 900,
#  'function_decl': 2711,
#  'function_type': 1013,
#  'ge_expr': 10,
#  'goto_expr': 200,
#  'gt_expr': 9,
#  'indirect_ref': 276,
#  'integer_cst': 603,
#  'integer_type': 271,
#  'label_decl': 183,
#  'label_expr': 136,
#  'le_expr': 13,
#  'lshift_expr': 6,
#  'lt_expr': 17,
#  'mem_ref': 1,
#  'minus_expr': 20,
#  'modify_expr': 413,
#  'mult_expr': 47,
#  'ne_expr': 187,
#  'negate_expr': 5,
#  'nop_expr': 431,
#  'parm_decl': 83,
#  'plus_expr': 31,
#  'pointer_bounds_type': 1,
#  'pointer_plus_expr': 90,
#  'pointer_type': 433,
#  'postincrement_expr': 56,
#  'predict_expr': 12,
#  'preincrement_expr': 8,
#  'real_type': 9,
#  'record_type': 239,
#  'reference_type': 1,
#  'result_decl': 44,
#  'return_expr': 51,
#  'rshift_expr': 3,
#  'statement_list': 179,
#  'string_cst': 112,
#  'switch_expr': 4,
#  'target_expr': 14,
#  'translation_unit_decl': 1,
#  'tree_list': 2902,
#  'trunc_div_expr': 4,
#  'truth_and_expr': 21,
#  'truth_andif_expr': 30,
#  'truth_or_expr': 2,
#  'truth_orif_expr': 37,
#  'type_decl': 557,
#  'union_type': 39,
#  'var_decl': 280,
#  'vector_type': 12,
#  'void_type': 5

class Decl(Node):
    pass

@node_type('function_decl')
class FunctionDecl(Decl):
    def __init__(self, nodeid, nodetype , nodedata):
        #print "Nodetype '%s'" %nodetype
        #print "Nodeid '%s'" %nodeid.value
        Decl.__init__(self,nodeid.value, nodetype)
        #self.value = nodedata.slice[-1].value.val
        #
        #pprint.pprint(nodedata.slice[-1].__dict__)
        #pprint.pprint([nodeid.value,nodetype,nodedata.slice])
    def __str__(self):
        return "FunctionDecl: %s %s " % (self.node_id, pprint.pformat(self.__dict__))
    
@node_type('identifier_node')
class Identifier(Node):
    def __init__(self, nodeid, nodetype , nodedata):
        #print "Nodetype '%s'" %nodetype
        #print "Nodeid '%s'" %nodeid.value
        Node.__init__(self,nodeid, nodetype)
        self.value = nodedata.slice[-1].value.val
        self.addr = nodedata.slice[-1].value.addr
        #pprint.pprint    ([nodeid.value,nodetype,nodedata.slice[-1].value])
    def __str__(self):
        return "Identifier: %s %s " % (self.node_id, self.value)
