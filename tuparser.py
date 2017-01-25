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

    print("DEBUG START")

    if psr_val.slice[1].value:
        print "Token Value:" + psr_val.slice[1].value
        print "Token Type:" + psr_val.slice[1].type

    for x in psr_val.slice:
        print("MATCHES: %s" % x)

#    print("MATCHES: %s" % dir(psr_val.lexer.token) )
#    print("MATCHES: %s" % psr_val.lexer.lexliterals )
#    print("MATCHES: %s" % psr_val.lexer.lexdata )
#    print("MATCHES: %s" % psr_val.lexer.lexmatch.string )
    for group in psr_val.lexer.lexmatch.groups() :
        c = c+1
        if group:
            print("DEBUG",c,group)
            ret.append(group)
    return ret

# the first rule is important
def p_node(psr_val):
    # the node declaration
    'node : NODE ntype attrs'
    #print "main NODE %s" % psr_val[1]
    #print "main TYPE %s" % psr_val[2]
    #print "main ATTRS %s" % psr_val[3]
    #print "main stack : %s" % psr_val.stack
    # psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])

def p_node_attrs(psr_val):
    'node : NODE ntype attrs addr_attrs'
    psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])
    
#def p_node_addr2(psr_val):
#     'attrs : addr_attrs'
#     psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])
    
# the first rule is important
def p_node_id(psr_val):
    # the identifier node declaration
    'node : NODE ntype_id str_attrs len_attrs addr_attrs'
    #print "main NODE %s" % psr_val[1]
    #print "main TYPE %s" % psr_val[2]
    #print "main ATTRS %s" % psr_val[3]
    #print "main stack : %s" % psr_val.stack
    # psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])
    psr_val.lexer.begin('INITIAL')  # begin the string group
    
def p_node_id2(psr_val):
    # no length
    'node : NODE ntype_id str_attrs len_attrs'
    psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])
    psr_val.lexer.begin('INITIAL')
        
def p_node_id3(psr_val):
    # no length
    'node : NODE ntype_id str_attrs'
    psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])
    psr_val.lexer.begin('INITIAL')

# # # empty_node
# def p_node_empty(psr_val):
#      # the node with no attrs
#      'node : NODE ntype'
#      #print "empty node %s %s " % (psr_val[2], psr_val[1])
#      psr_val[0] = tuast.Node(psr_val[2], psr_val[1], [])


def ntype_base(psr_val):
    #print "debug 1 %s" % psr_val
    ntype = psr_val[1]
    #print "debug node type %s" % ntype
    #print "debug 3 %s" % psr_val.stack
    #psr_val[0] = ntype
    return ntype

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
    node = tuast.Attr(type_str, psr_val[2])
    #result = append_list(psr_val[3], node)
    
    return psr_val

def std_attrs2(psr_val):

    print "val1: %s " %  psr_val[1]
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

