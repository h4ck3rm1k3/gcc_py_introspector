'''
reader
'''
import pprint

import ply.yacc as yacc # Get the token map from the lexer.  This is required.
from tu import tokens
import tuast  # import Link

def matches(psr_val, debug=True):
    c =0
    ret = []

    #print("DEBUG START")

    #if psr_val.slice[1].value:
        #print "Token Value:" + psr_val.slice[1].value
        #print "Token Type:" + psr_val.slice[1].type

    #for x in psr_val.slice:
        #print("MATCHES: %s" % x)
    #    pass

#    print("MATCHES: %s" % dir(psr_val.lexer.token) )
#    print("MATCHES: %s" % psr_val.lexer.lexliterals )
#    print("MATCHES: %s" % psr_val.lexer.lexdata )
#    print("MATCHES: %s" % psr_val.lexer.lexmatch.string )
    for group in psr_val.lexer.lexmatch.groups() :
        c = c+1
        if group:
           # print("DEBUG",c,group)
            ret.append(group)
    return ret



# the first rule is important
def p_node(psr_val):
    # the node declaration
    'node : NODE attr_list'
    #print "main NODE %s" % psr_val[1]
    #print "main TYPE %s" % psr_val[2]
    #print "main ATTRS %s" % psr_val[3]
    #print "main stack : %s" % psr_val.stack
    # psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    #psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])

#def p_ADDR_EXPR_node(psr_val):
#    'node : NODE ADDR_EXPR attr_list'
def p_CONSTRUCTOR_node(psr_val):
    'node : NODE CONSTRUCTOR attr_list'
def p_NTYPE_ARRAY_REF_node(psr_val):
    'node : NODE NTYPE_ARRAY_REF attr_list'
def p_NTYPE_ARRAY_TYPE_node(psr_val):
    'node : NODE NTYPE_ARRAY_TYPE attr_list'
def p_NTYPE_BIND_EXPR_node(psr_val):
    'node : NODE NTYPE_BIND_EXPR attr_list'
def p_NTYPE_BIT_AND_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_AND_EXPR attr_list'
def p_NTYPE_BIT_FIELD_REF_node(psr_val):
    'node : NODE NTYPE_BIT_FIELD_REF attr_list'
def p_NTYPE_BIT_IOR_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_IOR_EXPR attr_list'
def p_NTYPE_BIT_NOT_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_NOT_EXPR attr_list'
def p_NTYPE_BOOLEAN_TYPE_node(psr_val):
    'node : NODE NTYPE_BOOLEAN_TYPE attr_list'
def p_NTYPE_CALL_EXPR_node(psr_val):
    'node : NODE NTYPE_CALL_EXPR attr_list'
def p_NTYPE_CASE_LABEL_EXPR_node(psr_val):
    'node : NODE NTYPE_CASE_LABEL_EXPR attr_list'
def p_NTYPE_COMPLEX_TYPE_node(psr_val):
    'node : NODE NTYPE_COMPLEX_TYPE attr_list'
def p_NTYPE_COMPONENT_REF_node(psr_val):
    'node : NODE NTYPE_COMPONENT_REF attr_list'
def p_NTYPE_COMPOUND_EXPR_node(psr_val):
    'node : NODE NTYPE_COMPOUND_EXPR attr_list'
def p_NTYPE_COND_EXPR_node(psr_val):
    'node : NODE NTYPE_COND_EXPR attr_list'
def p_NTYPE_CONST_DECL_node(psr_val):
    'node : NODE NTYPE_CONST_DECL attr_list'
def p_NTYPE_CONVERT_EXPR_node(psr_val):
    'node : NODE NTYPE_CONVERT_EXPR attr_list'
def p_NTYPE_DECL_EXPR_node(psr_val):
    'node : NODE NTYPE_DECL_EXPR attr_list'
def p_NTYPE_ENUMERAL_TYPE_node(psr_val):
    'node : NODE NTYPE_ENUMERAL_TYPE attr_list'
def p_NTYPE_EQ_EXPR_node(psr_val):
    'node : NODE NTYPE_EQ_EXPR attr_list'
def p_NTYPE_FIELD_DECL_node(psr_val):
    'node : NODE NTYPE_FIELD_DECL attr_list'
def p_NTYPE_FUNCTION_DECL_node(psr_val):
    'node : NODE NTYPE_FUNCTION_DECL attr_list'
def p_NTYPE_FUNCTION_TYPE_node(psr_val):
    'node : NODE NTYPE_FUNCTION_TYPE attr_list'
def p_NTYPE_GE_EXPR_node(psr_val):
    'node : NODE NTYPE_GE_EXPR attr_list'
def p_NTYPE_GOTO_EXPR_node(psr_val):
    'node : NODE NTYPE_GOTO_EXPR attr_list'
def p_NTYPE_GT_EXPR_node(psr_val):
    'node : NODE NTYPE_GT_EXPR attr_list'

def p_NTYPE_IDENTIFIER_NODE_node(psr_val):
    'node : NODE NTYPE_IDENTIFIER_NODE attr_list'
def p_NTYPE_INDIRECT_REF_node(psr_val):
    'node : NODE NTYPE_INDIRECT_REF attr_list'
def p_NTYPE_INTEGER_CST_node(psr_val):
    'node : NODE NTYPE_INTEGER_CST attr_list'
def p_NTYPE_INTEGER_TYPE_node(psr_val):
    'node : NODE NTYPE_INTEGER_TYPE attr_list'
def p_NTYPE_LABEL_DECL_node(psr_val):
    'node : NODE NTYPE_LABEL_DECL attr_list'
def p_NTYPE_LABEL_EXPR_node(psr_val):
    'node : NODE NTYPE_LABEL_EXPR attr_list'
def p_NTYPE_LE_EXPR_node(psr_val):
    'node : NODE NTYPE_LE_EXPR attr_list'
def p_NTYPE_LSHIFT_EXPR_node(psr_val):
    'node : NODE NTYPE_LSHIFT_EXPR attr_list'
def p_NTYPE_LT_EXPR_node(psr_val):
    'node : NODE NTYPE_LT_EXPR attr_list'
def p_NTYPE_MEM_REF_node(psr_val):
    'node : NODE NTYPE_MEM_REF attr_list'
def p_NTYPE_MINUS_EXPR_node(psr_val):
    'node : NODE NTYPE_MINUS_EXPR attr_list'
def p_NTYPE_MODIFY_EXPR_node(psr_val):
    'node : NODE NTYPE_MODIFY_EXPR attr_list'
def p_NTYPE_MULT_EXPR_node(psr_val):
    'node : NODE NTYPE_MULT_EXPR attr_list'
def p_NTYPE_NE_EXPR_node(psr_val):
    'node : NODE NTYPE_NE_EXPR attr_list'
