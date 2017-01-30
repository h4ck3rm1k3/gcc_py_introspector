from attributes import parser_node_rule


@parser_node_rule
def p_ADDR_EXPR_node(psr_val):
    'node : NODE ADDR_EXPR attr_list'
@parser_node_rule
def p_CONSTRUCTOR_node(psr_val):
    'node : NODE CONSTRUCTOR attr_list'
@parser_node_rule
def p_NTYPE_ARRAY_REF_node(psr_val):
    'node : NODE NTYPE_ARRAY_REF attr_list'
@parser_node_rule
def p_NTYPE_ARRAY_TYPE_node(psr_val):
    'node : NODE NTYPE_ARRAY_TYPE attr_list'
@parser_node_rule
def p_NTYPE_BIND_EXPR_node(psr_val):
    'node : NODE NTYPE_BIND_EXPR attr_list'
@parser_node_rule
def p_NTYPE_BIT_AND_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_AND_EXPR attr_list'
@parser_node_rule
def p_NTYPE_BIT_FIELD_REF_node(psr_val):
    'node : NODE NTYPE_BIT_FIELD_REF attr_list'
@parser_node_rule
def p_NTYPE_BIT_IOR_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_IOR_EXPR attr_list'
@parser_node_rule
def p_NTYPE_BIT_NOT_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_NOT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_BOOLEAN_TYPE_node(psr_val):
    'node : NODE NTYPE_BOOLEAN_TYPE attr_list'
@parser_node_rule
def p_NTYPE_CALL_EXPR_node(psr_val):
    'node : NODE NTYPE_CALL_EXPR attr_list'
@parser_node_rule
def p_NTYPE_CASE_LABEL_EXPR_node(psr_val):
    'node : NODE NTYPE_CASE_LABEL_EXPR attr_list'
@parser_node_rule
def p_NTYPE_COMPLEX_TYPE_node(psr_val):
    'node : NODE NTYPE_COMPLEX_TYPE attr_list'
@parser_node_rule
def p_NTYPE_COMPONENT_REF_node(psr_val):
    'node : NODE NTYPE_COMPONENT_REF attr_list'
@parser_node_rule
def p_NTYPE_COMPOUND_EXPR_node(psr_val):
    'node : NODE NTYPE_COMPOUND_EXPR attr_list'
@parser_node_rule
def p_NTYPE_COND_EXPR_node(psr_val):
    'node : NODE NTYPE_COND_EXPR attr_list'
@parser_node_rule
def p_NTYPE_CONST_DECL_node(psr_val):
    'node : NODE NTYPE_CONST_DECL attr_list'
@parser_node_rule
def p_NTYPE_CONVERT_EXPR_node(psr_val):
    'node : NODE NTYPE_CONVERT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_DECL_EXPR_node(psr_val):
    'node : NODE NTYPE_DECL_EXPR attr_list'
@parser_node_rule
def p_NTYPE_ENUMERAL_TYPE_node(psr_val):
    'node : NODE NTYPE_ENUMERAL_TYPE attr_list'
@parser_node_rule
def p_NTYPE_EQ_EXPR_node(psr_val):
    'node : NODE NTYPE_EQ_EXPR attr_list'
@parser_node_rule
def p_NTYPE_FIELD_DECL_node(psr_val):
    'node : NODE NTYPE_FIELD_DECL attr_list'

@parser_node_rule
def p_NTYPE_FUNCTION_DECL_node(psr_val):
    'node : NODE NTYPE_FUNCTION_DECL attr_list'
@parser_node_rule
def p_NTYPE_FUNCTION_TYPE_node(psr_val):
    'node : NODE NTYPE_FUNCTION_TYPE attr_list'
@parser_node_rule
def p_NTYPE_GE_EXPR_node(psr_val):
    'node : NODE NTYPE_GE_EXPR attr_list'
@parser_node_rule
def p_NTYPE_GOTO_EXPR_node(psr_val):
    'node : NODE NTYPE_GOTO_EXPR attr_list'
@parser_node_rule
def p_NTYPE_GT_EXPR_node(psr_val):
    'node : NODE NTYPE_GT_EXPR attr_list'

@parser_node_rule
def p_NTYPE_INDIRECT_REF_node(psr_val):
    'node : NODE NTYPE_INDIRECT_REF attr_list'
@parser_node_rule
def p_NTYPE_INTEGER_CST_node(psr_val):
    'node : NODE NTYPE_INTEGER_CST attr_list'
@parser_node_rule
def p_NTYPE_INTEGER_TYPE_node(psr_val):
    'node : NODE NTYPE_INTEGER_TYPE attr_list'
@parser_node_rule
def p_NTYPE_LABEL_DECL_node(psr_val):
    'node : NODE NTYPE_LABEL_DECL attr_list'