def p_ntype_goto_expr(psr_val):
    'ntype : NTYPE_GOTO_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_label_expr(psr_val):
    'ntype : NTYPE_LABEL_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_switch_expr(psr_val):
    'ntype : NTYPE_SWITCH_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_truth_and_expr(psr_val):
    'ntype : NTYPE_TRUTH_AND_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_aggr_init_expr(psr_val):
    'ntype : NTYPE_AGGR_INIT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_modify_expr(psr_val):
    'ntype : NTYPE_MODIFY_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_alignof_expr(psr_val):
    'ntype : NTYPE_ALIGNOF_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_array_ref(psr_val):
    'ntype : NTYPE_ARRAY_REF'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_array_type(psr_val):
    'ntype : NTYPE_ARRAY_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_arrow_expr(psr_val):
    'ntype : NTYPE_ARROW_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_baselink(psr_val):
    'ntype : NTYPE_BASELINK'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_bind_expr(psr_val):
    'ntype : NTYPE_BIND_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_binfo(psr_val):
    'ntype : NTYPE_BINFO'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_bit_and_expr(psr_val):
    'ntype : NTYPE_BIT_AND_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_bit_ior_expr(psr_val):
    'ntype : NTYPE_BIT_IOR_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_bit_not_expr(psr_val):
    'ntype : NTYPE_BIT_NOT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_bit_xor_expr(psr_val):
    'ntype : NTYPE_BIT_XOR_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_boolean_type(psr_val):
    'ntype : NTYPE_BOOLEAN_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_bound_template_template_parm(psr_val):
    'ntype : NTYPE_BOUND_TEMPLATE_TEMPLATE_PARM'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_break_stmt(psr_val):
    'ntype : NTYPE_BREAK_STMT'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_call_expr(psr_val):
    'ntype : NTYPE_CALL_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_case_label_expr(psr_val):
    'ntype : NTYPE_CASE_LABEL_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_cast_expr(psr_val):
    'ntype : NTYPE_CAST_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_complex_type(psr_val):
    'ntype : NTYPE_COMPLEX_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_component_ref(psr_val):
    'ntype : NTYPE_COMPONENT_REF'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_compound_expr(psr_val):
    'ntype : NTYPE_COMPOUND_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_cond_expr(psr_val):
    'ntype : NTYPE_COND_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_const_cast_expr(psr_val):
    'ntype : NTYPE_CONST_CAST_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_const_decl(psr_val):
    'ntype : NTYPE_CONST_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_continue_stmt(psr_val):
    'ntype : NTYPE_CONTINUE_STMT'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_ctor_initializer(psr_val):
    'ntype : NTYPE_CTOR_INITIALIZER'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_decl_expr(psr_val):
    'ntype : NTYPE_DECL_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_decltype_type(psr_val):
    'ntype : NTYPE_DECLTYPE_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_dl_expr(psr_val):
    'ntype : NTYPE_DL_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_do_stmt(psr_val):
    'ntype : NTYPE_DO_STMT'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_dotstar_expr(psr_val):
    'ntype : NTYPE_DOTSTAR_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_dynamic_cast_expr(psr_val):
    'ntype : NTYPE_DYNAMIC_CAST_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_enumeral_type(psr_val):
    'ntype : NTYPE_ENUMERAL_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_eq_expr(psr_val):
    'ntype : NTYPE_EQ_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_error_mark(psr_val):
    'ntype : NTYPE_ERROR_MARK'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_expr_stmt(psr_val):
    'ntype : NTYPE_EXPR_STMT'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_field_decl(psr_val):
    'ntype : NTYPE_FIELD_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_for_stmt(psr_val):
    'ntype : NTYPE_FOR_STMT'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_function_decl(psr_val):
    'ntype : NTYPE_FUNCTION_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_function_type(psr_val):
    'ntype : NTYPE_FUNCTION_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_ge_expr(psr_val):
    'ntype : NTYPE_GE_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_gt_expr(psr_val):
    'ntype : NTYPE_GT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_handler(psr_val):
    'ntype : NTYPE_HANDLER'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_identifier_node(psr_val):
    'ntype_id : NTYPE_IDENTIFIER_NODE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_if_stmt(psr_val):
    'ntype : NTYPE_IF_STMT'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_indirect_ref(psr_val):
    'ntype : NTYPE_INDIRECT_REF'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_integer_cst(psr_val):
    'ntype : NTYPE_INTEGER_CST'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_integer_type(psr_val):
    'ntype : NTYPE_INTEGER_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_label_decl(psr_val):
    'ntype : NTYPE_LABEL_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_lang_type(psr_val):
    'ntype : NTYPE_LANG_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_le_expr(psr_val):
    'ntype : NTYPE_LE_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_lshift_expr(psr_val):
    'ntype : NTYPE_LSHIFT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_lt_expr(psr_val):
    'ntype : NTYPE_LT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_member_ref(psr_val):
    'ntype : NTYPE_MEMBER_REF'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_method_type(psr_val):
    'ntype : NTYPE_METHOD_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_minus_expr(psr_val):
    'ntype : NTYPE_MINUS_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_modop_expr(psr_val):
    'ntype : NTYPE_MODOP_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_mult_expr(psr_val):
    'ntype : NTYPE_MULT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_namespace_decl(psr_val):
    'ntype : NTYPE_NAMESPACE_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_ne_expr(psr_val):
    'ntype : NTYPE_NE_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_negate_expr(psr_val):
    'ntype : NTYPE_NEGATE_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_nop_expr(psr_val):
    'ntype : NTYPE_NOP_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_nw_expr(psr_val):
    'ntype : NTYPE_NW_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_offset_type(psr_val):
    'ntype : NTYPE_OFFSET_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_overload(psr_val):
    'ntype : NTYPE_OVERLOAD'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_parm_decl(psr_val):
    'ntype : NTYPE_PARM_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_plus_expr(psr_val):
    'ntype : NTYPE_PLUS_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_pointer_type(psr_val):
    'ntype : NTYPE_POINTER_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_pointer_bounds_type(psr_val):
    'ntype : NTYPE_POINTER_BOUNDS_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_postdecrement_expr(psr_val):
    'ntype : NTYPE_POSTDECREMENT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_postincrement_expr(psr_val):
    'ntype : NTYPE_POSTINCREMENT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_predecrement_expr(psr_val):
    'ntype : NTYPE_PREDECREMENT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_preincrement_expr(psr_val):
    'ntype : NTYPE_PREINCREMENT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_ptrmem_cst(psr_val):
    'ntype : NTYPE_PTRMEM_CST'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_real_cst(psr_val):
    'ntype : NTYPE_REAL_CST'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_real_type(psr_val):
    'ntype : NTYPE_REAL_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_record_type(psr_val):
    'ntype : NTYPE_RECORD_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_reference_type(psr_val):
    'ntype : NTYPE_REFERENCE_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_reinterpret_cast_expr(psr_val):
    'ntype : NTYPE_REINTERPRET_CAST_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_return_expr(psr_val):
    'ntype : NTYPE_RETURN_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_rshift_expr(psr_val):
    'ntype : NTYPE_RSHIFT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_scope_ref(psr_val):
    'ntype : NTYPE_SCOPE_REF'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_sizeof_expr(psr_val):
    'ntype : NTYPE_SIZEOF_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_statement_list(psr_val):
    'ntype : NTYPE_STATEMENT_LIST'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_static_cast_expr(psr_val):
    'ntype : NTYPE_STATIC_CAST_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_string_cst(psr_val):
    'ntype : NTYPE_STRING_CST'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_switch_stmt(psr_val):
    'ntype : NTYPE_SWITCH_STMT'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_tag_defn(psr_val):
    'ntype : NTYPE_TAG_DEFN'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_target_expr(psr_val):
    'ntype : NTYPE_TARGET_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_template_decl(psr_val):
    'ntype : NTYPE_TEMPLATE_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_template_id_expr(psr_val):
    'ntype : NTYPE_TEMPLATE_ID_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_template_parm_index(psr_val):
    'ntype : NTYPE_TEMPLATE_PARM_INDEX'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_template_template_parm(psr_val):
    'ntype : NTYPE_TEMPLATE_TEMPLATE_PARM'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_template_type_parm(psr_val):
    'ntype : NTYPE_TEMPLATE_TYPE_PARM'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_throw_expr(psr_val):
    'ntype : NTYPE_THROW_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_trait_expr(psr_val):
    'ntype : NTYPE_TRAIT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_translation_unit_decl(psr_val):
    'ntype : NTYPE_TRANSLATION_UNIT_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_tree_list(psr_val):
    'ntype : NTYPE_TREE_LIST'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_tree_vec(psr_val):
    'ntype : NTYPE_TREE_VEC'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_trunc_div_expr(psr_val):
    'ntype : NTYPE_TRUNC_DIV_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_trunc_mod_expr(psr_val):
    'ntype : NTYPE_TRUNC_MOD_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_truth_andif_expr(psr_val):
    'ntype : NTYPE_TRUTH_ANDIF_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_truth_not_expr(psr_val):
    'ntype : NTYPE_TRUTH_NOT_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_truth_orif_expr(psr_val):
    'ntype : NTYPE_TRUTH_ORIF_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_try_block(psr_val):
    'ntype : NTYPE_TRY_BLOCK'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_type_decl(psr_val):
    'ntype : NTYPE_TYPE_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_typeid_expr(psr_val):
    'ntype : NTYPE_TYPEID_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_typename_type(psr_val):
    'ntype : NTYPE_TYPENAME_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_typeof_type(psr_val):
    'ntype : NTYPE_TYPEOF_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_union_type(psr_val):
    'ntype : NTYPE_UNION_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_using_decl(psr_val):
    'ntype : NTYPE_USING_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_using_stmt(psr_val):
    'ntype : NTYPE_USING_STMT'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_var_decl(psr_val):
    'ntype : NTYPE_VAR_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_vector_type(psr_val):
    'ntype : NTYPE_VECTOR_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_void_type(psr_val):
    'ntype : NTYPE_VOID_TYPE'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_while_stmt(psr_val):
    'ntype : NTYPE_WHILE_STMT'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_pointer_plus_extr(psr_val):
    'ntype : NTYPE_POINTER_PLUS_EXPR'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_result_decl(psr_val):
    'ntype : NTYPE_RESULT_DECL'
    psr_val[0] = ntype_base(psr_val)