def p_NTYPE_NEGATE_EXPR_node(psr_val):
    'node : NODE NTYPE_NEGATE_EXPR attr_list'
def p_NTYPE_NOP_EXPR_node(psr_val):
    'node : NODE NTYPE_NOP_EXPR attr_list'
def p_NTYPE_PARM_DECL_node(psr_val):
    'node : NODE NTYPE_PARM_DECL attr_list'
def p_NTYPE_PLUS_EXPR_node(psr_val):
    'node : NODE NTYPE_PLUS_EXPR attr_list'
def p_NTYPE_POINTER_BOUNDS_TYPE_node(psr_val):
    'node : NODE NTYPE_POINTER_BOUNDS_TYPE attr_list'
def p_NTYPE_POINTER_PLUS_EXPR_node(psr_val):
    'node : NODE NTYPE_POINTER_PLUS_EXPR attr_list'
def p_NTYPE_POINTER_TYPE_node(psr_val):
    'node : NODE NTYPE_POINTER_TYPE attr_list'
def p_NTYPE_POSTINCREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_POSTINCREMENT_EXPR attr_list'
def p_NTYPE_PREDICT_EXPR_node(psr_val):
    'node : NODE NTYPE_PREDICT_EXPR attr_list'
def p_NTYPE_PREINCREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_PREINCREMENT_EXPR attr_list'
def p_NTYPE_REAL_TYPE_node(psr_val):
    'node : NODE NTYPE_REAL_TYPE attr_list'
def p_NTYPE_RECORD_TYPE_node(psr_val):
    'node : NODE NTYPE_RECORD_TYPE attr_list'
def p_NTYPE_REFERENCE_TYPE_node(psr_val):
    'node : NODE NTYPE_REFERENCE_TYPE attr_list'
def p_NTYPE_RESULT_DECL_node(psr_val):
    'node : NODE NTYPE_RESULT_DECL attr_list'
def p_NTYPE_RETURN_EXPR_node(psr_val):
    'node : NODE NTYPE_RETURN_EXPR attr_list'
def p_NTYPE_RSHIFT_EXPR_node(psr_val):
    'node : NODE NTYPE_RSHIFT_EXPR attr_list'
def p_NTYPE_STATEMENT_LIST_node(psr_val):
    'node : NODE NTYPE_STATEMENT_LIST attr_list'
def p_NTYPE_STRING_CST_node(psr_val):
    'node : NODE NTYPE_STRING_CST attr_list'
def p_NTYPE_SWITCH_EXPR_node(psr_val):
    'node : NODE NTYPE_SWITCH_EXPR attr_list'
def p_NTYPE_TARGET_EXPR_node(psr_val):
    'node : NODE NTYPE_TARGET_EXPR attr_list'
def p_NTYPE_TRANSLATION_UNIT_DECL_node(psr_val):
    'node : NODE NTYPE_TRANSLATION_UNIT_DECL attr_list'
def p_NTYPE_TREE_LIST_node(psr_val):
    'node : NODE NTYPE_TREE_LIST attr_list'
def p_NTYPE_TRUNC_DIV_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUNC_DIV_EXPR attr_list'
def p_NTYPE_TRUTH_AND_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_AND_EXPR attr_list'
def p_NTYPE_TRUTH_ANDIF_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_ANDIF_EXPR attr_list'
def p_NTYPE_TRUTH_OR_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_OR_EXPR attr_list'
def p_NTYPE_TRUTH_ORIF_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_ORIF_EXPR attr_list'
def p_NTYPE_TYPE_DECL_node(psr_val):
    'node : NODE NTYPE_TYPE_DECL attr_list'
def p_NTYPE_UNION_TYPE_node(psr_val):
    'node : NODE NTYPE_UNION_TYPE attr_list'
def p_NTYPE_VAR_DECL_node(psr_val):
    'node : NODE NTYPE_VAR_DECL attr_list'
def p_NTYPE_VECTOR_TYPE_node(psr_val):
    'node : NODE NTYPE_VECTOR_TYPE attr_list'
def p_NTYPE_VOID_TYPE_node(psr_val):
    'node : NODE NTYPE_VOID_TYPE attr_list'
def p_NTYPE_LANG_TYPE_node(psr_val):
    'node : NODE NTYPE_LANG_TYPE attr_list'
        
def p_NTYPE_CONTINUE_STMT_node(psr_val):
    'node : NODE NTYPE_CONTINUE_STMT attr_list'
    
def p_NTYPE_FOR_STMT_node(psr_val):
    'node : NODE NTYPE_FOR_STMT attr_list'
def p_NTYPE_USING_STMT_node(psr_val):
    'node : NODE NTYPE_USING_STMT attr_list'
def p_NTYPE_TEMPLATE_DECL_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_DECL attr_list'
def p_NTYPE_TEMPLATE_TYPE_PARM_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_TYPE_PARM attr_list'
def p_NTYPE_TREE_VEC_node(psr_val):
    'node : NODE NTYPE_TREE_VEC attr_list'
def p_NTYPE_PTRMEM_CST_node(psr_val):
    'node : NODE NTYPE_PTRMEM_CST attr_list'
def p_NTYPE_ARROW_EXPR_node(psr_val):
    'node : NODE NTYPE_ARROW_EXPR attr_list'
def p_NTYPE_CONST_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_CONST_CAST_EXPR attr_list'
def p_NTYPE_BINFO_node(psr_val):
    'node : NODE NTYPE_BINFO attr_list'
def p_NTYPE_REAL_CST_node(psr_val):
    'node : NODE NTYPE_REAL_CST attr_list'
def p_NTYPE_REINTERPRET_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_REINTERPRET_CAST_EXPR attr_list'
def p_NTYPE_SCOPE_REF_node(psr_val):
    'node : NODE NTYPE_SCOPE_REF attr_list'
def p_NTYPE_NW_EXPR_node(psr_val):
    'node : NODE NTYPE_NW_EXPR attr_list'
def p_NTYPE_ERROR_MARK_node(psr_val):
    'node : NODE NTYPE_ERROR_MARK attr_list'
def p_NTYPE_TYPEOF_TYPE_node(psr_val):
    'node : NODE NTYPE_TYPEOF_TYPE attr_list'
def p_NTYPE_NAMESPACE_DECL_node(psr_val):
    'node : NODE NTYPE_NAMESPACE_DECL attr_list'
def p_NTYPE_TRY_BLOCK_node(psr_val):
    'node : NODE NTYPE_TRY_BLOCK attr_list'
def p_NTYPE_MEMBER_REF_node(psr_val):
    'node : NODE NTYPE_MEMBER_REF attr_list'
def p_NTYPE_TRAIT_EXPR_node(psr_val):
    'node : NODE NTYPE_TRAIT_EXPR attr_list'
def p_NTYPE_THROW_EXPR_node(psr_val):
    'node : NODE NTYPE_THROW_EXPR attr_list'
