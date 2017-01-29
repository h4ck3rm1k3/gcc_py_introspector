'''
reader
'''
import pprint
import ply.yacc as yacc # Get the token map from the lexer.  This is required.
from tu import tokens
import tuast  # import Link
from utils import goto_initial, create_list, merge_list

# the first rule is important
from attributes import parser_rule,parser_node_rule

# this first rule is synthetic and matches any nodes
@parser_rule
def p_any_node(psr_val):
    # the node declaration
    'anynode : node '
    psr_val[0]=psr_val[1]

@parser_node_rule
def p_NTYPE_IDENTIFIER_NODE_node(psr_val):
    'node : NODE NTYPE_IDENTIFIER_NODE attr_list'
    


@parser_rule
def p_node_id(psr_val):
    # the identifier node declaration
    'node : NODE HEXVAL attr_list' # len_attrs
    psr_val[0] = { 'node' : psr_val[1],
                   'hexval' :psr_val[2],
                   'attr_list' : psr_val[3]
    }

    
    goto_initial(psr_val)  # begin the string group

    
@parser_rule
def p_attr_accs(psr_val):
    'attrtype : ATTR_ACCS'
    psr_val[0] = 'accs'

@parser_rule
def p_attr_labl(psr_val):
    'attrtype : ATTR_LABL'
    psr_val[0] = 'labl'

@parser_rule
def p_attr_vars(psr_val):
    'attrtype : ATTR_VARS'
    psr_val[0] = 'vars'

@parser_rule
def p_attr_alis(psr_val):
    'attrtype : ATTR_ALIS'
    psr_val[0] = 'alis'

@parser_rule
def p_attr_args(psr_val):
    'attrtype : ATTR_ARGS'
    psr_val[0] = 'args'
    
@parser_rule
def p_attr_argt(psr_val):
    'attrtype : ATTR_ARGT'
    psr_val[0] = 'argt'
    
@parser_rule
def p_attr_base(psr_val):
    'attrtype : ATTR_BASE'
    psr_val[0] = 'base'
    
@parser_rule
def p_attr_bases(psr_val):
    'attrtype : ATTR_BASES'
    psr_val[0] = 'bases'
    
@parser_rule
def p_attr_binf(psr_val):
    'attrtype : ATTR_BINF'
    psr_val[0] = 'binf'
    
@parser_rule
def p_attr_body(psr_val):
    'attrtype : ATTR_BODY'
    psr_val[0] = 'body'
    
@parser_rule
def p_attr_bpos(psr_val):
    'attrtype : ATTR_BPOS'
    psr_val[0] = 'bpos'
    
@parser_rule
def p_attr_chain(psr_val):
    'attrtype : ATTR_CHAIN'
    psr_val[0] = 'chain'
    
@parser_rule
def p_attr_chan(psr_val):
    'attrtype : ATTR_CHAN'
    psr_val[0] = 'chan'
    
@parser_rule
def p_attr_clas(psr_val):
    'attrtype : ATTR_CLAS'
    psr_val[0] = 'clas'
    
@parser_rule
def p_attr_clnp(psr_val):
    'attrtype : ATTR_CLNP'
    psr_val[0] = 'clnp'
    
@parser_rule
def p_attr_cls(psr_val):
    'attrtype : ATTR_CLS'
    psr_val[0] = 'cls'
    
@parser_rule
def p_attr_cnst(psr_val):
    'attrtype : ATTR_CNST'
    psr_val[0] = 'cnst'
    
@parser_rule
def p_attr_cond(psr_val):
    'attrtype : ATTR_COND'
    psr_val[0] = 'cond'
    
@parser_rule
def p_attr_crnt(psr_val):
    'attrtype : ATTR_CRNT'
    psr_val[0] = 'crnt'
    
@parser_rule
def p_attr_csts(psr_val):
    'attrtype : ATTR_CSTS'
    psr_val[0] = 'csts'
    
@parser_rule
def p_attr_ctor(psr_val):
    'attrtype : ATTR_CTOR'
    psr_val[0] = 'ctor'
    
@parser_rule
def p_attr_dcls(psr_val):
    'attrtype : ATTR_DCLS'
    psr_val[0] = 'dcls'
    
@parser_rule
def p_attr_decl(psr_val):
    'attrtype : ATTR_DECL'
    psr_val[0] = 'decl'
    