def p_ntype_convert_expr(psr_val):
    'ntype : NTYPE_CONVERT_EXPR'
    psr_val[0] = ntype_base(psr_val)


##
def p_attr_accs(psr_val):
    'attrtype : ATTR_ACCS'
    psr_val[0] = attr_base(psr_val)

def p_attr_labl(psr_val):
    'attrtype : ATTR_LABL'
    psr_val[0] = attr_base(psr_val)

def p_attr_vars(psr_val):
    'attrtype : ATTR_VARS'
    psr_val[0] = attr_base(psr_val)

# def p_attr_addr(psr_val):
#     'attrtype : ATTR_ADDR'
#     psr_val[0] = attr_base(psr_val)


def p_attr_alis(psr_val):
    'attrtype : ATTR_ALIS'
    psr_val[0] = attr_base(psr_val)

def p_attr_args(psr_val):
    'attrtype : ATTR_ARGS'
    psr_val[0] = attr_base(psr_val)

def p_attr_argt(psr_val):
    'attrtype : ATTR_ARGT'
    psr_val[0] = attr_base(psr_val)

def p_attr_base(psr_val):
    'attrtype : ATTR_BASE'
    psr_val[0] = attr_base(psr_val)

def p_attr_bases(psr_val):
    'attrtype : ATTR_BASES'
    psr_val[0] = attr_base(psr_val)

def p_attr_binf(psr_val):
    'attrtype : ATTR_BINF'
    psr_val[0] = attr_base(psr_val)

def p_attr_body(psr_val):
    'attrtype : ATTR_BODY'
    psr_val[0] = attr_base(psr_val)

def p_attr_bpos(psr_val):
    'attrtype : ATTR_BPOS'
    psr_val[0] = attr_base(psr_val)

def p_attr_chain(psr_val):
    'attrtype : ATTR_CHAIN'
    psr_val[0] = attr_base(psr_val)

def p_attr_chan(psr_val):
    'attrtype : ATTR_CHAN'
    psr_val[0] = attr_base(psr_val)

def p_attr_clas(psr_val):
    'attrtype : ATTR_CLAS'
    psr_val[0] = attr_base(psr_val)

def p_attr_clnp(psr_val):
    'attrtype : ATTR_CLNP'
    psr_val[0] = attr_base(psr_val)

def p_attr_cls(psr_val):
    'attrtype : ATTR_CLS'
    psr_val[0] = attr_base(psr_val)

def p_attr_cnst(psr_val):
    'attrtype : ATTR_CNST'
    psr_val[0] = attr_base(psr_val)

def p_attr_cond(psr_val):
    'attrtype : ATTR_COND'
    psr_val[0] = attr_base(psr_val)

def p_attr_crnt(psr_val):
    'attrtype : ATTR_CRNT'
    psr_val[0] = attr_base(psr_val)

def p_attr_csts(psr_val):
    'attrtype : ATTR_CSTS'
    psr_val[0] = attr_base(psr_val)

def p_attr_ctor(psr_val):
    'attrtype : ATTR_CTOR'
    psr_val[0] = attr_base(psr_val)

def p_attr_dcls(psr_val):
    'attrtype : ATTR_DCLS'
    psr_val[0] = attr_base(psr_val)

def p_attr_decl(psr_val):
    'attrtype : ATTR_DECL'
    psr_val[0] = attr_base(psr_val)