def p_NTYPE_DYNAMIC_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_DYNAMIC_CAST_EXPR attr_list'
def p_NTYPE_DECLTYPE_TYPE_node(psr_val):
    'node : NODE NTYPE_DECLTYPE_TYPE attr_list'
def p_NTYPE_TYPEID_EXPR_node(psr_val):
    'node : NODE NTYPE_TYPEID_EXPR attr_list'
def p_NTYPE_EXPR_STMT_node(psr_val):
    'node : NODE NTYPE_EXPR_STMT attr_list'
def p_NTYPE_PREDECREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_PREDECREMENT_EXPR attr_list'
def p_NTYPE_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_CAST_EXPR attr_list'
def p_NTYPE_SIZEOF_EXPR_node(psr_val):
    'node : NODE NTYPE_SIZEOF_EXPR attr_list'
def p_NTYPE_TRUTH_NOT_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_NOT_EXPR attr_list'
def p_NTYPE_TEMPLATE_TEMPLATE_PARM_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_TEMPLATE_PARM attr_list'
def p_NTYPE_DL_EXPR_node(psr_val):
    'node : NODE NTYPE_DL_EXPR attr_list'
def p_NTYPE_POSTDECREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_POSTDECREMENT_EXPR attr_list'
def p_NTYPE_TEMPLATE_ID_EXPR_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_ID_EXPR attr_list'
def p_NTYPE_WHILE_STMT_node(psr_val):
    'node : NODE NTYPE_WHILE_STMT attr_list'
def p_NTYPE_OVERLOAD_node(psr_val):
    'node : NODE NTYPE_OVERLOAD attr_list'
def p_NTYPE_TAG_DEFN_node(psr_val):
    'node : NODE NTYPE_TAG_DEFN attr_list'
def p_NTYPE_TYPENAME_TYPE_node(psr_val):
    'node : NODE NTYPE_TYPENAME_TYPE attr_list'
def p_NTYPE_SWITCH_STMT_node(psr_val):
    'node : NODE NTYPE_SWITCH_STMT attr_list'
def p_NTYPE_TEMPLATE_PARM_INDEX_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_PARM_INDEX attr_list'
def p_NTYPE_BOUND_TEMPLATE_TEMPLATE_PARM_node(psr_val):
    'node : NODE NTYPE_BOUND_TEMPLATE_TEMPLATE_PARM attr_list'
def p_NTYPE_METHOD_TYPE_node(psr_val):
    'node : NODE NTYPE_METHOD_TYPE attr_list'
def p_NTYPE_BREAK_STMT_node(psr_val):
    'node : NODE NTYPE_BREAK_STMT attr_list'
def p_NTYPE_MODOP_EXPR_node(psr_val):
    'node : NODE NTYPE_MODOP_EXPR attr_list'
def p_NTYPE_BASELINK_node(psr_val):
    'node : NODE NTYPE_BASELINK attr_list'
def p_NTYPE_STATIC_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_STATIC_CAST_EXPR attr_list'
def p_NTYPE_TRUNC_MOD_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUNC_MOD_EXPR attr_list'
def p_NTYPE_OFFSET_TYPE_node(psr_val):
    'node : NODE NTYPE_OFFSET_TYPE attr_list'
def p_NTYPE_ALIGNOF_EXPR_node(psr_val):
    'node : NODE NTYPE_ALIGNOF_EXPR attr_list'
def p_NTYPE_DO_STMT_node(psr_val):
    'node : NODE NTYPE_DO_STMT attr_list'
def p_NTYPE_CTOR_INITIALIZER_node(psr_val):
    'node : NODE NTYPE_CTOR_INITIALIZER attr_list'
def p_NTYPE_IF_STMT_node(psr_val):
    'node : NODE NTYPE_IF_STMT attr_list'
def p_NTYPE_BIT_XOR_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_XOR_EXPR attr_list'
def p_NTYPE_USING_DECL_node(psr_val):
    'node : NODE NTYPE_USING_DECL attr_list'
def p_NTYPE_AGGR_INIT_EXPR_node(psr_val):
    'node : NODE NTYPE_AGGR_INIT_EXPR attr_list'
def p_NTYPE_HANDLER_node(psr_val):
    'node : NODE NTYPE_HANDLER attr_list'
def p_NTYPE_DOTSTAR_EXPR_node(psr_val):
    'node : NODE NTYPE_DOTSTAR_EXPR attr_list'


# def p_node_attrs(psr_val):
#     'node : NODE ntype attrs'
#     psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])
    
#def p_node_addr2(psr_val):
#     'attrs : addr_attrs'
#     psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])

def goto_initial(p):
    #print 'begin initial'
    #raise Exception('where')
    p.lexer.begin('INITIAL')  # begin the string group

# the first rule is important
def p_node_id(psr_val):
    # the identifier node declaration
    'node : NODE HEXVAL attr_list' # len_attrs
    #print "main NODE %s" % psr_val[1]
    #print "main TYPE %s" % psr_val[2]
    #print "main ATTRS %s" % psr_val[3]
    #print "main stack : %s" % psr_val.stack
    # psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    #psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])
    goto_initial(psr_val)  # begin the string group
    
# def p_node_id2(psr_val):
#     # no length
#     'node : NODE ntype_id attr_list ' # len_attrs
#     psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])
#     goto_initial(psr_val)
        
# def p_node_id3(psr_val):
#     # no length
#     'node : NODE ntype_id str_attrs'
#     psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])
#     goto_initial(psr_val)

# # # empty_node
# def p_node_empty(psr_val):
#      # the node with no attrs
#      'node : NODE ntype'
#      #print "empty node %s %s " % (psr_val[2], psr_val[1])
#      psr_val[0] = tuast.Node(psr_val[2], psr_val[1], [])


# def ntype_base(psr_val):
#     #print "debug 1 %s" % psr_val
#     ntype = psr_val[1]
#     #print "debug node type %s" % ntype
#     #print "debug 3 %s" % psr_val.stack
#     #psr_val[0] = ntype
#     return ntype

def attr_base(psr_val):
    m = psr_val.slice
    if len(m) > 1:
        attr = m[1].value
    else:
        attr =  ""
    #print "got attr %s" % attr
    return attr

def std_attrs(psr_val):
    """
    called for each attribute
    """
    #m=psr_val.slice
#    print "debug1",m

    type_str= psr_val[1]
    assert(type_str)
    #node = tuast.Attr(type_str, psr_val[2])
    #result = append_list(psr_val[3], node)
    
    return psr_val

def std_attrs2(psr_val):

    #print "val1: %s " %  psr_val[1]
    #print "val2: %s " %  psr_val[2]
    #print "val3: %s " %  psr_val[3]

#    m=matches(psr_val)
#    print "debug2",m
    type_str= psr_val[1]
    #print "std attrs 2 type_str %s " % psr_val[1]