@parser_rule
def p_attr_domn(psr_val):
    'attrtype : ATTR_DOMN'
    psr_val[0] = 'domn'
    
@parser_rule
def p_attr_else(psr_val):
    'attrtype : ATTR_ELSE'
    psr_val[0] = 'else'
    
@parser_rule
def p_attr_elts(psr_val):
    'attrtype : ATTR_ELTS'
    psr_val[0] = 'elts'
    
@parser_rule
def p_attr_expr(psr_val):
    'attrtype : ATTR_EXPR'
    psr_val[0] = 'expr'
    
@parser_rule
def p_attr_flds(psr_val):
    'attrtype : ATTR_FLDS'
    psr_val[0] = 'flds'
    
@parser_rule
def p_attr_fn(psr_val):
    'attrtype : ATTR_FN'
    psr_val[0] = 'fn'
    
@parser_rule
def p_attr_fncs(psr_val):
    'attrtype : ATTR_FNCS'
    psr_val[0] = 'fncs'
    
@parser_rule
def p_attr_hdlr(psr_val):
    'attrtype : ATTR_HDLR'
    psr_val[0] = 'hdlr'
    
@parser_rule
def p_attr_high(psr_val):
    'attrtype : ATTR_HIGH'
    psr_val[0] = 'high'
    
@parser_rule
def p_attr_init(psr_val):
    'attrtype : ATTR_INIT'
    psr_val[0] = 'init'
    
@parser_rule
def p_attr_inst(psr_val):
    'attrtype : ATTR_INST'
    psr_val[0] = 'inst'
    
@parser_rule
def p_attr_lang(psr_val):
    'attrtype : ATTR_LANG'
    psr_val[0] = 'lang'
    
@parser_rule
def p_attr_line(psr_val):
    'attrtype : ATTR_LINE'
    psr_val[0] = 'line'

@parser_rule
def p_attr_link(psr_val):
    'attrtype : ATTR_LINK'
    psr_val[0] = 'link'
    
@parser_rule
def p_attr_low(psr_val):
    'attrtype : ATTR_LOW'
    psr_val[0] = 'low'
    
@parser_rule
def p_attr_max(psr_val):
    'attrtype : ATTR_MAX'
    psr_val[0] = 'max'
    
@parser_rule
def p_attr_mbr(psr_val):
    'attrtype : ATTR_MBR'
    psr_val[0] = 'mbr'
    
@parser_rule
def p_attr_min(psr_val):
    'attrtype : ATTR_MIN'
    psr_val[0] = 'min'
    
@parser_rule
def p_attr_mngl(psr_val):
    'attrtype : ATTR_MNGL'
    psr_val[0] = 'mngl'
    
@parser_rule
def p_attr_name(psr_val):
    'attrtype : ATTR_NAME'
    psr_val[0] = 'name'
    
@parser_rule
def p_attr_nmsp(psr_val):
    'attrtype : ATTR_NMSP'
    psr_val[0] = 'mnsp'
    
@parser_rule
def p_attr_note(psr_val):
    'attrtype : ATTR_NOTE'
    psr_val[0] = 'note'
    
@parser_rule
def p_attr_nst(psr_val):
    'attrtype : ATTR_NST'
    psr_val[0] = 'nst'
    
@parser_rule
def p_attr_orig(psr_val):
    'attrtype : ATTR_ORIG'
    psr_val[0] = 'orig'
    
@parser_rule
def p_attr_parm(psr_val):
    'attrtype : ATTR_PARM'
    psr_val[0] = 'parm'

@parser_rule
def p_attr_prms(psr_val):
    'attrtype : ATTR_PRMS'
    psr_val[0] = 'prms'

@parser_rule
def p_attr_ptd(psr_val):
    'attrtype : ATTR_PTD'
    psr_val[0] = 'ptd'

@parser_rule
def p_attr_purp(psr_val):
    'attrtype : ATTR_PURP'
    psr_val[0] = 'purp'

@parser_rule
def p_attr_qual(psr_val):
    'attrtype : ATTR_QUAL'
    psr_val[0] = 'qual'

@parser_rule
def p_attr_refd(psr_val):
    'attrtype : ATTR_REFD'
    psr_val[0] = 'refd'
    
@parser_rule
def p_attr_retn(psr_val):
    'attrtype : ATTR_RETN'
    psr_val[0] = 'retn'