def p_attr_domn(psr_val):
    'attrtype : ATTR_DOMN'
    psr_val[0] = attr_base(psr_val)

def p_attr_else(psr_val):
    'attrtype : ATTR_ELSE'
    psr_val[0] = attr_base(psr_val)

def p_attr_elts(psr_val):
    'attrtype : ATTR_ELTS'
    psr_val[0] = attr_base(psr_val)

def p_attr_expr(psr_val):
    'attrtype : ATTR_EXPR'
    psr_val[0] = attr_base(psr_val)

def p_attr_flds(psr_val):
    'attrtype : ATTR_FLDS'
    psr_val[0] = attr_base(psr_val)

def p_attr_fn(psr_val):
    'attrtype : ATTR_FN'
    psr_val[0] = attr_base(psr_val)

def p_attr_fncs(psr_val):
    'attrtype : ATTR_FNCS'
    psr_val[0] = attr_base(psr_val)

def p_attr_hdlr(psr_val):
    'attrtype : ATTR_HDLR'
    psr_val[0] = attr_base(psr_val)

def p_attr_high(psr_val):
    'attrtype : ATTR_HIGH'
    psr_val[0] = attr_base(psr_val)

def p_attr_init(psr_val):
    'attrtype : ATTR_INIT'
    psr_val[0] = attr_base(psr_val)

def p_attr_inst(psr_val):
    'attrtype : ATTR_INST'
    psr_val[0] = attr_base(psr_val)

def p_attr_lang(psr_val):
    'attrtype : ATTR_LANG'
    psr_val[0] = attr_base(psr_val)

def p_attr_line(psr_val):
    'attrtype : ATTR_LINE'
    psr_val[0] = attr_base(psr_val)

def p_attr_link(psr_val):
    'attrtype : ATTR_LINK'
    psr_val[0] = attr_base(psr_val)

def p_attr_low(psr_val):
    'attrtype : ATTR_LOW'
    psr_val[0] = attr_base(psr_val)

def p_attr_max(psr_val):
    'attrtype : ATTR_MAX'
    psr_val[0] = attr_base(psr_val)

def p_attr_mbr(psr_val):
    'attrtype : ATTR_MBR'
    psr_val[0] = attr_base(psr_val)

def p_attr_min(psr_val):
    'attrtype : ATTR_MIN'
    psr_val[0] = attr_base(psr_val)

def p_attr_mngl(psr_val):
    'attrtype : ATTR_MNGL'
    psr_val[0] = attr_base(psr_val)

def p_attr_name(psr_val):
    'attrtype : ATTR_NAME'
    psr_val[0] = attr_base(psr_val)

def p_attr_nmsp(psr_val):
    'attrtype : ATTR_NMSP'
    psr_val[0] = attr_base(psr_val)

def p_attr_note(psr_val):
    'attrtype : ATTR_NOTE'
    psr_val[0] = attr_base(psr_val)

def p_attr_nst(psr_val):
    'attrtype : ATTR_NST'
    psr_val[0] = attr_base(psr_val)

def p_attr_orig(psr_val):
    'attrtype : ATTR_ORIG'
    psr_val[0] = attr_base(psr_val)

def p_attr_parm(psr_val):
    'attrtype : ATTR_PARM'
    psr_val[0] = attr_base(psr_val)


def p_attr_prms(psr_val):
    'attrtype : ATTR_PRMS'
    psr_val[0] = attr_base(psr_val)

def p_attr_ptd(psr_val):
    'attrtype : ATTR_PTD'
    psr_val[0] = attr_base(psr_val)

def p_attr_purp(psr_val):
    'attrtype : ATTR_PURP'
    psr_val[0] = attr_base(psr_val)

def p_attr_qual(psr_val):
    'attrtype : ATTR_QUAL'
    #print ("QUAL:")
    psr_val[0] = attr_base(psr_val)

def p_attr_refd(psr_val):
    'attrtype : ATTR_REFD'
    psr_val[0] = attr_base(psr_val)

def p_attr_retn(psr_val):
    'attrtype : ATTR_RETN'
    psr_val[0] = attr_base(psr_val)

def p_attr_rslt(psr_val):
    'attrtype : ATTR_RSLT'
    psr_val[0] = attr_base(psr_val)

def p_attr_scpe(psr_val):
    'attrtype : ATTR_SCPE'
    psr_val[0] = attr_base(psr_val)

def p_attr_sign(psr_val):
    'attrtype : ATTR_SIGN'
    psr_val[0] = attr_base(psr_val)

def p_attr_size(psr_val):
    'attrtype : ATTR_SIZE'
    psr_val[0] = attr_base(psr_val)

def p_attr_spcs(psr_val):
    'attrtype : ATTR_SPCS'
    psr_val[0] = attr_base(psr_val)

def p_attr_srcp(psr_val):
    'attrtype : ATTR_SRCP'
    psr_val[0] = attr_base(psr_val)

def p_attr_sts(psr_val):
    'attrtype : ATTR_STS'
    psr_val[0] = attr_base(psr_val)

def p_attr_tag(psr_val):
    'attrtype : ATTR_TAG'
    psr_val[0] = attr_base(psr_val)

def p_attr_then(psr_val):
    'attrtype : ATTR_THEN'
    psr_val[0] = attr_base(psr_val)

def p_attr_unql(psr_val):
    'attrtype : ATTR_UNQL'
    psr_val[0] = attr_base(psr_val)

def p_attr_used(psr_val):
    'attrtype_used : ATTR_USED'
    psr_val[0] = attr_base(psr_val)

def p_attr_val(psr_val):
    'attrtype : ATTR_VAL'
    psr_val[0] = attr_base(psr_val)