#    if not type_str :
#        type_str = "UNKNOWN_TODO %s" % m
        
    #node = tuast.Attr(type_str, psr_val[2])
    #pprint.pprint(psr_val[0])
    #pprint.pprint(psr_val[1])
    #pprint.pprint(psr_val[2])
    #result = append_list(psr_val[3], node)
    return []


#create_rules()



##
def p_attr_accs(psr_val):
    'attrtype : ATTR_ACCS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_labl(psr_val):
    'attrtype : ATTR_LABL'
    #psr_val[0] = attr_base(psr_val)

def p_attr_vars(psr_val):
    'attrtype : ATTR_VARS'
    #psr_val[0] = attr_base(psr_val)

# def p_attr_addr(psr_val):
#     'attrtype : ATTR_ADDR'
#     #psr_val[0] = attr_base(psr_val)


def p_attr_alis(psr_val):
    'attrtype : ATTR_ALIS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_args(psr_val):
    'attrtype : ATTR_ARGS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_argt(psr_val):
    'attrtype : ATTR_ARGT'
    #psr_val[0] = attr_base(psr_val)

def p_attr_base(psr_val):
    'attrtype : ATTR_BASE'
    #psr_val[0] = attr_base(psr_val)

def p_attr_bases(psr_val):
    'attrtype : ATTR_BASES'
    #psr_val[0] = attr_base(psr_val)

def p_attr_binf(psr_val):
    'attrtype : ATTR_BINF'
    #psr_val[0] = attr_base(psr_val)

def p_attr_body(psr_val):
    'attrtype : ATTR_BODY'
    #psr_val[0] = attr_base(psr_val)

def p_attr_bpos(psr_val):
    'attrtype : ATTR_BPOS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_chain(psr_val):
    'attrtype : ATTR_CHAIN'
    #psr_val[0] = attr_base(psr_val)

def p_attr_chan(psr_val):
    'attrtype : ATTR_CHAN'
    #psr_val[0] = attr_base(psr_val)

def p_attr_clas(psr_val):
    'attrtype : ATTR_CLAS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_clnp(psr_val):
    'attrtype : ATTR_CLNP'
    #psr_val[0] = attr_base(psr_val)

def p_attr_cls(psr_val):
    'attrtype : ATTR_CLS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_cnst(psr_val):
    'attrtype : ATTR_CNST'
    #psr_val[0] = attr_base(psr_val)

def p_attr_cond(psr_val):
    'attrtype : ATTR_COND'
    #psr_val[0] = attr_base(psr_val)

def p_attr_crnt(psr_val):
    'attrtype : ATTR_CRNT'
    #psr_val[0] = attr_base(psr_val)

def p_attr_csts(psr_val):
    'attrtype : ATTR_CSTS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_ctor(psr_val):
    'attrtype : ATTR_CTOR'
    #psr_val[0] = attr_base(psr_val)

def p_attr_dcls(psr_val):
    'attrtype : ATTR_DCLS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_decl(psr_val):
    'attrtype : ATTR_DECL'
    #psr_val[0] = attr_base(psr_val)

def p_attr_domn(psr_val):
    'attrtype : ATTR_DOMN'
    #psr_val[0] = attr_base(psr_val)

def p_attr_else(psr_val):
    'attrtype : ATTR_ELSE'
    #psr_val[0] = attr_base(psr_val)

def p_attr_elts(psr_val):
    'attrtype : ATTR_ELTS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_expr(psr_val):
    'attrtype : ATTR_EXPR'
    #psr_val[0] = attr_base(psr_val)

def p_attr_flds(psr_val):
    'attrtype : ATTR_FLDS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_fn(psr_val):
    'attrtype : ATTR_FN'
    #psr_val[0] = attr_base(psr_val)

def p_attr_fncs(psr_val):
    'attrtype : ATTR_FNCS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_hdlr(psr_val):
    'attrtype : ATTR_HDLR'
    #psr_val[0] = attr_base(psr_val)

def p_attr_high(psr_val):
    'attrtype : ATTR_HIGH'
    #psr_val[0] = attr_base(psr_val)

def p_attr_init(psr_val):
    'attrtype : ATTR_INIT'
    #psr_val[0] = attr_base(psr_val)

def p_attr_inst(psr_val):
    'attrtype : ATTR_INST'
    #psr_val[0] = attr_base(psr_val)

def p_attr_lang(psr_val):
    'attrtype : ATTR_LANG'
    #psr_val[0] = attr_base(psr_val)

def p_attr_line(psr_val):
    'attrtype : ATTR_LINE'
    #psr_val[0] = attr_base(psr_val)

def p_attr_link(psr_val):
    'attrtype : ATTR_LINK'
    #psr_val[0] = attr_base(psr_val)

def p_attr_low(psr_val):
    'attrtype : ATTR_LOW'
    #psr_val[0] = attr_base(psr_val)

def p_attr_max(psr_val):
    'attrtype : ATTR_MAX'
    #psr_val[0] = attr_base(psr_val)

def p_attr_mbr(psr_val):
    'attrtype : ATTR_MBR'
    #psr_val[0] = attr_base(psr_val)

def p_attr_min(psr_val):
    'attrtype : ATTR_MIN'
    #psr_val[0] = attr_base(psr_val)

def p_attr_mngl(psr_val):
    'attrtype : ATTR_MNGL'
    #psr_val[0] = attr_base(psr_val)

def p_attr_name(psr_val):
    'attrtype : ATTR_NAME'
    #psr_val[0] = attr_base(psr_val)

def p_attr_nmsp(psr_val):
    'attrtype : ATTR_NMSP'
    #psr_val[0] = attr_base(psr_val)

def p_attr_note(psr_val):
    'attrtype : ATTR_NOTE'
    #psr_val[0] = attr_base(psr_val)

def p_attr_nst(psr_val):
    'attrtype : ATTR_NST'
    #psr_val[0] = attr_base(psr_val)

def p_attr_orig(psr_val):
    'attrtype : ATTR_ORIG'
    #psr_val[0] = attr_base(psr_val)

def p_attr_parm(psr_val):
    'attrtype : ATTR_PARM'
    #psr_val[0] = attr_base(psr_val)


def p_attr_prms(psr_val):
    'attrtype : ATTR_PRMS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_ptd(psr_val):
    'attrtype : ATTR_PTD'
    #psr_val[0] = attr_base(psr_val)

def p_attr_purp(psr_val):
    'attrtype : ATTR_PURP'
    #psr_val[0] = attr_base(psr_val)

def p_attr_qual(psr_val):
    'attrtype : ATTR_QUAL'
    #print ("QUAL:")
    #psr_val[0] = attr_base(psr_val)

def p_attr_refd(psr_val):
    'attrtype : ATTR_REFD'
    #psr_val[0] = attr_base(psr_val)

