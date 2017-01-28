node_types = [ 'ADDR_EXPR','CONSTRUCTOR','NTYPE_ARRAY_REF','NTYPE_ARRAY_TYPE','NTYPE_BIND_EXPR','NTYPE_BIT_AND_EXPR','NTYPE_BIT_FIELD_REF','NTYPE_BIT_IOR_EXPR','NTYPE_BIT_NOT_EXPR','NTYPE_BOOLEAN_TYPE','NTYPE_CALL_EXPR','NTYPE_CASE_LABEL_EXPR','NTYPE_COMPLEX_TYPE','NTYPE_COMPONENT_REF','NTYPE_COMPOUND_EXPR','NTYPE_COND_EXPR','NTYPE_CONST_DECL','NTYPE_CONVERT_EXPR','NTYPE_DECL_EXPR','NTYPE_ENUMERAL_TYPE','NTYPE_EQ_EXPR','NTYPE_FIELD_DECL','NTYPE_FUNCTION_DECL','NTYPE_FUNCTION_TYPE','NTYPE_GE_EXPR','NTYPE_GOTO_EXPR','NTYPE_GT_EXPR','NTYPE_IDENTIFIER_NODE','NTYPE_INDIRECT_REF','NTYPE_INTEGER_CST','NTYPE_INTEGER_TYPE','NTYPE_LABEL_DECL','NTYPE_LABEL_EXPR','NTYPE_LE_EXPR','NTYPE_LSHIFT_EXPR','NTYPE_LT_EXPR','NTYPE_MEM_REF','NTYPE_MINUS_EXPR','NTYPE_MODIFY_EXPR','NTYPE_MULT_EXPR','NTYPE_NE_EXPR','NTYPE_NEGATE_EXPR','NTYPE_NOP_EXPR','NTYPE_PARM_DECL','NTYPE_PLUS_EXPR','NTYPE_POINTER_BOUNDS_TYPE','NTYPE_POINTER_PLUS_EXPR','NTYPE_POINTER_TYPE','NTYPE_POSTINCREMENT_EXPR','NTYPE_PREDICT_EXPR','NTYPE_PREINCREMENT_EXPR','NTYPE_REAL_TYPE','NTYPE_RECORD_TYPE','NTYPE_REFERENCE_TYPE','NTYPE_RESULT_DECL','NTYPE_RETURN_EXPR','NTYPE_RSHIFT_EXPR','NTYPE_STATEMENT_LIST','NTYPE_STRING_CST','NTYPE_SWITCH_EXPR','NTYPE_TARGET_EXPR','NTYPE_TRANSLATION_UNIT_DECL','NTYPE_TREE_LIST','NTYPE_TRUNC_DIV_EXPR','NTYPE_TRUTH_AND_EXPR','NTYPE_TRUTH_ANDIF_EXPR','NTYPE_TRUTH_OR_EXPR','NTYPE_TRUTH_ORIF_EXPR','NTYPE_TYPE_DECL','NTYPE_UNION_TYPE','NTYPE_VAR_DECL','NTYPE_VECTOR_TYPE','NTYPE_VOID_TYPE', 'NTYPE_LANG_TYPE',
'NTYPE_CONTINUE_STMT',
'NTYPE_FOR_STMT',
'NTYPE_USING_STMT',
'NTYPE_TEMPLATE_DECL',
'NTYPE_TEMPLATE_TYPE_PARM',
'NTYPE_TREE_VEC',
'NTYPE_PTRMEM_CST',
'NTYPE_ARROW_EXPR',
'NTYPE_CONST_CAST_EXPR',
'NTYPE_BINFO',
'NTYPE_REAL_CST',
'NTYPE_REINTERPRET_CAST_EXPR',
'NTYPE_SCOPE_REF',
'NTYPE_NW_EXPR',
'NTYPE_ERROR_MARK',
'NTYPE_TYPEOF_TYPE',
'NTYPE_NAMESPACE_DECL',
'NTYPE_TRY_BLOCK',
'NTYPE_MEMBER_REF',
'NTYPE_TRAIT_EXPR',
'NTYPE_THROW_EXPR',
'NTYPE_DYNAMIC_CAST_EXPR',
'NTYPE_DECLTYPE_TYPE',
'NTYPE_TYPEID_EXPR',
'NTYPE_EXPR_STMT',
'NTYPE_PREDECREMENT_EXPR',
'NTYPE_CAST_EXPR',
'NTYPE_SIZEOF_EXPR',
'NTYPE_TRUTH_NOT_EXPR',
'NTYPE_TEMPLATE_TEMPLATE_PARM',
'NTYPE_DL_EXPR',
'NTYPE_POSTDECREMENT_EXPR',
'NTYPE_TEMPLATE_ID_EXPR',
'NTYPE_WHILE_STMT',
'NTYPE_OVERLOAD',
'NTYPE_TAG_DEFN',
'NTYPE_TYPENAME_TYPE',
'NTYPE_SWITCH_STMT',
'NTYPE_TEMPLATE_PARM_INDEX',
'NTYPE_BOUND_TEMPLATE_TEMPLATE_PARM',
'NTYPE_METHOD_TYPE',
'NTYPE_BREAK_STMT',
'NTYPE_MODOP_EXPR',
'NTYPE_BASELINK',
'NTYPE_STATIC_CAST_EXPR',
'NTYPE_TRUNC_MOD_EXPR',
'NTYPE_OFFSET_TYPE',
'NTYPE_ALIGNOF_EXPR',
'NTYPE_DO_STMT',
'NTYPE_CTOR_INITIALIZER',
'NTYPE_IF_STMT',
'NTYPE_BIT_XOR_EXPR',
'NTYPE_USING_DECL',
'NTYPE_AGGR_INIT_EXPR',
'NTYPE_HANDLER',
'NTYPE_DOTSTAR_EXPR',

]
for x in node_types:
    #print x
    print """def p_%s_node(psr_val):
    'node : NODE %s attr_list'""" % (x,x)