@parser_rule
def p_attr_rslt(psr_val):
    'attrtype : ATTR_RSLT'
    psr_val[0] = 'rslt'

@parser_rule
def p_attr_scpe(psr_val):
    'attrtype : ATTR_SCPE'
    psr_val[0] = 'scpe'
    
@parser_rule
def p_attr_sign(psr_val):
    'attrtype : ATTR_SIGN'
    psr_val[0] = 'sign'

@parser_rule
def p_attr_size(psr_val):
    'attrtype : ATTR_SIZE'
    psr_val[0] = 'size'

@parser_rule
def p_attr_spcs(psr_val):
    'attrtype : ATTR_SPCS'
    psr_val[0] = 'spcs'

@parser_rule
def p_attr_srcp(psr_val):
    'attrtype : ATTR_SRCP'
    psr_val[0] = 'srcp'

@parser_rule
def p_attr_sts(psr_val):
    'attrtype : ATTR_STS'
    psr_val[0] = 'sts'
    
@parser_rule
def p_attr_tag(psr_val):
    'attrtype : ATTR_TAG'
    psr_val[0] = 'tag'

@parser_rule
def p_attr_then(psr_val):
    'attrtype : ATTR_THEN'
    psr_val[0] = 'then'

@parser_rule
def p_attr_unql(psr_val):
    'attrtype : ATTR_UNQL'
    psr_val[0] = 'unql'

@parser_rule
def p_attr_used(psr_val):
    'attrtype_used : ATTR_USED'
    psr_val[0] = 'used'

@parser_rule
def p_attr_val(psr_val):
    'attrtype : ATTR_VAL'
    psr_val[0] = 'val'

@parser_rule
def p_attr_idx(psr_val):
    'attrtype : ATTR_IDX'
    psr_val[0] = 'idx'

@parser_rule
def p_attr_valu(psr_val):
    'attrtype : ATTR_VALU'
    psr_val[0] = 'valu'
    #psr_val[0] = attr_base(psr_val)

@parser_rule
def p_attr_vfld(psr_val):
    'attrtype : ATTR_VFLD'
    psr_val[0] = 'vfld'
    #psr_val[0] = attr_base(psr_val)
# special case for attribute OP 1 ... OP n

@parser_rule
def p_attr_OP(psr_val):
    'attrtype : ATTR_OP'
    psr_val[0] = 'op'
    #psr_val[0] = attr_base(psr_val)
# special case for attribute E 1 ... E n

@parser_rule
def p_attr_En(psr_val):
    'attrtype : ATTR_En'
    psr_val[0] = 'en'
    #psr_val[0] = attr_base(psr_val)

##########################################