@parser_node_rule
def p_NTYPE_LABEL_EXPR_node(psr_val):
    'node : NODE NTYPE_LABEL_EXPR attr_list'
@parser_node_rule
def p_NTYPE_LE_EXPR_node(psr_val):
    'node : NODE NTYPE_LE_EXPR attr_list'
@parser_node_rule
def p_NTYPE_LSHIFT_EXPR_node(psr_val):
    'node : NODE NTYPE_LSHIFT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_LT_EXPR_node(psr_val):
    'node : NODE NTYPE_LT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_MEM_REF_node(psr_val):
    'node : NODE NTYPE_MEM_REF attr_list'
@parser_node_rule
def p_NTYPE_MINUS_EXPR_node(psr_val):
    'node : NODE NTYPE_MINUS_EXPR attr_list'
@parser_node_rule
def p_NTYPE_MODIFY_EXPR_node(psr_val):
    'node : NODE NTYPE_MODIFY_EXPR attr_list'
@parser_node_rule
def p_NTYPE_MULT_EXPR_node(psr_val):
    'node : NODE NTYPE_MULT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_NE_EXPR_node(psr_val):
    'node : NODE NTYPE_NE_EXPR attr_list'
@parser_node_rule
def p_NTYPE_NEGATE_EXPR_node(psr_val):
    'node : NODE NTYPE_NEGATE_EXPR attr_list'
@parser_node_rule
def p_NTYPE_NOP_EXPR_node(psr_val):
    'node : NODE NTYPE_NOP_EXPR attr_list'
@parser_node_rule
def p_NTYPE_PARM_DECL_node(psr_val):
    'node : NODE NTYPE_PARM_DECL attr_list'
@parser_node_rule
def p_NTYPE_PLUS_EXPR_node(psr_val):
    'node : NODE NTYPE_PLUS_EXPR attr_list'
@parser_node_rule
def p_NTYPE_POINTER_BOUNDS_TYPE_node(psr_val):
    'node : NODE NTYPE_POINTER_BOUNDS_TYPE attr_list'
@parser_node_rule
def p_NTYPE_POINTER_PLUS_EXPR_node(psr_val):
    'node : NODE NTYPE_POINTER_PLUS_EXPR attr_list'
@parser_node_rule
def p_NTYPE_POINTER_TYPE_node(psr_val):
    'node : NODE NTYPE_POINTER_TYPE attr_list'
@parser_node_rule
def p_NTYPE_POSTINCREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_POSTINCREMENT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_PREDICT_EXPR_node(psr_val):
    'node : NODE NTYPE_PREDICT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_PREINCREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_PREINCREMENT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_REAL_TYPE_node(psr_val):
    'node : NODE NTYPE_REAL_TYPE attr_list'
@parser_node_rule
def p_NTYPE_RECORD_TYPE_node(psr_val):
    'node : NODE NTYPE_RECORD_TYPE attr_list'
@parser_node_rule
def p_NTYPE_REFERENCE_TYPE_node(psr_val):
    'node : NODE NTYPE_REFERENCE_TYPE attr_list'
@parser_node_rule
def p_NTYPE_RESULT_DECL_node(psr_val):
    'node : NODE NTYPE_RESULT_DECL attr_list'
@parser_node_rule
def p_NTYPE_RETURN_EXPR_node(psr_val):
    'node : NODE NTYPE_RETURN_EXPR attr_list'
@parser_node_rule
def p_NTYPE_RSHIFT_EXPR_node(psr_val):
    'node : NODE NTYPE_RSHIFT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_STATEMENT_LIST_node(psr_val):
    'node : NODE NTYPE_STATEMENT_LIST attr_list'
@parser_node_rule
def p_NTYPE_STRING_CST_node(psr_val):
    'node : NODE NTYPE_STRING_CST attr_list'
@parser_node_rule
def p_NTYPE_SWITCH_EXPR_node(psr_val):
    'node : NODE NTYPE_SWITCH_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TARGET_EXPR_node(psr_val):
    'node : NODE NTYPE_TARGET_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TRANSLATION_UNIT_DECL_node(psr_val):
    'node : NODE NTYPE_TRANSLATION_UNIT_DECL attr_list'
@parser_node_rule
def p_NTYPE_TREE_LIST_node(psr_val):
    'node : NODE NTYPE_TREE_LIST attr_list'
@parser_node_rule
def p_NTYPE_TRUNC_DIV_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUNC_DIV_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TRUTH_AND_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_AND_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TRUTH_ANDIF_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_ANDIF_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TRUTH_OR_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_OR_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TRUTH_ORIF_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_ORIF_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TYPE_DECL_node(psr_val):
    'node : NODE NTYPE_TYPE_DECL attr_list'