def p_attr_idx(psr_val):
    'attrtype : ATTR_IDX'
    psr_val[0] = attr_base(psr_val)

def p_attr_valu(psr_val):
    'attrtype : ATTR_VALU'
    psr_val[0] = attr_base(psr_val)

def p_attr_vfld(psr_val):
    'attrtype : ATTR_VFLD'
    psr_val[0] = attr_base(psr_val)

# special case for attribute OP 1 ... OP n
def p_attr_OP(psr_val):
    'attrtype : ATTR_OP'
    psr_val[0] = attr_base(psr_val)

# special case for attribute E 1 ... E n
def p_attr_En(psr_val):
    'attrtype : ATTR_En'
    psr_val[0] = attr_base(psr_val)


##########################################

def operator_base(psr_val):
    pass

def p_operator_add(psr_val):
    'op_type : OPERATOR_ADD'
    psr_val[0] = operator_base(psr_val)

def p_operator_and(psr_val):
    'op_type : OPERATOR_AND'
    psr_val[0] = operator_base(psr_val)

def p_operator_andassign(psr_val):
    'op_type : OPERATOR_ANDASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_addr(psr_val):
    'op_type : OPERATOR_ADDR'
    psr_val[0] = operator_base(psr_val)

def p_operator_assign(psr_val):
    'op_type : OPERATOR_ASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_call(psr_val):
    'op_type : OPERATOR_CALL'
    psr_val[0] = operator_base(psr_val)

def p_operator_compound(psr_val):
    'op_type : OPERATOR_COMPOUND'
    psr_val[0] = operator_base(psr_val)

def p_operator_delete(psr_val):
    'op_type : OPERATOR_DELETE'
    psr_val[0] = operator_base(psr_val)

def p_operator_deref(psr_val):
    'op_type : OPERATOR_DEREF'
    psr_val[0] = operator_base(psr_val)

def p_operator_div(psr_val):
    'op_type : OPERATOR_DIV'
    psr_val[0] = operator_base(psr_val)

def p_operator_divassign(psr_val):
    'op_type : OPERATOR_DIVASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_eq(psr_val):
    'op_type : OPERATOR_EQ'
    psr_val[0] = operator_base(psr_val)

def p_operator_ge(psr_val):
    'op_type : OPERATOR_GE'
    psr_val[0] = operator_base(psr_val)

def p_operator_gt(psr_val):
    'op_type : OPERATOR_GT'
    psr_val[0] = operator_base(psr_val)

def p_operator_le(psr_val):
    'op_type : OPERATOR_LE'
    psr_val[0] = operator_base(psr_val)

def p_operator_lnot(psr_val):
    'op_type : OPERATOR_LNOT'
    psr_val[0] = operator_base(psr_val)

def p_operator_lshift(psr_val):
    'op_type : OPERATOR_LSHIFT'
    psr_val[0] = operator_base(psr_val)

def p_operator_lshiftassign(psr_val):
    'op_type : OPERATOR_LSHIFTASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_lt(psr_val):
    'op_type : OPERATOR_LT'
    psr_val[0] = operator_base(psr_val)

def p_operator_minus(psr_val):
    'op_type : OPERATOR_MINUS'
    psr_val[0] = operator_base(psr_val)

def p_operator_minusassign(psr_val):
    'op_type : OPERATOR_MINUSASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_mult(psr_val):
    'op_type : OPERATOR_MULT'
    psr_val[0] = operator_base(psr_val)

def p_operator_multassign(psr_val):
    'op_type : OPERATOR_MULTASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_ne(psr_val):
    'op_type : OPERATOR_NE'
    psr_val[0] = operator_base(psr_val)

def p_operator_neg(psr_val):
    'op_type : OPERATOR_NEG'
    psr_val[0] = operator_base(psr_val)

def p_operator_new(psr_val):
    'op_type : OPERATOR_NEW'
    psr_val[0] = operator_base(psr_val)

def p_operator_or(psr_val):
    'op_type : OPERATOR_OR'
    psr_val[0] = operator_base(psr_val)

def p_operator_orassign(psr_val):
    'op_type : OPERATOR_ORASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_plus(psr_val):
    'op_type : OPERATOR_PLUS'
    psr_val[0] = operator_base(psr_val)

def p_operator_plusassign(psr_val):
    'op_type : OPERATOR_PLUSASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_postdec(psr_val):
    'op_type : OPERATOR_POSTDEC'
    psr_val[0] = operator_base(psr_val)

def p_operator_postinc(psr_val):
    'op_type : OPERATOR_POSTINC'
    psr_val[0] = operator_base(psr_val)

def p_operator_predec(psr_val):
    'op_type : OPERATOR_PREDEC'
    psr_val[0] = operator_base(psr_val)

def p_operator_preinc(psr_val):
    'op_type : OPERATOR_PREINC'
    psr_val[0] = operator_base(psr_val)

def p_operator_rshift(psr_val):
    'op_type : OPERATOR_RSHIFT'
    psr_val[0] = operator_base(psr_val)

def p_operator_vecdelete(psr_val):
    'op_type : OPERATOR_VECDELETE'
    psr_val[0] = operator_base(psr_val)

def p_operator_vecnew(psr_val):
    'op_type : OPERATOR_VECNEW'
    psr_val[0] = operator_base(psr_val)

def p_operator_xor(psr_val):
    'op_type : OPERATOR_XOR'
    psr_val[0] = operator_base(psr_val)