@parser_rule
def p_operator_add(psr_val):
    'op_type : OPERATOR_ADD'
    psr_val[0] = '+'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_and(psr_val):
    'op_type : OPERATOR_AND'
    psr_val[0] = '&'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_andassign(psr_val):
    'op_type : OPERATOR_ANDASSIGN'
    psr_val[0] = '+='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_addr(psr_val):
    'op_type : OPERATOR_ADDR'
    psr_val[0] = '&'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_assign(psr_val):
    'op_type : OPERATOR_ASSIGN'
    psr_val[0] = '='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_call(psr_val):
    'op_type : OPERATOR_CALL'
    psr_val[0] = 'call'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_compound(psr_val):
    'op_type : OPERATOR_COMPOUND'
    psr_val[0] = 'compound'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_delete(psr_val):
    'op_type : OPERATOR_DELETE'
    psr_val[0] = 'delete'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_deref(psr_val):
    'op_type : OPERATOR_DEREF'
    psr_val[0] = 'deref'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_div(psr_val):
    'op_type : OPERATOR_DIV'
    psr_val[0] = '/'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_divassign(psr_val):
    'op_type : OPERATOR_DIVASSIGN'
    psr_val[0] = '/='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_eq(psr_val):
    'op_type : OPERATOR_EQ'
    psr_val[0] = '=='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_ge(psr_val):
    'op_type : OPERATOR_GE'
    psr_val[0] = '>='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_gt(psr_val):
    'op_type : OPERATOR_GT'
    psr_val[0] = '>'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_le(psr_val):
    'op_type : OPERATOR_LE'
    psr_val[0] = '<='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_lnot(psr_val):
    'op_type : OPERATOR_LNOT'
    psr_val[0] = 'lnot'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_lshift(psr_val):
    'op_type : OPERATOR_LSHIFT'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_lshiftassign(psr_val):
    'op_type : OPERATOR_LSHIFTASSIGN'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_lt(psr_val):
    'op_type : OPERATOR_LT'
    psr_val[0] = '<'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_minus(psr_val):
    'op_type : OPERATOR_MINUS'
    psr_val[0] = '-'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_minusassign(psr_val):
    'op_type : OPERATOR_MINUSASSIGN'
    psr_val[0] = '-='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_mult(psr_val):
    'op_type : OPERATOR_MULT'
    psr_val[0] = '*'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_multassign(psr_val):
    'op_type : OPERATOR_MULTASSIGN'
    psr_val[0] = '*='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_ne(psr_val):
    'op_type : OPERATOR_NE'
    psr_val[0] = '!='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_neg(psr_val):
    'op_type : OPERATOR_NEG'
    psr_val[0] = '!'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_new(psr_val):
    'op_type : OPERATOR_NEW'
    psr_val[0] = 'new'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_or(psr_val):
    'op_type : OPERATOR_OR'
    psr_val[0] = 'or'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_orassign(psr_val):
    'op_type : OPERATOR_ORASSIGN'
    psr_val[0] = 'orassign'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_plus(psr_val):
    'op_type : OPERATOR_PLUS'
    psr_val[0] = '+'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_plusassign(psr_val):
    'op_type : OPERATOR_PLUSASSIGN'
    psr_val[0] = '+='
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_postdec(psr_val):
    'op_type : OPERATOR_POSTDEC'
    psr_val[0] = 'postdec'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_postinc(psr_val):
    'op_type : OPERATOR_POSTINC'
    psr_val[0] = 'postinc'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_predec(psr_val):
    'op_type : OPERATOR_PREDEC'
    psr_val[0] = 'predec'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_preinc(psr_val):
    'op_type : OPERATOR_PREINC'
    psr_val[0] = 'preinc'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_rshift(psr_val):
    'op_type : OPERATOR_RSHIFT'
    psr_val[0] = 'rshift'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_vecdelete(psr_val):
    'op_type : OPERATOR_VECDELETE'
    psr_val[0] = 'vecdelete'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_vecnew(psr_val):
    'op_type : OPERATOR_VECNEW'
    psr_val[0] = 'vecnew'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_xor(psr_val):
    'op_type : OPERATOR_XOR'
    psr_val[0] = 'xor'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_xorassign(psr_val):
    'op_type : OPERATOR_XORASSIGN'
    psr_val[0] = 'xorassign'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_not(psr_val):
    'op_type : OPERATOR_NOT'
    psr_val[0] = 'not'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_pos(psr_val):
    'op_type : OPERATOR_POS'
    psr_val[0] = 'pos'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_ref(psr_val):
    'op_type : OPERATOR_REF'
    psr_val[0] = 'ref'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_rshiftassign(psr_val):
    'op_type : OPERATOR_RSHIFTASSIGN'
    psr_val[0] = 'rshiftassign'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_operator_subs(psr_val):
    'op_type : OPERATOR_SUBS'
    psr_val[0] = 'subs'
    #psr_val[0] = operator_base(psr_val)
    
@parser_rule
def p_idx_val_item(psr_val):
    'idx_val_item : ATTR_IDX NODE ATTR_VAL NODE'
    psr_val[0] = [psr_val[1],psr_val[2],psr_val[3]]
    
@parser_rule
def p_idx_val_list(psr_val):
    'idx_val_list : idx_val_item idx_val_list'
    psr_val[0] = [psr_val[1],psr_val[2]]
    
@parser_rule
def p_idx_val_list2(psr_val):
    'idx_val_list : idx_val_item'
    psr_val[0] = [psr_val[1]]
    
@parser_rule
def p_node_constructor(psr_val):
    #            1             2
    'node : NODE CONSTRUCTOR LEN idx_val_list attr_list'
    #print "CHECK LIST1 %s" % psr_val[3]
    # #psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    #psr_val[0] = tuast.NodeConstructor(psr_val[2], psr_val[1], psr_val[3])
    psr_val[0] = {
        '__type__' :'constructor',
        'node' : psr_val[1],
        'len' : psr_val[2],
        'idx_val' : psr_val[3],
        'attr_list' : psr_val[4],
    }
    #psr_val[0] = merge_list({'__type__':'attr_list', 'attrs': { 'type' : '' }, 'list': psr_val[2]})
        

