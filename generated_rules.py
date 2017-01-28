import ply.yacc as yacc # Get the token map from the lexer.  This is required.

def p_NTYPE_UNION_TYPE_node(psr_val):
    'node : NODE NTYPE_UNION_TYPE  attr_list'
def p_NTYPE_FIELD_DECL_node(psr_val):
    'node : NODE NTYPE_FIELD_DECL  attr_list'
def p_NTYPE_VOID_TYPE_node(psr_val):
    'node : NODE NTYPE_VOID_TYPE  attr_list'
def p_NTYPE_COMPLEX_TYPE_node(psr_val):
    'node : NODE NTYPE_COMPLEX_TYPE  attr_list'
def p_NTYPE_POINTER_TYPE_node(psr_val):
    'node : NODE NTYPE_POINTER_TYPE  attr_list'
def p_NTYPE_LABEL_DECL_node(psr_val):
    'node : NODE NTYPE_LABEL_DECL  attr_list'
def p_NTYPE_REFERENCE_TYPE_node(psr_val):
    'node : NODE NTYPE_REFERENCE_TYPE  attr_list'
def p_CONSTRUCTOR_node(psr_val):
    'node : NODE CONSTRUCTOR  attr_list'
def p_NTYPE_FUNCTION_TYPE_node(psr_val):
    'node : NODE NTYPE_FUNCTION_TYPE  attr_list'
def p_NTYPE_VECTOR_TYPE_node(psr_val):
    'node : NODE NTYPE_VECTOR_TYPE  attr_list'
def p_NTYPE_CALL_EXPR_node(psr_val):
    'node : NODE NTYPE_CALL_EXPR  attr_list'
def p_NTYPE_FUNCTION_DECL_node(psr_val):
    'node : NODE NTYPE_FUNCTION_DECL  attr_list'
def p_NTYPE_GOTO_EXPR_node(psr_val):
    'node : NODE NTYPE_GOTO_EXPR  attr_list'
def p_NTYPE_STATEMENT_LIST_node(psr_val):
    'node : NODE NTYPE_STATEMENT_LIST  attr_list'
def p_NTYPE_SWITCH_EXPR_node(psr_val):
    'node : NODE NTYPE_SWITCH_EXPR  attr_list'
def p_NTYPE_PARM_DECL_node(psr_val):
    'node : NODE NTYPE_PARM_DECL  attr_list'
def p_NTYPE_POINTER_BOUNDS_TYPE_node(psr_val):
    'node : NODE NTYPE_POINTER_BOUNDS_TYPE  attr_list'
def p_NTYPE_LABEL_EXPR_node(psr_val):
    'node : NODE NTYPE_LABEL_EXPR  attr_list'
def p_NTYPE_CASE_LABEL_EXPR_node(psr_val):
    'node : NODE NTYPE_CASE_LABEL_EXPR  attr_list'
def p_NTYPE_ENUMERAL_TYPE_node(psr_val):
    'node : NODE NTYPE_ENUMERAL_TYPE  attr_list'
def p_NTYPE_RETURN_EXPR_node(psr_val):
    'node : NODE NTYPE_RETURN_EXPR  attr_list'
def p_NTYPE_TARGET_EXPR_node(psr_val):
    'node : NODE NTYPE_TARGET_EXPR  attr_list'
def p_NTYPE_BOOLEAN_TYPE_node(psr_val):
    'node : NODE NTYPE_BOOLEAN_TYPE  attr_list'
def p_NTYPE_CONST_DECL_node(psr_val):
    'node : NODE NTYPE_CONST_DECL  attr_list'
def p_NTYPE_REAL_TYPE_node(psr_val):
    'node : NODE NTYPE_REAL_TYPE  attr_list'
def p_NTYPE_BIND_EXPR_node(psr_val):
    'node : NODE NTYPE_BIND_EXPR  attr_list'
def p_NTYPE_STRING_CST_node(psr_val):
    'node : NODE NTYPE_STRING_CST  attr_list'
def p_NTYPE_TREE_LIST_node(psr_val):
    'node : NODE NTYPE_TREE_LIST  attr_list'
def p_NTYPE_INTEGER_TYPE_node(psr_val):
    'node : NODE NTYPE_INTEGER_TYPE  attr_list'
def p_NTYPE_ARRAY_TYPE_node(psr_val):
    'node : NODE NTYPE_ARRAY_TYPE  attr_list'
def p_NTYPE_RESULT_DECL_node(psr_val):
    'node : NODE NTYPE_RESULT_DECL  attr_list'
def p_NTYPE_TRANSLATION_UNIT_DECL_node(psr_val):
    'node : NODE NTYPE_TRANSLATION_UNIT_DECL  attr_list'