def p_operator_xorassign(psr_val):
    'op_type : OPERATOR_XORASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_not(psr_val):
    'op_type : OPERATOR_NOT'
    psr_val[0] = operator_base(psr_val)

def p_operator_pos(psr_val):
    'op_type : OPERATOR_POS'
    psr_val[0] = operator_base(psr_val)

def p_operator_ref(psr_val):
    'op_type : OPERATOR_REF'
    psr_val[0] = operator_base(psr_val)

def p_operator_rshiftassign(psr_val):
    'op_type : OPERATOR_RSHIFTASSIGN'
    psr_val[0] = operator_base(psr_val)

def p_operator_subs(psr_val):
    'op_type : OPERATOR_SUBS'
    psr_val[0] = operator_base(psr_val)


##########################################
def p_node_constructor(psr_val):
    #            1             2
    'node : NODE CONSTRUCTOR attrs'
    #print "CHECK LIST1 %s" % psr_val[3]
    # psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    psr_val[0] = tuast.NodeConstructor(psr_val[2], psr_val[1], psr_val[3])

def p_node_mem_ref(psr_val):
    'node : NODE NTYPE_MEM_REF attrs'
    psr_val[0] = tuast.NodeConstructor(psr_val[2], psr_val[1], psr_val[3])

def p_addr_attrs3(psr_val):
    'attrs :  addr_attrs'
    psr_val[0] = std_attrs2(psr_val)

    

def p_attrs(psr_val):
    'attrs :  attrtype attrval attrs'
    # refactored to std function

    psr_val[0] = std_attrs2(psr_val)


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
    'attrs :  ADDR_ATTR SOMEINT attrs'
    psr_val[0] = std_attrs(psr_val)

#


def p_attrs_op0(psr_val):
    #           1     2     3
    'attrs :  OP0_ATTR attrval attrs'
    psr_val[0] = std_attrs(psr_val)

def p_attrs_op1(psr_val):
    'attrs :  OP1_ATTR attrval attrs'
    psr_val[0] = std_attrs(psr_val)

def p_attrs_done(psr_val):
    'attrs : '
    # print "final attrs %s" % p
    #print (stack)
    psr_val[0] = [] # empty list

# def p_attrs_spec2(psr_val):
#     #            1          2        3        4
#     'attrs :  SPEC_ATTR SPEC_VALU SPEC_VALU attrs'
#     attr_list = psr_val[4]
#     node = tuast.SpecAttr(psr_val[1], psr_val[2], psr_val[3])
#     psr_val[0] = append_list(attr_list, node)
#     return psr_val[0]

# def p_attrs_spec3(psr_val):
#     #          1        2
#     'attrs :  SPEC_VALU attrs'
#     node = tuast.SpecAttr3(psr_val[1])
#     psr_val[0] = append_list(psr_val[2], node)
#     return psr_val[0]

# def p_attrs_spec1(psr_val):
#     #           1          2       3
#     'attrs :  SPEC_ATTR SPEC_VALU attrs'
#     node = tuast.SpecAttr2(psr_val[1], psr_val[2])
#     psr_val[0] = append_list(psr_val[3], node)
#     return psr_val[0]


def p_attrs_note(psr_val):
    'attrs :  NOTE'
    # psr_val[0]="NOTE(%s)" % p
    psr_val[0] = tuast.NoteAttr(psr_val[1])


def p_strlist(psr_val):
    'strlist : SOMESTRG strlist'
    m=psr_val[1]
    if m:
         print "string list '%s'" % m
         psr_val[0] = [tuast.String(m)]
    psr_val.lexer.begin('len')
    
def p_strlist2(psr_val):
     'strlist : SOMESTRG'
     m=psr_val[1]
     if m:
          print "matched string '%s'" % m
          psr_val[0] = [tuast.String(m)]
     psr_val.lexer.begin('len')
    
    
# def p_attrs_strg2(psr_val):
#     'str_attrs : STRG strlist'
#     m=psr_val[1]
#     if m:
#         print "single string '%s'" % m
#         psr_val[0] = [tuast.String(m)]
#     psr_val.lexer.begin('INITIAL')

def p_attrs_strg3(psr_val):
    'str_attrs : STRG strlist'
    m=psr_val[1]
    if m:
        print "simple string list '%s'" % m
        psr_val[0] = [tuast.String(m)]
    #psr_val.lexer.begin('len')

def p_attrs_addrs(psr_val):
    'addr_attrs : ADDR_ATTR HEXVAL'
    m=psr_val[1]
    if m:
        print "address is set to", m
        psr_val[0] = [tuast.String(m)]
    psr_val.lexer.begin('INITIAL')

def p_attrs_addrs2(psr_val):
    'addr_attrs : ADDR_ATTR SOMEHEX3'
    m=psr_val[1]
    if m:
        print "address is set to", m
        psr_val[0] = [tuast.String(m)]
    psr_val.lexer.begin('INITIAL')

def p_attrs_addrs3(psr_val):
    'addr_attrs : ADDR_ATTR SOMEHEX4'
    m=psr_val[1]
    if m:
        print "address is set to", m
        psr_val[0] = [tuast.String(m)]
    psr_val.lexer.begin('INITIAL')

def p_attrs_strglen(psr_val):
    'len_attrs : STRGLEN2 SOMEINT'
    #psr_val.lexer.begin('INITIAL')
    m=psr_val[2]
    if m:
        print "string length is :", m
        psr_val[0] = [tuast.String(m)]
    #psr_val.lexer.begin('INITIAL')

#def p_attrs_strglen2(psr_val):
#    'attrs : STRGLEN HEXVAL'
 #   psr_val.lexer.begin('INITIAL')
 #   m=psr_val[1]
 #   if m:
 #       print "string with length", m