@parser_rule
def p_attrs_addr(psr_val):
    #           1     2         3
    'attrs :  ADDR_ATTR SOMEINT'
    psr_val[0] = { 'addr': psr_val[2] }
    
@parser_rule
def p_attrs_op0(psr_val):
    #           1     2     3
    'attrs :  OP0_ATTR attrval'
    psr_val[0] = { 'op0' : psr_val[2] } 
    #psr_val[0] = std_attrs(psr_val)
    
@parser_rule
def p_attrs_op1(psr_val):
    'attrs :  OP1_ATTR attrval'
    psr_val[0] = { 'op1': psr_val[2] }
    #psr_val[0] = std_attrs(psr_val)
    
    
@parser_rule
def p_attr_list2(psr_val):
    'attr_list : str_attrs attr_list'
    psr_val[0] = {
        'strattrs': psr_val[1],
        'list': psr_val[2]
    }
    
@parser_rule
def p_attr_list4(psr_val):
    'attr_list : addr_attrs attr_list'
    psr_val[0] = { 'addr_attrs': psr_val[1],
                   'list' : psr_val[2]
    }
    
    
@parser_rule
def p_attr_lista(psr_val):
    'attr_list : attrs'
    psr_val[0] = psr_val[1]

    
@parser_rule
def p_attr_list3(psr_val):
    'attr_list : type_attrs attr_list'
    #psr_val[0] = {'type_attrs'psr_val[1],psr_val[2]{
    psr_val[0] = merge_list({'__type__':'attr_list', 'attrs': psr_val[1], 'list': psr_val[2]})
    
@parser_rule
def p_attrs_spec2(psr_val):
     #            1          2        3        4
     'attrs :  SPEC_ATTR SPEC_REGISTER '
     psr_val[0] = { 'spec': psr_val[2] }

@parser_rule
def p_attrs_spec3(psr_val):
     #          1        2
     'attrs :  SPEC_VALU'
     psr_val[0] = psr_val[1]
 
@parser_rule
def p_attrs_note(psr_val):
    'attrs :  NOTE'
    psr_val[0] = psr_val[1]
    
    
@parser_rule
def p_attrs_strg_empty(psr_val):
    'str_attrs : STRG ' # no string....    
    m=psr_val[1]
    if m:
        #print "simple string list '%s'" % m
        psr_val[0] = m
    goto_initial(psr_val)
    

@parser_rule
def p_attrs_addrs2(psr_val):
    'addr_attrs : ADDR_ATTR SOMEHEX3'
    m=psr_val[2]
    if m:
        #print "address is set to", m
        psr_val[0] = { 'addr': m }
    goto_initial(psr_val)

@parser_rule
def p_attrs_addrs3(psr_val):
    'addr_attrs : ADDR_ATTR SOMEHEX4'
    m=psr_val[2]
    if m:
        #print "address is set to", m
        psr_val[0] = { 'addr': m }
    goto_initial(psr_val)

@parser_rule
def p_attrs_member(psr_val):
    'attrs : MEMBER'
    # psr_val[0]="MEMBER(%s)" % psr_val[1]
    psr_val[0] = { 'member': psr_val[1] }

@parser_rule
def p_attrval_note(psr_val):
    'attrval :  NOTE'
    # psr_val[0]="NOTE(%s)" % p
    #psr_val[0] = tuast.Note(psr_val[1])
    psr_val[0] = { 'note' :psr_val[1] }
    
@parser_rule
def p_attrval_member(psr_val):
    'attrval : MEMBER'
    # psr_val[0]="MEMBER(%s)" % psr_val[1]
    #psr_val[0] = tuast.Member(psr_val[1])
    psr_val[0] = { 'member' : psr_val[1] }
    
@parser_rule
def p_attrval_qual(psr_val):
    'attrval :  QUAL'
    psr_val[0] = { 'qual': psr_val[1] }
    #print "QUAL(%s)" % psr_val[1]
    #psr_val[0] = tuast.Qual(psr_val[1])

@parser_rule
def p_attrval_artificial(psr_val):
    'attrval :  ARTIFICIAL'
    # psr_val[0]="ARTIFICAL(%s)" % psr_val[1]
    #psr_val[0] = tuast.Artificial(psr_val[1])
    psr_val[0] = { 'artificial' : psr_val[1] }
    