def p_NTYPE_RECORD_TYPE_node(psr_val):
    'node : NODE NTYPE_RECORD_TYPE  attr_list'
def p_NTYPE_POSTINCREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_POSTINCREMENT_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_COMPOUND_EXPR_node(psr_val):
    'node : NODE NTYPE_COMPOUND_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_MODIFY_EXPR_node(psr_val):
    'node : NODE NTYPE_MODIFY_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_MULT_EXPR_node(psr_val):
    'node : NODE NTYPE_MULT_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_NE_EXPR_node(psr_val):
    'node : NODE NTYPE_NE_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_GE_EXPR_node(psr_val):
    'node : NODE NTYPE_GE_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_TRUNC_DIV_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUNC_DIV_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_GT_EXPR_node(psr_val):
    'node : NODE NTYPE_GT_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_PREINCREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_PREINCREMENT_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_ARRAY_REF_node(psr_val):
    'node : NODE NTYPE_ARRAY_REF TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_BIT_AND_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_AND_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_MINUS_EXPR_node(psr_val):
    'node : NODE NTYPE_MINUS_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_RSHIFT_EXPR_node(psr_val):
    'node : NODE NTYPE_RSHIFT_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_POINTER_PLUS_EXPR_node(psr_val):
    'node : NODE NTYPE_POINTER_PLUS_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_PLUS_EXPR_node(psr_val):
    'node : NODE NTYPE_PLUS_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_TRUTH_ORIF_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_ORIF_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_EQ_EXPR_node(psr_val):
    'node : NODE NTYPE_EQ_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_TRUTH_ANDIF_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_ANDIF_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_BIT_IOR_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_IOR_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_LSHIFT_EXPR_node(psr_val):
    'node : NODE NTYPE_LSHIFT_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_COND_EXPR_node(psr_val):
    'node : NODE NTYPE_COND_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_COMPONENT_REF_node(psr_val):
    'node : NODE NTYPE_COMPONENT_REF TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_LT_EXPR_node(psr_val):
    'node : NODE NTYPE_LT_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_LE_EXPR_node(psr_val):
    'node : NODE NTYPE_LE_EXPR TYPE_ATTR OP0_ATTR OP1_ATTR attr_list'
def p_NTYPE_NEGATE_EXPR_node(psr_val):
    'node : NODE NTYPE_NEGATE_EXPR TYPE_ATTR OP0_ATTR attr_list'
def p_NTYPE_BIT_NOT_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_NOT_EXPR TYPE_ATTR OP0_ATTR attr_list'
def p_NTYPE_INDIRECT_REF_node(psr_val):
    'node : NODE NTYPE_INDIRECT_REF TYPE_ATTR OP0_ATTR attr_list'
def p_NTYPE_BIT_FIELD_REF_node(psr_val):
    'node : NODE NTYPE_BIT_FIELD_REF TYPE_ATTR OP0_ATTR attr_list'
def p_ADDR_EXPR_node(psr_val):
    'node : NODE ADDR_EXPR TYPE_ATTR OP0_ATTR attr_list'
def p_NTYPE_NOP_EXPR_node(psr_val):
    'node : NODE NTYPE_NOP_EXPR TYPE_ATTR OP0_ATTR attr_list'
def p_NTYPE_CONVERT_EXPR_node(psr_val):
    'node : NODE NTYPE_CONVERT_EXPR TYPE_ATTR OP0_ATTR attr_list'
def p_NTYPE_VAR_DECL_node(psr_val):
    'node : NODE NTYPE_VAR_DECL SPEC_ATTR attr_list'
def p_NTYPE_TYPE_DECL_node(psr_val):
    'node : NODE NTYPE_TYPE_DECL TYPE_ATTR attr_list'
def p_NTYPE_PREDICT_EXPR_node(psr_val):
    'node : NODE NTYPE_PREDICT_EXPR TYPE_ATTR attr_list'
def p_NTYPE_TRUTH_AND_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_AND_EXPR TYPE_ATTR attr_list'
def p_NTYPE_INTEGER_CST_node(psr_val):
    'node : NODE NTYPE_INTEGER_CST TYPE_ATTR attr_list'
def p_NTYPE_DECL_EXPR_node(psr_val):
    'node : NODE NTYPE_DECL_EXPR TYPE_ATTR attr_list'
def p_NTYPE_TRUTH_OR_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_OR_EXPR TYPE_ATTR attr_list'
def p_NTYPE_MEM_REF_node(psr_val):
    'node : NODE NTYPE_MEM_REF TYPE_ATTR attr_list'