@parser_node_rule
def p_NTYPE_UNION_TYPE_node(psr_val):
    'node : NODE NTYPE_UNION_TYPE attr_list'
@parser_node_rule
def p_NTYPE_VAR_DECL_node(psr_val):
    'node : NODE NTYPE_VAR_DECL attr_list'
@parser_node_rule
def p_NTYPE_VECTOR_TYPE_node(psr_val):
    'node : NODE NTYPE_VECTOR_TYPE attr_list'
@parser_node_rule
def p_NTYPE_VOID_TYPE_node(psr_val):
    'node : NODE NTYPE_VOID_TYPE attr_list'
@parser_node_rule
def p_NTYPE_LANG_TYPE_node(psr_val):
    'node : NODE NTYPE_LANG_TYPE attr_list'
@parser_node_rule
def p_NTYPE_CONTINUE_STMT_node(psr_val):
    'node : NODE NTYPE_CONTINUE_STMT attr_list'
@parser_node_rule
def p_NTYPE_FOR_STMT_node(psr_val):
    'node : NODE NTYPE_FOR_STMT attr_list'
@parser_node_rule
def p_NTYPE_USING_STMT_node(psr_val):
    'node : NODE NTYPE_USING_STMT attr_list'
@parser_node_rule
def p_NTYPE_TEMPLATE_DECL_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_DECL attr_list'
@parser_node_rule
def p_NTYPE_TEMPLATE_TYPE_PARM_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_TYPE_PARM attr_list'
@parser_node_rule
def p_NTYPE_TREE_VEC_node(psr_val):
    'node : NODE NTYPE_TREE_VEC attr_list'
@parser_node_rule
def p_NTYPE_PTRMEM_CST_node(psr_val):
    'node : NODE NTYPE_PTRMEM_CST attr_list'
@parser_node_rule
def p_NTYPE_ARROW_EXPR_node(psr_val):
    'node : NODE NTYPE_ARROW_EXPR attr_list'
@parser_node_rule
def p_NTYPE_CONST_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_CONST_CAST_EXPR attr_list'
@parser_node_rule
def p_NTYPE_BINFO_node(psr_val):
    'node : NODE NTYPE_BINFO attr_list'
@parser_node_rule
def p_NTYPE_REAL_CST_node(psr_val):
    'node : NODE NTYPE_REAL_CST attr_list'
@parser_node_rule
def p_NTYPE_REINTERPRET_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_REINTERPRET_CAST_EXPR attr_list'
@parser_node_rule
def p_NTYPE_SCOPE_REF_node(psr_val):
    'node : NODE NTYPE_SCOPE_REF attr_list'
@parser_node_rule
def p_NTYPE_NW_EXPR_node(psr_val):
    'node : NODE NTYPE_NW_EXPR attr_list'
@parser_node_rule
def p_NTYPE_ERROR_MARK_node(psr_val):
    'node : NODE NTYPE_ERROR_MARK attr_list'
@parser_node_rule
def p_NTYPE_TYPEOF_TYPE_node(psr_val):
    'node : NODE NTYPE_TYPEOF_TYPE attr_list'
@parser_node_rule
def p_NTYPE_NAMESPACE_DECL_node(psr_val):
    'node : NODE NTYPE_NAMESPACE_DECL attr_list'
@parser_node_rule
def p_NTYPE_TRY_BLOCK_node(psr_val):
    'node : NODE NTYPE_TRY_BLOCK attr_list'
@parser_node_rule
def p_NTYPE_MEMBER_REF_node(psr_val):
    'node : NODE NTYPE_MEMBER_REF attr_list'
@parser_node_rule
def p_NTYPE_TRAIT_EXPR_node(psr_val):
    'node : NODE NTYPE_TRAIT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_THROW_EXPR_node(psr_val):
    'node : NODE NTYPE_THROW_EXPR attr_list'
@parser_node_rule
def p_NTYPE_DYNAMIC_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_DYNAMIC_CAST_EXPR attr_list'
@parser_node_rule
def p_NTYPE_DECLTYPE_TYPE_node(psr_val):
    'node : NODE NTYPE_DECLTYPE_TYPE attr_list'
@parser_node_rule
def p_NTYPE_TYPEID_EXPR_node(psr_val):
    'node : NODE NTYPE_TYPEID_EXPR attr_list'
@parser_node_rule
def p_NTYPE_EXPR_STMT_node(psr_val):
    'node : NODE NTYPE_EXPR_STMT attr_list'
@parser_node_rule
def p_NTYPE_PREDECREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_PREDECREMENT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_CAST_EXPR attr_list'
@parser_node_rule
def p_NTYPE_SIZEOF_EXPR_node(psr_val):
    'node : NODE NTYPE_SIZEOF_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TRUTH_NOT_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUTH_NOT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TEMPLATE_TEMPLATE_PARM_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_TEMPLATE_PARM attr_list'