def p_attr_retn(psr_val):
    'attrtype : ATTR_RETN'
    #psr_val[0] = attr_base(psr_val)

def p_attr_rslt(psr_val):
    'attrtype : ATTR_RSLT'
    #psr_val[0] = attr_base(psr_val)

def p_attr_scpe(psr_val):
    'attrtype : ATTR_SCPE'
    #psr_val[0] = attr_base(psr_val)

def p_attr_sign(psr_val):
    'attrtype : ATTR_SIGN'
    #psr_val[0] = attr_base(psr_val)

def p_attr_size(psr_val):
    'attrtype : ATTR_SIZE'
    #psr_val[0] = attr_base(psr_val)

def p_attr_spcs(psr_val):
    'attrtype : ATTR_SPCS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_srcp(psr_val):
    'attrtype : ATTR_SRCP'
    #psr_val[0] = attr_base(psr_val)

def p_attr_sts(psr_val):
    'attrtype : ATTR_STS'
    #psr_val[0] = attr_base(psr_val)

def p_attr_tag(psr_val):
    'attrtype : ATTR_TAG'
    #psr_val[0] = attr_base(psr_val)

def p_attr_then(psr_val):
    'attrtype : ATTR_THEN'
    #psr_val[0] = attr_base(psr_val)

def p_attr_unql(psr_val):
    'attrtype : ATTR_UNQL'
    #psr_val[0] = attr_base(psr_val)

def p_attr_used(psr_val):
    'attrtype_used : ATTR_USED'
    #psr_val[0] = attr_base(psr_val)

def p_attr_val(psr_val):
    'attrtype : ATTR_VAL'
    #psr_val[0] = attr_base(psr_val)

def p_attr_idx(psr_val):
    'attrtype : ATTR_IDX'
    #psr_val[0] = attr_base(psr_val)

def p_attr_valu(psr_val):
    'attrtype : ATTR_VALU'
    #psr_val[0] = attr_base(psr_val)

def p_attr_vfld(psr_val):
    'attrtype : ATTR_VFLD'
    #psr_val[0] = attr_base(psr_val)

# special case for attribute OP 1 ... OP n
def p_attr_OP(psr_val):
    'attrtype : ATTR_OP'
    #psr_val[0] = attr_base(psr_val)

# special case for attribute E 1 ... E n
def p_attr_En(psr_val):
    'attrtype : ATTR_En'
    #psr_val[0] = attr_base(psr_val)


##########################################

def operator_base(psr_val):
    pass

def p_operator_add(psr_val):
    'op_type : OPERATOR_ADD'
    #psr_val[0] = operator_base(psr_val)

def p_operator_and(psr_val):
    'op_type : OPERATOR_AND'
    #psr_val[0] = operator_base(psr_val)

def p_operator_andassign(psr_val):
    'op_type : OPERATOR_ANDASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_addr(psr_val):
    'op_type : OPERATOR_ADDR'
    #psr_val[0] = operator_base(psr_val)

def p_operator_assign(psr_val):
    'op_type : OPERATOR_ASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_call(psr_val):
    'op_type : OPERATOR_CALL'
    #psr_val[0] = operator_base(psr_val)

def p_operator_compound(psr_val):
    'op_type : OPERATOR_COMPOUND'
    #psr_val[0] = operator_base(psr_val)

def p_operator_delete(psr_val):
    'op_type : OPERATOR_DELETE'
    #psr_val[0] = operator_base(psr_val)

def p_operator_deref(psr_val):
    'op_type : OPERATOR_DEREF'
    #psr_val[0] = operator_base(psr_val)

def p_operator_div(psr_val):
    'op_type : OPERATOR_DIV'
    #psr_val[0] = operator_base(psr_val)

def p_operator_divassign(psr_val):
    'op_type : OPERATOR_DIVASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_eq(psr_val):
    'op_type : OPERATOR_EQ'
    #psr_val[0] = operator_base(psr_val)

def p_operator_ge(psr_val):
    'op_type : OPERATOR_GE'
    #psr_val[0] = operator_base(psr_val)

def p_operator_gt(psr_val):
    'op_type : OPERATOR_GT'
    #psr_val[0] = operator_base(psr_val)

def p_operator_le(psr_val):
    'op_type : OPERATOR_LE'
    #psr_val[0] = operator_base(psr_val)

def p_operator_lnot(psr_val):
    'op_type : OPERATOR_LNOT'
    #psr_val[0] = operator_base(psr_val)

def p_operator_lshift(psr_val):
    'op_type : OPERATOR_LSHIFT'
    #psr_val[0] = operator_base(psr_val)

def p_operator_lshiftassign(psr_val):
    'op_type : OPERATOR_LSHIFTASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_lt(psr_val):
    'op_type : OPERATOR_LT'
    #psr_val[0] = operator_base(psr_val)

def p_operator_minus(psr_val):
    'op_type : OPERATOR_MINUS'
    #psr_val[0] = operator_base(psr_val)

def p_operator_minusassign(psr_val):
    'op_type : OPERATOR_MINUSASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_mult(psr_val):
    'op_type : OPERATOR_MULT'
    #psr_val[0] = operator_base(psr_val)

def p_operator_multassign(psr_val):
    'op_type : OPERATOR_MULTASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_ne(psr_val):
    'op_type : OPERATOR_NE'
    #psr_val[0] = operator_base(psr_val)

def p_operator_neg(psr_val):
    'op_type : OPERATOR_NEG'
    #psr_val[0] = operator_base(psr_val)

def p_operator_new(psr_val):
    'op_type : OPERATOR_NEW'
    #psr_val[0] = operator_base(psr_val)

def p_operator_or(psr_val):
    'op_type : OPERATOR_OR'
    #psr_val[0] = operator_base(psr_val)

def p_operator_orassign(psr_val):
    'op_type : OPERATOR_ORASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_plus(psr_val):
    'op_type : OPERATOR_PLUS'
    #psr_val[0] = operator_base(psr_val)

def p_operator_plusassign(psr_val):
    'op_type : OPERATOR_PLUSASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_postdec(psr_val):
    'op_type : OPERATOR_POSTDEC'
    #psr_val[0] = operator_base(psr_val)

def p_operator_postinc(psr_val):
    'op_type : OPERATOR_POSTINC'
    #psr_val[0] = operator_base(psr_val)

def p_operator_predec(psr_val):
    'op_type : OPERATOR_PREDEC'
    #psr_val[0] = operator_base(psr_val)

def p_operator_preinc(psr_val):
    'op_type : OPERATOR_PREINC'
    #psr_val[0] = operator_base(psr_val)

def p_operator_rshift(psr_val):
    'op_type : OPERATOR_RSHIFT'
    #psr_val[0] = operator_base(psr_val)

def p_operator_vecdelete(psr_val):
    'op_type : OPERATOR_VECDELETE'
    #psr_val[0] = operator_base(psr_val)