@parser_rule
def p_attrval_signed(psr_val):
    'attrval :  SIGNED'
    # psr_val[0]="SIGNED(%s)" % psr_val[1]
    #psr_val[0] = tuast.Signed(psr_val[1])
    psr_val[0] = {'signed':psr_val[1]}
    
@parser_rule
def p_attrval_struct(psr_val):
    'attrval :  STRUCT'
    # psr_val[0]="STRUCT(%s)" % psr_val[1]
    #psr_val[0] = tuast.Struct(psr_val[1])
    psr_val[0] = { 'struct' : psr_val[1] }

@parser_rule
def p_attrval_constructor(psr_val):
    'attrval :  CONSTRUCTOR'
    # psr_val[0]="CONSTRUCTOR(%s)" % psr_val[1]
    #psr_val[0] = tuast.VConstructor(psr_val[1])
    psr_val[0] = {'constructor':psr_val[1]}

@parser_rule
def p_attrval_op(psr_val):
    'attrval :  op_type'
    # psr_val[0]="OP(%s)" % psr_val[1]
    #psr_val[0] = tuast.Op(psr_val[1])
    psr_val[0] = psr_val[1]

@parser_rule
def p_attrval_pseudo_tmpl(psr_val):
    'attrval :  PSEUDO_TMPL PSEUDO_TMPL'
    # psr_val[0]="PSEUDO_TMPL2(%s,%s)" % (psr_val[1],psr_val[2])
    #psr_val[0] = tuast.PseudoTempl(psr_val[1], psr_val[2])
    psr_val[0] = {'pseudo_tmpl':psr_val[1],
                  'pseudo_tmpl2':psr_val[2]}

@parser_rule
def p_attrval_access(psr_val):
    'attrval :  ACC '
    # psr_val[0]="ACC(%s)" % psr_val[1]
    #psr_val[0] = tuast.AccVal(psr_val[1])
    psr_val[0] = { 'acc':psr_val[1]}

@parser_rule
def p_attrval_link(psr_val):
    'attrval :  LINK'
    # "LINK(%s)" %
    #psr_val[0] = tuast.Link(psr_val[1])
    psr_val[0] = psr_val[1]

@parser_rule
def p_attrval_node(psr_val):
    'attrval : NODE'
    #m = matches(psr_val)
    #print "CHECK5 NODEREF %s" % psr_val.__dict__['slice'][1]
    #print "attrval_node %s" % psr_val.__dict__
    psr_val[0] = psr_val[1]

@parser_rule
def p_attrval_node_spec(psr_val):
    'attrval : NODE SPEC'
    # print "CHECK5 NODEREF %s" % psr_val[1]
    #psr_val[0]="NodeRef(%s)" % psr_val[1]
    #psr_val[0] = tuast.NodeRefSpec(psr_val[1], psr_val[2])
    psr_val[0] = { 'node': psr_val[1],
                   'spec' : psr_val[2]} 

@parser_rule
def p_attrval_file(psr_val):
    'attrval : BUILTIN_FILE'
    #m = matches(psr_val)
    # psr_val[0]= "FILE(%s)" % psr_val[1]
    #psr_val[0] = tuast.FileBuiltin()
    psr_val[0] = { 'file':psr_val[1]}

@parser_rule
def p_attrval_hxx_file(psr_val):
    'attrval : HXX_FILE'
    #m = matches(psr_val)
    # psr_val[0]= "FILE(%s)" % psr_val[1]
    #psr_val[0] = tuast.FilePos(psr_val[1])
    psr_val[0] = {'hxx_file' :psr_val[1] }

@parser_rule
def p_attrval_float(psr_val):
    'attrval : FLOAT'
    # psr_val[0]="FLOAT(%s)" % p
    #psr_val[0] = tuast.Float(psr_val[1])
    psr_val[0] = { 'float' : psr_val[1] }

@parser_rule
def p_attrval_float_spec(psr_val):
    'attrval : FLOAT SPEC'
    # psr_val[0]="FLOAT(%s)" % p
    #psr_val[0] = tuast.FloatSpec(psr_val[1], psr_val[2])
    psr_val[0] = { 'float_spec':psr_val[1]}

@parser_rule
def p_attrval_lang(psr_val):
    'attrval : LANG'
    # psr_val[0]="lang(%s)" % p
    #psr_val[0] = tuast.Lang(psr_val[1])
    psr_val[0] = { 'lang':psr_val[1]}