@parser_node_rule
def p_NTYPE_DL_EXPR_node(psr_val):
    'node : NODE NTYPE_DL_EXPR attr_list'
@parser_node_rule
def p_NTYPE_POSTDECREMENT_EXPR_node(psr_val):
    'node : NODE NTYPE_POSTDECREMENT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TEMPLATE_ID_EXPR_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_ID_EXPR attr_list'
@parser_node_rule
def p_NTYPE_WHILE_STMT_node(psr_val):
    'node : NODE NTYPE_WHILE_STMT attr_list'
@parser_node_rule
def p_NTYPE_OVERLOAD_node(psr_val):
    'node : NODE NTYPE_OVERLOAD attr_list'
@parser_node_rule
def p_NTYPE_TAG_DEFN_node(psr_val):
    'node : NODE NTYPE_TAG_DEFN attr_list'
@parser_node_rule
def p_NTYPE_TYPENAME_TYPE_node(psr_val):
    'node : NODE NTYPE_TYPENAME_TYPE attr_list'
@parser_node_rule
def p_NTYPE_SWITCH_STMT_node(psr_val):
    'node : NODE NTYPE_SWITCH_STMT attr_list'
@parser_node_rule
def p_NTYPE_TEMPLATE_PARM_INDEX_node(psr_val):
    'node : NODE NTYPE_TEMPLATE_PARM_INDEX attr_list'
@parser_node_rule
def p_NTYPE_BOUND_TEMPLATE_TEMPLATE_PARM_node(psr_val):
    'node : NODE NTYPE_BOUND_TEMPLATE_TEMPLATE_PARM attr_list'
@parser_node_rule
def p_NTYPE_METHOD_TYPE_node(psr_val):
    'node : NODE NTYPE_METHOD_TYPE attr_list'
@parser_node_rule
def p_NTYPE_BREAK_STMT_node(psr_val):
    'node : NODE NTYPE_BREAK_STMT attr_list'
@parser_node_rule
def p_NTYPE_MODOP_EXPR_node(psr_val):
    'node : NODE NTYPE_MODOP_EXPR attr_list'
@parser_node_rule
def p_NTYPE_BASELINK_node(psr_val):
    'node : NODE NTYPE_BASELINK attr_list'
@parser_node_rule
def p_NTYPE_STATIC_CAST_EXPR_node(psr_val):
    'node : NODE NTYPE_STATIC_CAST_EXPR attr_list'
@parser_node_rule
def p_NTYPE_TRUNC_MOD_EXPR_node(psr_val):
    'node : NODE NTYPE_TRUNC_MOD_EXPR attr_list'
@parser_node_rule
def p_NTYPE_OFFSET_TYPE_node(psr_val):
    'node : NODE NTYPE_OFFSET_TYPE attr_list'
@parser_node_rule
def p_NTYPE_ALIGNOF_EXPR_node(psr_val):
    'node : NODE NTYPE_ALIGNOF_EXPR attr_list'
@parser_node_rule
def p_NTYPE_DO_STMT_node(psr_val):
    'node : NODE NTYPE_DO_STMT attr_list'
@parser_node_rule
def p_NTYPE_CTOR_INITIALIZER_node(psr_val):
    'node : NODE NTYPE_CTOR_INITIALIZER attr_list'
@parser_node_rule
def p_NTYPE_IF_STMT_node(psr_val):
    'node : NODE NTYPE_IF_STMT attr_list'
@parser_node_rule
def p_NTYPE_BIT_XOR_EXPR_node(psr_val):
    'node : NODE NTYPE_BIT_XOR_EXPR attr_list'
@parser_node_rule
def p_NTYPE_USING_DECL_node(psr_val):
    'node : NODE NTYPE_USING_DECL attr_list'
@parser_node_rule
def p_NTYPE_AGGR_INIT_EXPR_node(psr_val):
    'node : NODE NTYPE_AGGR_INIT_EXPR attr_list'
@parser_node_rule
def p_NTYPE_HANDLER_node(psr_val):
    'node : NODE NTYPE_HANDLER attr_list'
@parser_node_rule
def p_NTYPE_DOTSTAR_EXPR_node(psr_val):
    'node : NODE NTYPE_DOTSTAR_EXPR attr_list'


@parser_node_rule
def p_NTYPE_IDENTIFIER_NODE_node(psr_val):
    'node : NODE NTYPE_IDENTIFIER_NODE attr_list'

@parser_node_rule
def p_NTYPE_SAVE_EXPR_node(psr_val):
    'node : NODE NTYPE_SAVE_EXPR attr_list'
@parser_node_rule
def p_NTYPE_ASM_EXPR_node(psr_val):
    'node : NODE NTYPE_ASM_EXPR attr_list'