def p_operator_vecnew(psr_val):
    'op_type : OPERATOR_VECNEW'
    #psr_val[0] = operator_base(psr_val)

def p_operator_xor(psr_val):
    'op_type : OPERATOR_XOR'
    #psr_val[0] = operator_base(psr_val)

def p_operator_xorassign(psr_val):
    'op_type : OPERATOR_XORASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_not(psr_val):
    'op_type : OPERATOR_NOT'
    #psr_val[0] = operator_base(psr_val)

def p_operator_pos(psr_val):
    'op_type : OPERATOR_POS'
    #psr_val[0] = operator_base(psr_val)

def p_operator_ref(psr_val):
    'op_type : OPERATOR_REF'
    #psr_val[0] = operator_base(psr_val)

def p_operator_rshiftassign(psr_val):
    'op_type : OPERATOR_RSHIFTASSIGN'
    #psr_val[0] = operator_base(psr_val)

def p_operator_subs(psr_val):
    'op_type : OPERATOR_SUBS'
    #psr_val[0] = operator_base(psr_val)

def p_idx_val_list(p):
    'idx_val_list : ATTR_IDX NODE ATTR_VAL NODE idx_val_list' 

def p_idx_val_list2(p):
    'idx_val_list : ATTR_IDX NODE ATTR_VAL NODE' 

##########################################
def p_node_constructor(psr_val):
    #            1             2
    'node : NODE CONSTRUCTOR LEN idx_val_list attr_list'
    #print "CHECK LIST1 %s" % psr_val[3]
    # #psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    #psr_val[0] = tuast.NodeConstructor(psr_val[2], psr_val[1], psr_val[3])

# def p_node_mem_ref(psr_val):
#     'node : NODE NTYPE_MEM_REF attr_list'
#     ##psr_val[0] = tuast.NodeConstructor(psr_val[2], psr_val[1], psr_val[3])

# def p_addr_attrs3(psr_val):
#     'attrs :  addr_attrs'
#     #psr_val[0] = std_attrs2(psr_val)

    

def p_attrs(psr_val):
    'attrs :  attrtype attrval'
    # refactored to std function

    #psr_val[0] = std_attrs2(psr_val)


def append_list(current_list, node):
    if current_list :
        if isinstance(current_list,list):
            current_list.insert(0,node)
        else:
            current_list = [node, current_list]
        result = current_list
    else:
        result = node
    return result


# attributes like 'address: 5fa31238843838' in the newer compilers    
# the addr: attribute
def p_attrs_addr(psr_val):
    #           1     2         3
    'attrs :  ADDR_ATTR SOMEINT'
    #psr_val[0] = std_attrs(psr_val)

#


def p_attrs_op0(psr_val):
    #           1     2     3
    'attrs :  OP0_ATTR attrval'
    #psr_val[0] = std_attrs(psr_val)

def p_attrs_op1(psr_val):
    'attrs :  OP1_ATTR attrval'
    #psr_val[0] = std_attrs(psr_val)

# def p_attrs_done(psr_val):
#     'attrs : '
#     # print "final attrs %s" % p
#     #print (stack)
#     #psr_val[0] = [] # empty list

def p_attr_list(p):
    'attr_list : attrs attr_list'
    
def p_attr_list2(p):
    'attr_list : str_attrs attr_list' 


def p_attr_list4(p):
    'attr_list : addr_attrs attr_list'

def p_attr_list4a(p):
    'attr_list : addr_attrs'

def p_attr_lista(p):
    'attr_list : attrs'
    
def p_attr_list2a(p):
    'attr_list : str_attrs' 

def p_attr_list3a(p):
    'attr_list : type_attrs'

def p_attr_list3(p):
    'attr_list : type_attrs attr_list'
    

def p_attrs_spec2(psr_val):
#     #            1          2        3        4
     'attrs :  SPEC_ATTR SPEC_REGISTER '
#     attr_list = psr_val[4]
#     node = tuast.SpecAttr(psr_val[1], psr_val[2], psr_val[3])
#     #psr_val[0] = append_list(attr_list, node)
#     return psr_val[0]

def p_attrs_spec3(psr_val):
     #          1        2
     'attrs :  SPEC_VALU'
     #node = tuast.SpecAttr3(psr_val[1])
     ##psr_val[0] = append_list(psr_val[2], node)
     return psr_val[0]

# def p_attrs_spec1(psr_val):
#     #           1          2       3
#     'attrs :  SPEC_ATTR SPEC_VALU attrs'
#     node = tuast.SpecAttr2(psr_val[1], psr_val[2])
#     #psr_val[0] = append_list(psr_val[3], node)
#     return psr_val[0]


def p_attrs_note(psr_val):
    'attrs :  NOTE'
    # psr_val[0]="NOTE(%s)" % p
    #psr_val[0] = tuast.NoteAttr(psr_val[1])


# def p_strlist(psr_val):
#     'strlist : SOMESTRG strlist'
#     m=psr_val[1]
#     if m:
#         #print "string list '%s'" % m
#          #psr_val[0] = [tuast.String(m)]
#     #psr_val.lexer.begin('len')
    
# def p_strlist2(psr_val):
#      'strlist : SOMESTRG'
#      m=psr_val[1]
#      if m:
#          #print "matched string '%s'" % m
#           #psr_val[0] = [tuast.String(m)]
#      #psr_val.lexer.begin('len')

# def p_strlist3(psr_val):
#      'strlist : SOMESTRG addr_attrs'
#      m=psr_val[1]
#      if m:
#          #print "matched string '%s'" % m
#           #psr_val[0] = [tuast.String(m)]
#      psr_val.lexer.begin('len')
     
    
# def p_attrs_strg2(psr_val):
#     'str_attrs : STRG strlist'
#     m=psr_val[1]
#     if m:
#         print "single string '%s'" % m
#         #psr_val[0] = [tuast.String(m)]
#     goto_initial(psr_val)

def p_attrs_strg3(psr_val):
    'str_attrs : STRG SOMESTRG'
    m=psr_val[1]
    #if m:
        #print "simple string list '%s'" % m
        #psr_val[0] = [tuast.String(m)]
    goto_initial(psr_val)

def p_attrs_strg_empty(psr_val):
    'str_attrs : STRG ' # no string....
    m=psr_val[1]
    #if m:
        #print "simple string list '%s'" % m
        #psr_val[0] = [tuast.String(m)]
    goto_initial(psr_val)

def p_attrs_addrs(psr_val):
    'addr_attrs : ADDR_ATTR HEXVAL'
    m=psr_val[1]
    #if m:
        #print "address is set to", m
        #psr_val[0] = [tuast.String(m)]
    #print 'after hexval'
    goto_initial(psr_val)