#        psr_val[0] = [tuast.String(m)]

# def p_hexval(psr_val):
#     'hexval : STRGLEN HEXVAL'
#     m=psr_val[1]
#     if m:
#         print "strlen", m
#         psr_val[0] = [tuast.String(m)]

 
# def p_attrs_strg_addr(psr_val):
#     'adr_attrs : ADDR_ATTR HEXVAL'
#     m=psr_val[1]
#     if m:
#         print "addr length", m
#         psr_val[0] = [tuast.String(m)]



def p_attrs_member(psr_val):
    'attrs : MEMBER'
    # psr_val[0]="MEMBER(%s)" % psr_val[1]
    psr_val[0] = tuast.MemberAttr(psr_val[1])


def p_attrval_note(psr_val):
    'attrval :  NOTE'
    # psr_val[0]="NOTE(%s)" % p
    psr_val[0] = tuast.Note(psr_val[1])


def p_attrval_member(psr_val):
    'attrval : MEMBER'
    # psr_val[0]="MEMBER(%s)" % psr_val[1]
    psr_val[0] = tuast.Member(psr_val[1])


def p_attrval_qual(psr_val):
    'attrval :  QUAL'
    #print "QUAL(%s)" % psr_val[1]
    psr_val[0] = tuast.Qual(psr_val[1])


def p_attrval_artificial(psr_val):
    'attrval :  ARTIFICIAL'
    # psr_val[0]="ARTIFICAL(%s)" % psr_val[1]
    psr_val[0] = tuast.Artificial(psr_val[1])


def p_attrval_signed(psr_val):
    'attrval :  SIGNED'
    # psr_val[0]="SIGNED(%s)" % psr_val[1]
    psr_val[0] = tuast.Signed(psr_val[1])


def p_attrval_struct(psr_val):
    'attrval :  STRUCT'
    # psr_val[0]="STRUCT(%s)" % psr_val[1]
    psr_val[0] = tuast.Struct(psr_val[1])


def p_attrval_constructor(psr_val):
    'attrval :  CONSTRUCTOR'
    # psr_val[0]="CONSTRUCTOR(%s)" % psr_val[1]
    psr_val[0] = tuast.VConstructor(psr_val[1])


def p_attrval_op(psr_val):
    'attrval :  op_type'
    # psr_val[0]="OP(%s)" % psr_val[1]
    psr_val[0] = tuast.Op(psr_val[1])


def p_attrval_pseudo_tmpl(psr_val):
    'attrval :  PSEUDO_TMPL PSEUDO_TMPL'
    # psr_val[0]="PSEUDO_TMPL2(%s,%s)" % (psr_val[1],psr_val[2])
    psr_val[0] = tuast.PseudoTempl(psr_val[1], psr_val[2])

# def p_attrval_PSEUDO_TMPL(psr_val):
#     'attrval :  PSEUDO_TMPL'
# psr_val[0]="PSEUDO_TMPL(%s)" % psr_val[1]
#     psr_val[0]=tuast.PseudoTempl(psr_val[1])

def p_attrval_access(psr_val):
    'attrval :  ACC '
    # psr_val[0]="ACC(%s)" % psr_val[1]
    psr_val[0] = tuast.AccVal(psr_val[1])


# def p_attrval_access_spec(psr_val):
#     'attrval :  ACC SPEC_VALU'
#     # psr_val[0]="ACC2(%s,%s)" % (psr_val[1],psr_val[2])
#     psr_val[0] = tuast.AccSpec(psr_val[1], psr_val[2])
#     #print ("ACCESS_SPEC1:%s" % psr_val[0])


def p_attrval_link(psr_val):
    'attrval :  LINK'
    # "LINK(%s)" %
    psr_val[0] = tuast.Link(psr_val[1])


def p_attrval_node(psr_val):
    'attrval : NODE'
    #m = matches(psr_val)
    #print "CHECK5 NODEREF %s" % psr_val.__dict__['slice'][1]
    #print "attrval_node %s" % psr_val.__dict__
    psr_val[0] = tuast.NodeRef(psr_val[1])


def p_attrval_node_spec(psr_val):
    'attrval : NODE SPEC'
    # print "CHECK5 NODEREF %s" % psr_val[1]
    #psr_val[0]="NodeRef(%s)" % psr_val[1]
    psr_val[0] = tuast.NodeRefSpec(psr_val[1], psr_val[2])


def p_attrval_file(psr_val):
    'attrval : BUILTIN_FILE'
    #m = matches(psr_val)
    # psr_val[0]= "FILE(%s)" % psr_val[1]
    psr_val[0] = tuast.FileBuiltin()


def p_attrval_hxx_file(psr_val):
    'attrval : HXX_FILE'
    #m = matches(psr_val)
    # psr_val[0]= "FILE(%s)" % psr_val[1]
    psr_val[0] = tuast.FilePos(psr_val[1])


def p_attrval_float(psr_val):
    'attrval : FLOAT'
    # psr_val[0]="FLOAT(%s)" % p
    psr_val[0] = tuast.Float(psr_val[1])


def p_attrval_float_spec(psr_val):
    'attrval : FLOAT SPEC'
    # psr_val[0]="FLOAT(%s)" % p
    psr_val[0] = tuast.FloatSpec(psr_val[1], psr_val[2])


def p_attrval_lang(psr_val):
    'attrval : LANG'
    # psr_val[0]="lang(%s)" % p
    psr_val[0] = tuast.Lang(psr_val[1])