def p_error(psr_val):
    print "Check Syntax error in input! %s" % psr_val
    #print "Line Number: %s" % psr_val.lineno
    #print "Line Pos: %s" % psr_val.lexpos
    print("Parser %s" % parser)
    raise Exception('error %s' % psr_val)
    #pass
    
@parser_rule
def p_attrs_prec(psr_val):
    #           1     2         3
    'attrs :  ATTR_PREC SOMEINT2'
    goto_initial(psr_val)  # begin the string group
    psr_val[0] = {'prec':psr_val[2]}
    
@parser_rule
def p_attrs_algn(psr_val):
    #           1     2         3
    'attrs :  ATTR_ALGN SOMEINT'
    #psr_val[0] = std_attrs(psr_val)
    goto_initial(psr_val)  # begin the string group
    psr_val[0] = {psr_val[1] :psr_val[2] }

@parser_rule
def p_attrs_type6(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEINT2'
    goto_initial(psr_val)  # go back
    #print 'finished TYPE_ATTR NODE'
    #psr_val[0] = std_attrs(psr_val)
    psr_val[0] = { 'type': psr_val[1],
                   'node' : psr_val[2],
                   'int': psr_val[3],
                   'someint':psr_val[4],
    }

@parser_rule
def p_attrs_used(psr_val):
    #           type_     2     3
    'attrs : attrtype_used SOMEINT2'
    goto_initial(psr_val)  # go back
    #psr_val[0] = std_attrs(psr_val)
    psr_val[0] = {psr_val[1]:psr_val[2]}

@parser_rule
def p_attrs_type3(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEHEX2'
    goto_initial(psr_val)  # go back
    #print 'finished TYPE_ATTR NODE'
    #psr_val[0] = std_attrs(psr_val)
    psr_val[0] = { 'type': psr_val[1],
                   'node': psr_val[2],
                   'int': psr_val[3],
                   'somehex': psr_val[4]
    }

@parser_rule
def p_attrs_type3b(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEHEX3'
    goto_initial(psr_val)  # go back
    #print 'finished TYPE_ATTR NODE'
    #psr_val[0] = std_attrs(psr_val)
    #psr_val[0] = [psr_val[1],psr_val[2],psr_val[3],psr_val[4]]
    psr_val[0] = { 'type': psr_val[1],
                   'node': psr_val[2],
                   'int': psr_val[3],
                   'somehex': psr_val[4]
    }

    
@parser_rule
def p_attrs_type5(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE' # len_attrs
    #print 'finished TYPE_ATTR NODE'
    #goto_initial(psr_val)  # go back
    #psr_val[0] = std_attrs(psr_val)
    psr_val[0] = { psr_val[1] : psr_val[2] }
    
## autogenerated follows
from generated_rules import *
from generated_rules2 import *

#parser_rule
def p_attrs_strg3(psr_val):
    'str_attrs : STRG SOMESTRG'
    m=psr_val[2]
    if m:
        #print "simple string '%s'" % m
        psr_val[0] = tuast.String2(m)
    goto_initial(psr_val)

@parser_rule
def p_attr_list2a(psr_val):
    'attr_list : str_attrs'
    psr_val[0] = psr_val[1]

@parser_rule
def p_attrs(psr_val):
    'attrs :  attrtype attrval'
    psr_val[0] = {
        '__type__' : 'attrs',
        'type':psr_val[1],
        'val': psr_val[2]
    }

@parser_rule
def p_attr_list(psr_val):
    'attr_list : attrs attr_list'
    psr_val[0] = merge_list({'__type__':'attr_list', 'attrs': psr_val[1], 'list': psr_val[2]})

@parser_rule
def p_attr_list4a(psr_val):
    'attr_list : addr_attrs'
    psr_val[0] = psr_val[1]

@parser_rule
def p_attr_list3a(psr_val):
    'attr_list : type_attrs'
    psr_val[0] = psr_val[1]

@parser_rule
def p_attrs_addrs(psr_val):
    'addr_attrs : ADDR_ATTR HEXVAL'
    m=psr_val[2]
    #if m:
        #print "address is set to", m
        #psr_val[0] = [tuast.String(m)]
    #print 'after hexval'
    goto_initial(psr_val)
    psr_val[0] = { 'addr': m }
        
parser = yacc.yacc()