def p_attrs_addrs2(psr_val):
    'addr_attrs : ADDR_ATTR SOMEHEX3'
    m=psr_val[1]
    #if m:
        #print "address is set to", m
        #psr_val[0] = [tuast.String(m)]
    goto_initial(psr_val)


def p_attrs_addrs3(psr_val):
    'addr_attrs : ADDR_ATTR SOMEHEX4'
    m=psr_val[1]
    #if m:
        #print "address is set to", m
        #psr_val[0] = [tuast.String(m)]
    goto_initial(psr_val)

# def p_attrs_strglen(psr_val):
#     'len_attrs : STRGLEN2 SOMEINT'
#     #goto_initial(psr_val)
#     m=psr_val[2]
#     if m:
#         #print "string length is :", m
#         #psr_val[0] = [tuast.String(m)]
#     #goto_initial(psr_val)

#def p_attrs_strglen2(psr_val):
#    'attrs : STRGLEN HEXVAL'
 #   goto_initial(psr_val)
 #   m=psr_val[1]
 #   if m:
 #       print "string with length", m
#        #psr_val[0] = [tuast.String(m)]

# def p_hexval(psr_val):
#     'hexval : STRGLEN HEXVAL'
#     m=psr_val[1]
#     if m:
#         print "strlen", m
#         #psr_val[0] = [tuast.String(m)]

 
# def p_attrs_strg_addr(psr_val):
#     'adr_attrs : ADDR_ATTR HEXVAL'
#     m=psr_val[1]
#     if m:
#         print "addr length", m
#         #psr_val[0] = [tuast.String(m)]



def p_attrs_member(psr_val):
    'attrs : MEMBER'
    # psr_val[0]="MEMBER(%s)" % psr_val[1]
    #psr_val[0] = tuast.MemberAttr(psr_val[1])


def p_attrval_note(psr_val):
    'attrval :  NOTE'
    # psr_val[0]="NOTE(%s)" % p
    #psr_val[0] = tuast.Note(psr_val[1])


def p_attrval_member(psr_val):
    'attrval : MEMBER'
    # psr_val[0]="MEMBER(%s)" % psr_val[1]
    #psr_val[0] = tuast.Member(psr_val[1])


def p_attrval_qual(psr_val):
    'attrval :  QUAL'
    #print "QUAL(%s)" % psr_val[1]
    #psr_val[0] = tuast.Qual(psr_val[1])


def p_attrval_artificial(psr_val):
    'attrval :  ARTIFICIAL'
    # psr_val[0]="ARTIFICAL(%s)" % psr_val[1]
    #psr_val[0] = tuast.Artificial(psr_val[1])


def p_attrval_signed(psr_val):
    'attrval :  SIGNED'
    # psr_val[0]="SIGNED(%s)" % psr_val[1]
    #psr_val[0] = tuast.Signed(psr_val[1])


def p_attrval_struct(psr_val):
    'attrval :  STRUCT'
    # psr_val[0]="STRUCT(%s)" % psr_val[1]
    #psr_val[0] = tuast.Struct(psr_val[1])


def p_attrval_constructor(psr_val):
    'attrval :  CONSTRUCTOR'
    # psr_val[0]="CONSTRUCTOR(%s)" % psr_val[1]
    #psr_val[0] = tuast.VConstructor(psr_val[1])


def p_attrval_op(psr_val):
    'attrval :  op_type'
    # psr_val[0]="OP(%s)" % psr_val[1]
    #psr_val[0] = tuast.Op(psr_val[1])


def p_attrval_pseudo_tmpl(psr_val):
    'attrval :  PSEUDO_TMPL PSEUDO_TMPL'
    # psr_val[0]="PSEUDO_TMPL2(%s,%s)" % (psr_val[1],psr_val[2])
    #psr_val[0] = tuast.PseudoTempl(psr_val[1], psr_val[2])

# def p_attrval_PSEUDO_TMPL(psr_val):
#     'attrval :  PSEUDO_TMPL'
# psr_val[0]="PSEUDO_TMPL(%s)" % psr_val[1]
#     psr_val[0]=tuast.PseudoTempl(psr_val[1])

def p_attrval_access(psr_val):
    'attrval :  ACC '
    # psr_val[0]="ACC(%s)" % psr_val[1]
    #psr_val[0] = tuast.AccVal(psr_val[1])


# def p_attrval_access_spec(psr_val):
#     'attrval :  ACC SPEC_VALU'
#     # psr_val[0]="ACC2(%s,%s)" % (psr_val[1],psr_val[2])
#     #psr_val[0] = tuast.AccSpec(psr_val[1], psr_val[2])
#     #print ("ACCESS_SPEC1:%s" % psr_val[0])


def p_attrval_link(psr_val):
    'attrval :  LINK'
    # "LINK(%s)" %
    #psr_val[0] = tuast.Link(psr_val[1])


def p_attrval_node(psr_val):
    'attrval : NODE'
    #m = matches(psr_val)
    #print "CHECK5 NODEREF %s" % psr_val.__dict__['slice'][1]
    #print "attrval_node %s" % psr_val.__dict__
    #psr_val[0] = tuast.NodeRef(psr_val[1])


def p_attrval_node_spec(psr_val):
    'attrval : NODE SPEC'
    # print "CHECK5 NODEREF %s" % psr_val[1]
    #psr_val[0]="NodeRef(%s)" % psr_val[1]
    #psr_val[0] = tuast.NodeRefSpec(psr_val[1], psr_val[2])


def p_attrval_file(psr_val):
    'attrval : BUILTIN_FILE'
    #m = matches(psr_val)
    # psr_val[0]= "FILE(%s)" % psr_val[1]
    #psr_val[0] = tuast.FileBuiltin()


def p_attrval_hxx_file(psr_val):
    'attrval : HXX_FILE'
    #m = matches(psr_val)
    # psr_val[0]= "FILE(%s)" % psr_val[1]
    #psr_val[0] = tuast.FilePos(psr_val[1])


def p_attrval_float(psr_val):
    'attrval : FLOAT'
    # psr_val[0]="FLOAT(%s)" % p
    #psr_val[0] = tuast.Float(psr_val[1])


def p_attrval_float_spec(psr_val):
    'attrval : FLOAT SPEC'
    # psr_val[0]="FLOAT(%s)" % p
    #psr_val[0] = tuast.FloatSpec(psr_val[1], psr_val[2])


def p_attrval_lang(psr_val):
    'attrval : LANG'
    # psr_val[0]="lang(%s)" % p
    #psr_val[0] = tuast.Lang(psr_val[1])

def p_node_addr_expr(psr_val):
    'node : NODE ADDR_EXPR OP0_ATTR NODE'
    #         1   2            3    4 
    #psr_val[0] = tuast.AddrExpr(psr_val[2], psr_val[1], psr_val[4])

def p_node_addr_expr2(psr_val):
    'node : NODE ADDR_EXPR type_attrs attr_list'
    #         1   2            3    4 
    #psr_val[0] = tuast.AddrExpr(psr_val[2], psr_val[1], psr_val[4])