def p_node_addr_expr(psr_val):
    'node : NODE ADDR_EXPR OP0_ATTR NODE'
    #         1   2            3    4 
    psr_val[0] = tuast.AddrExpr(psr_val[2], psr_val[1], psr_val[4])

# def p_node_addr_expr_type(psr_val):
#     'node : NODE ADDR_EXPR TYPE_ATTR NODE OP0_ATTR NODE '
#     #        1     2           3       4       5    6
#     psr_val[0] = tuast.AddrExprTyped(psr_val[2], psr_val[1], psr_val[4], psr_val[6])

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
#     psr_val[0] = attr_base(psr_val)
#     psr_val.lexer.begin('prec')

def p_attrs_prec(psr_val):
    #           1     2         3
    'attrs :  ATTR_PREC SOMEINT attrs'
    psr_val[0] = std_attrs(psr_val)
    psr_val.lexer.begin('INITIAL')  # begin the string group

###-------------------------------------------------------------

## algn
#def p_attr_algn(psr_val):
#    'attrtype_algn : ATTR_ALGN'
#    psr_val[0] = attr_base(psr_val)
#    psr_val.lexer.begin('algn')
    
def p_attrs_algn(psr_val):
    #           1     2         3
    'attrs :  ATTR_ALGN SOMEINT attrs'
    psr_val[0] = std_attrs(psr_val)
    psr_val.lexer.begin('INITIAL')  # begin the string group


def p_attrs_type(psr_val):
    'attrs :  type_attrs attrs'
    # refactored to std function
    psr_val[0] = std_attrs2(psr_val)

def p_attrs_type2(psr_val):
    'attrs :  type_attrs'
    # refactored to std function
    psr_val[0] = std_attrs2(psr_val)

#####
# def p_attrs_type2(psr_val):
#     'type_attrs2 : '
#     print 'p_attrs_type2'
#     #psr_val.lexer.begin('INITIAL')  # go back

# def p_attrs_type3(psr_val):
#     'type_attrs2 : INT SOMEHEX2'
#     print 'p_attrs_type3'
#     #psr_val.lexer.begin('INITIAL')  # go back

# def p_attrs_type4(psr_val):
#     'type_attrs2 : '
#     print 'p_attrs_type4'
#     #psr_val.lexer.begin('INITIAL')  # go back

def p_attrs_used(psr_val):
    #           type_     2     3
    'attrs : attrtype_used SOMEINT2'
    psr_val.lexer.begin('INITIAL')  # go back
    print 'finished TYPE_ATTR NODE'
    psr_val[0] = std_attrs(psr_val)

    
def p_attrs_type2(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEINT2'
    psr_val.lexer.begin('INITIAL')  # go back
    print 'finished TYPE_ATTR NODE'
    psr_val[0] = std_attrs(psr_val)


def p_attrs_type3(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEHEX2'
    psr_val.lexer.begin('INITIAL')  # go back
    print 'finished TYPE_ATTR NODE'
    psr_val[0] = std_attrs(psr_val)

def p_attrs_type3b(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEHEX3'
    psr_val.lexer.begin('INITIAL')  # go back
    print 'finished TYPE_ATTR NODE'
    psr_val[0] = std_attrs(psr_val)
    

def p_attrs_type4(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE'
    print 'finished TYPE_ATTR NODE'
    psr_val.lexer.begin('INITIAL')  # go back
    psr_val[0] = std_attrs(psr_val)

# def p_attrs_type6(psr_val):
#      'attrs :  type_attrs addr_attrs'
#      print 'p_attrs_type6'
#      psr_val.lexer.begin('INITIAL')  # go back
     
# def p_attrs_type7(psr_val):
#      'attrs :  type_attrs attrs'
#      print 'p_attrs_type6'
#      psr_val.lexer.begin('INITIAL')  # go back
     
# def p_attrs_type(psr_val):
#     #           type_     2     3
#     'type_attrs :  TYPE_ATTR NODE '
#     psr_val[0] = std_attrs(psr_val)
#     psr_val.lexer.begin('INITIAL')  # go back

#def p_attrs_type5(psr_val):
#    'attrs :  addr_attrs attrs'

            
# def p_attrs_type4(psr_val):
#     #           type_     2     3
#     'attrs :  TYPE_ATTR NODE type_attrs attrs '
#     psr_val[0] = std_attrs(psr_val)

# def p_attrs_type1(psr_val):
#     #           type_     2     3
#     'attrs :  TYPE_ATTR NODE attrs'
#     psr_val[0] = std_attrs(psr_val)
#     psr_val.lexer.begin('INITIAL')  # go back



    
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
    print "p4symstac:%s" % psr_val.parser.symstack
    print "p4statestack:%s" % psr_val.parser.statestack
    print "SLICE:%s" % psr_val.slice
    print "p6:%s" % psr_val.stack
    print "p2:%s" % psr_val.lineno(plen - 1)
    x = psr_val.lexspan(plen - 1)
    print (x)
    print "p1:%s,%s" % x
    print "p3:%s,%s" % psr_val.linespan(plen - 1)


def report_stack(psr_val):
    print (psr_val.parser.symstack)
  # print ( psr_val.parser.symstack[0].reverse())
    #stack = copy.copy(psr_val.parser.symstack)
    for x in psr_val.parser.symstack:
        if x.type == '$end':
            continue
        print ("Token %s" % x)
  # print (dir(x))
        print ("Value:%s" % x.value)
        print ("Type:%s" % x.type)
        if 'lexpos' in dir(x):
            print ("Lex %s" % x.lexpos)
            print ("Line %s" % x.lineno)
        # print (type(x))