# def p_node_addr_expr_type(psr_val):
#     'node : NODE ADDR_EXPR TYPE_ATTR NODE OP0_ATTR NODE '
#     #        1     2           3       4       5    6
#     #psr_val[0] = tuast.AddrExprTyped(psr_val[2], psr_val[1], psr_val[4], psr_val[6])

def p_error(psr_val):
    print "Check Syntax error in input! %s" % psr_val
    #print "Line Number: %s" % psr_val.lineno
    #print "Line Pos: %s" % psr_val.lexpos
    print("Parser %s" % parser)
    raise Exception('error %s' % psr_val)
    #pass


###-------------------------------------------------------------
### prec
# def p_attr_prec(psr_val):
#     'prec_attrtype : ATTR_PREC'
#     #psr_val[0] = attr_base(psr_val)
#     psr_val.lexer.begin('prec')

def p_attrs_prec(psr_val):
    #           1     2         3
    'attrs :  ATTR_PREC SOMEINT2'
    #psr_val[0] = std_attrs(psr_val)
    goto_initial(psr_val)  # begin the string group

###-------------------------------------------------------------

## algn
#def p_attr_algn(psr_val):
#    'attrtype_algn : ATTR_ALGN'
#    #psr_val[0] = attr_base(psr_val)
#    psr_val.lexer.begin('algn')
    
def p_attrs_algn(psr_val):
    #           1     2         3
    'attrs :  ATTR_ALGN SOMEINT'
    #psr_val[0] = std_attrs(psr_val)
    goto_initial(psr_val)  # begin the string group


# def p_attrs_type(psr_val):
#     'attrs :  type_attrs att'
#     # refactored to std function
#     #psr_val[0] = std_attrs2(psr_val)

# def p_attrs_type2(psr_val):
#     'attrs :  type_attrs'
#     # refactored to std function
#     #psr_val[0] = std_attrs2(psr_val)

def p_attrs_type6(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEINT2'
    goto_initial(psr_val)  # go back
    #print 'finished TYPE_ATTR NODE'
    #psr_val[0] = std_attrs(psr_val)

#####
# def p_attrs_type2(psr_val):
#     'type_attrs2 : '
#     print 'p_attrs_type2'
#     #goto_initial(psr_val)  # go back

# def p_attrs_type3(psr_val):
#     'type_attrs2 : INT SOMEHEX2'
#     print 'p_attrs_type3'
#     #goto_initial(psr_val)  # go back

# def p_attrs_type4(psr_val):
#     'type_attrs2 : '
#     print 'p_attrs_type4'
#     #goto_initial(psr_val)  # go back

def p_attrs_used(psr_val):
    #           type_     2     3
    'attrs : attrtype_used SOMEINT2'
    goto_initial(psr_val)  # go back
    #psr_val[0] = std_attrs(psr_val)

    


def p_attrs_type3(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEHEX2'
    goto_initial(psr_val)  # go back
    #print 'finished TYPE_ATTR NODE'
    #psr_val[0] = std_attrs(psr_val)

def p_attrs_type3b(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEHEX3'
    goto_initial(psr_val)  # go back
    #print 'finished TYPE_ATTR NODE'
    #psr_val[0] = std_attrs(psr_val)
    

# def p_attrs_type4(psr_val):
#     #           type_     2     3
#     'type_attrs : TYPE_ATTR NODE'
#     #print 'finished TYPE_ATTR NODE'
#     goto_initial(psr_val)  # go back
#     #psr_val[0] = std_attrs(psr_val)

def p_attrs_type5(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE' # len_attrs
    #print 'finished TYPE_ATTR NODE'
    #goto_initial(psr_val)  # go back
    #psr_val[0] = std_attrs(psr_val)

    
# def p_attrs_type6(psr_val):
#      'attrs :  type_attrs addr_attrs'
#      print 'p_attrs_type6'
#      goto_initial(psr_val)  # go back
     
# def p_attrs_type7(psr_val):
#      'attrs :  type_attrs attrs'
#      print 'p_attrs_type6'
#      goto_initial(psr_val)  # go back
     
# def p_attrs_type(psr_val):
#     #           type_     2     3
#     'type_attrs :  TYPE_ATTR NODE '
#     #psr_val[0] = std_attrs(psr_val)
#     goto_initial(psr_val)  # go back

#def p_attrs_type5(psr_val):
#    'attrs :  addr_attrs attrs'

            
# def p_attrs_type4(psr_val):
#     #           type_     2     3
#     'attrs :  TYPE_ATTR NODE type_attrs attrs '
#     #psr_val[0] = std_attrs(psr_val)

# def p_attrs_type1(psr_val):
#     #           type_     2     3
#     'attrs :  TYPE_ATTR NODE attrs'
#     #psr_val[0] = std_attrs(psr_val)
#     goto_initial(psr_val)  # go back
    
# Build the parser
parser = yacc.yacc()


#   result = parser.parse(s)

# Error rule for syntax errors



def debug(psr_val):
    print("final attrs %s" % dir(psr_val))
    print("doc %s" % psr_val.__doc__)
    # psr_val.__getitem__
    # psr_val.__getslice__
    # psr_val.__init__
    plen = psr_val.__len__()
    print("len:%s" % plen)
    # '__module__', '__setitem__', 'error',
    print(dir(psr_val.lexer))
    print("pos:%s" % psr_val.lexpos)
    # p4: 'action', 'errok', 'errorfunc', 'goto', 'parse', 'parsedebug', 'parseopt', 'parseopt_notrack', 'productions', 'restart', 'statestack', 'symstack']
#    print "p4:%s" % dir(psr_val.parser)
#    print "p4action:%s" % psr_val.parser.action
#    print "p4symstac:%s" % psr_val.parser.symstack
#    print "p4statestack:%s" % psr_val.parser.statestack
#    print "SLICE:%s" % psr_val.slice
#    print "p6:%s" % psr_val.stack
#    print "p2:%s" % psr_val.lineno(plen - 1)
    x = psr_val.lexspan(plen - 1)
#    print (x)
#    print "p1:%s,%s" % x
#    print "p3:%s,%s" % psr_val.linespan(plen - 1)


def report_stack(psr_val):
#    print (psr_val.parser.symstack)
  # print ( psr_val.parser.symstack[0].reverse())
    #stack = copy.copy(psr_val.parser.symstack)
    for x in psr_val.parser.symstack:
        if x.type == '$end':
            continue
        #print ("Token %s" % x)
  # print (dir(x))
        #print ("Value:%s" % x.value)
        #print ("Type:%s" % x.type)
        if 'lexpos' in dir(x):
            #print ("Lex %s" % x.lexpos)
            #print ("Line %s" % x.lineno)
            pass
        # print (type(x))
