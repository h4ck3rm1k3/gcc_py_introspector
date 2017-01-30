from attributes import parser_rule,parser_node_rule, parser_simple_rule
from utils import goto_initial, create_list, merge_list
import tuast

@parser_simple_rule
def p_attr_accs(psr_val):
    'attrs : ATTR_ACCS NODE'
    ## psr_val[0] = 'accs'

@parser_simple_rule
def p_attr_labl(psr_val):
    'attrs : ATTR_LABL NODE'
    ## psr_val[0] = 'labl'

@parser_simple_rule
def p_attr_vars(psr_val):
    'attrs : ATTR_VARS NODE'
    ## psr_val[0] = 'vars'

# @parser_simple_rule
# def p_attr_alis(psr_val):
#     'attrs : ATTR_ALIS'
#     # psr_val[0] = 'alis'

@parser_simple_rule
def p_attr_args(psr_val):
    'attrs : ATTR_ARGS NODE'
    ## psr_val[0] = 'args'

@parser_simple_rule
def p_attr_argt(psr_val):
    'attrs : ATTR_ARGT NODE'
    ## psr_val[0] = 'argt'

@parser_simple_rule
def p_attr_base(psr_val):
    'attrs : ATTR_BASE NODE'
    ## psr_val[0] = 'base'

@parser_simple_rule
def p_attr_bases(psr_val):
    'attrs : ATTR_BASES NODE'
    ## psr_val[0] = 'bases'

@parser_simple_rule
def p_attr_binf(psr_val):
    'attrs : ATTR_BINF NODE'
    # psr_val[0] = 'binf'


@parser_simple_rule
def p_attr_bpos(psr_val):
    'attrs : ATTR_BPOS NODE'
    # psr_val[0] = 'bpos'


@parser_simple_rule
def p_attr_chan(psr_val):
    'attrs : ATTR_CHAN NODE'
    # psr_val[0] = 'chan'

@parser_simple_rule
def p_attr_clas(psr_val):
    'attrs : ATTR_CLAS NODE'
    # psr_val[0] = 'clas'

@parser_simple_rule
def p_attr_clnp(psr_val):
    'attrs : ATTR_CLNP NODE'
    # psr_val[0] = 'clnp'

@parser_simple_rule
def p_attr_cls(psr_val):
    'attrs : ATTR_CLS NODE'
    # psr_val[0] = 'cls'

@parser_simple_rule
def p_attr_cnst(psr_val):
    'attrs : ATTR_CNST NODE'
    # psr_val[0] = 'cnst'

@parser_simple_rule
def p_attr_cond(psr_val):
    'attrs : ATTR_COND NODE'
    # psr_val[0] = 'cond'

@parser_simple_rule
def p_attr_crnt(psr_val):
    'attrs : ATTR_CRNT NODE'
    # psr_val[0] = 'crnt'

@parser_simple_rule
def p_attr_csts(psr_val):
    'attrs : ATTR_CSTS NODE'
    # psr_val[0] = 'csts'

@parser_simple_rule
def p_attr_ctor(psr_val):
    'attrs : ATTR_CTOR NODE'
    # psr_val[0] = 'ctor'

@parser_simple_rule
def p_attr_dcls(psr_val):
    'attrs : ATTR_DCLS NODE'
    # psr_val[0] = 'dcls'

@parser_simple_rule
def p_attr_decl(psr_val):
    'attrs : ATTR_DECL NODE'
    # psr_val[0] = 'decl'

@parser_simple_rule
def p_attr_domn(psr_val):
    'attrs : ATTR_DOMN NODE'
    # psr_val[0] = 'domn'

@parser_simple_rule
def p_attr_else(psr_val):
    'attrs : ATTR_ELSE NODE'
    # psr_val[0] = 'else'

@parser_simple_rule
def p_attr_elts(psr_val):
    'attrs : ATTR_ELTS NODE'
    # psr_val[0] = 'elts'

@parser_simple_rule
def p_attr_expr(psr_val):
    'attrs : ATTR_EXPR NODE'
    # psr_val[0] = 'expr'

@parser_simple_rule
def p_attr_flds(psr_val):
    'attrs : ATTR_FLDS NODE'
    # psr_val[0] = 'flds'

@parser_simple_rule
def p_attr_fn(psr_val):
    'attrs : ATTR_FN NODE'
    # psr_val[0] = 'fn'

@parser_simple_rule
def p_attr_fncs(psr_val):
    'attrs : ATTR_FNCS NODE'
    # psr_val[0] = 'fncs'

@parser_simple_rule
def p_attr_hdlr(psr_val):
    'attrs : ATTR_HDLR NODE'
    # psr_val[0] = 'hdlr'

@parser_simple_rule
def p_attr_high(psr_val):
    'attrs : ATTR_HIGH NODE'
    # psr_val[0] = 'high'

@parser_simple_rule
def p_attr_init(psr_val):
    'attrs : ATTR_INIT NODE'
    # psr_val[0] = 'init'

@parser_simple_rule
def p_attr_inst(psr_val):
    'attrs : ATTR_INST NODE'
    # psr_val[0] = 'inst'

@parser_simple_rule
def p_attr_lang(psr_val):
    'attrs : ATTR_LANG NODE'
    # psr_val[0] = 'lang'

@parser_simple_rule
def p_attr_line(psr_val):
    'attrs : ATTR_LINE NODE'
    # psr_val[0] = 'line'

@parser_simple_rule
def p_attr_low(psr_val):
    'attrs : ATTR_LOW NODE'
    # psr_val[0] = 'low'

@parser_simple_rule
def p_attr_max(psr_val):
    'attrs : ATTR_MAX NODE'
    # psr_val[0] = 'max'

@parser_simple_rule
def p_attr_mbr(psr_val):
    'attrs : ATTR_MBR NODE'
    # psr_val[0] = 'mbr'

@parser_simple_rule
def p_attr_min(psr_val):
    'attrs : ATTR_MIN NODE'
    # psr_val[0] = 'min'


@parser_simple_rule
def p_attr_name(psr_val):
    'attrs : ATTR_NAME NODE'
    ## psr_val[0] = 'name'

@parser_simple_rule
def p_attr_nmsp(psr_val):
    'attrs : ATTR_NMSP NODE'
    # psr_val[0] = 'mnsp'

@parser_simple_rule
def p_attr_note(psr_val):
    'attrs : ATTR_NOTE NODE'
    # psr_val[0] = 'note'

@parser_simple_rule
def p_attr_nst(psr_val):
    'attrs : ATTR_NST NODE'
    # psr_val[0] = 'nst'

@parser_simple_rule
def p_attr_orig(psr_val):
    'attrs : ATTR_ORIG NODE'
    # psr_val[0] = 'orig'

@parser_simple_rule
def p_attr_parm(psr_val):
    'attrs : ATTR_PARM NODE'
    # psr_val[0] = 'parm'

@parser_simple_rule
def p_attr_prms(psr_val):
    'attrs : ATTR_PRMS NODE'
    # psr_val[0] = 'prms'

@parser_simple_rule
def p_attr_ptd(psr_val):
    'attrs : ATTR_PTD NODE'
    # psr_val[0] = 'ptd'

@parser_simple_rule
def p_attr_purp(psr_val):
    'attrs : ATTR_PURP NODE'
    # psr_val[0] = 'purp'

@parser_simple_rule
def p_attr_qual(psr_val):
    'attrs : ATTR_QUAL QUAL'
    # psr_val[0] = 'qual'

@parser_simple_rule
def p_attr_refd(psr_val):
    'attrs : ATTR_REFD NODE'
    # psr_val[0] = 'refd'

@parser_simple_rule
def p_attr_retn(psr_val):
    'attrs : ATTR_RETN NODE'
    # psr_val[0] = 'retn'

@parser_simple_rule
def p_attr_rslt(psr_val):
    'attrs : ATTR_RSLT NODE'
    # psr_val[0] = 'rslt'

@parser_simple_rule
def p_attr_scpe(psr_val):
    'attrs : ATTR_SCPE NODE'
    ## psr_val[0] = 'scpe'

@parser_simple_rule
def p_attr_sign(psr_val):
    'attrs : ATTR_SIGN SIGNED'
    # psr_val[0] = 'sign'

@parser_simple_rule
def p_attr_size(psr_val):
    'attrs : ATTR_SIZE NODE'
    # psr_val[0] = 'size'

@parser_simple_rule
def p_attr_spcs(psr_val):
    'attrs : ATTR_SPCS NODE'
    # psr_val[0] = 'spcs'

@parser_simple_rule
def p_attr_srcp(psr_val):
    'attrs : ATTR_SRCP BUILTIN_FILE'
    ## psr_val[0] = 'srcp'

@parser_simple_rule
def p_attr_srcp_hxx(psr_val):
    'attrs : ATTR_SRCP HXX_FILE'
    ## psr_val[0] = 'srcp'

@parser_simple_rule
def p_attr_sts(psr_val):
    'attrs : ATTR_STS NODE'
    # psr_val[0] = 'sts'

@parser_simple_rule
def p_attr_tag(psr_val):
    'attrs : ATTR_TAG STRUCT'
    # psr_val[0] = 'tag'

@parser_simple_rule
def p_attr_then(psr_val):
    'attrs : ATTR_THEN NODE'
    # psr_val[0] = 'then'

@parser_simple_rule
def p_attr_unql(psr_val):
    'attrs : ATTR_UNQL NODE'
    # psr_val[0] = 'unql'

@parser_simple_rule
def p_attr_used(psr_val):
    'attrs : ATTR_USED SOMEINT2'
    goto_initial(psr_val)  # go back
    # psr_val[0] = 'used'

@parser_simple_rule
def p_attr_val(psr_val):
    'attrs : ATTR_VAL NODE'
    # psr_val[0] = 'val'

@parser_simple_rule
def p_attr_idx(psr_val):
    'attrs : ATTR_IDX NODE'
    # psr_val[0] = 'idx'

@parser_simple_rule
def p_attr_valu(psr_val):
    'attrs : ATTR_VALU NODE'
    # psr_val[0] = 'valu'
    ## psr_val[0] = attr_base(psr_val)

@parser_simple_rule
def p_attr_vfld(psr_val):
    'attrs : ATTR_VFLD NODE'
    # psr_val[0] = 'vfld'
    ## psr_val[0] = attr_base(psr_val)
# special case for attribute OP 1 ... OP n

@parser_simple_rule
def p_attr_OP(psr_val):
    'attrs : ATTR_OP NODE'
    # psr_val[0] = 'op'
    ## psr_val[0] = attr_base(psr_val)
# special case for attribute E 1 ... E n

@parser_simple_rule
def p_attr_En(psr_val):
    'attrs : ATTR_En NODE'
    # psr_val[0] = 'en'
    ## psr_val[0] = attr_base(psr_val)

@parser_simple_rule
def p_attrs_addr(psr_val):
    #           1     2         3
    'addr_attrs :  ADDR_ATTR SOMEINT'
    psr_val[0] = { 'addr': psr_val[2] }

@parser_simple_rule
def p_attrs_op0(psr_val):
    #           1     2     3
    'attrs :  OP0_ATTR op_type'
    #psr_val[0] = { 'op0' : psr_val[2] }
    #psr_val[0] = std_attrs(psr_val)

@parser_simple_rule
def p_attrs_op1(psr_val):
    'attrs :  OP1_ATTR op_type'
    #psr_val[0] = { 'op1': psr_val[2] }
    #psr_val[0] = std_attrs(psr_val)
    
@parser_simple_rule
def p_attrs_spec2(psr_val):
     #            1          2        3        4
     'attrs :  SPEC_ATTR SPEC_REGISTER '
     #psr_val[0] = { 'spec': psr_val[2] }


@parser_rule
def p_attrs_note(psr_val):
    'attrs :  ATTR_NOTE ARTIFICIAL'
    psr_val[0] = psr_val[1]

@parser_rule
def p_attrs_member(psr_val):
    'attrs : MEMBER'
    # psr_val[0]="MEMBER(%s)" % psr_val[1]
    psr_val[0] = { 'member': psr_val[1] }


# @parser_rule
# def p_attrval_note(psr_val):
#     'attrval :  NOTE'
#     # psr_val[0]="NOTE(%s)" % p
#     #psr_val[0] = tuast.Note(psr_val[1])
#     psr_val[0] = { 'note' :psr_val[1] }

# @parser_rule
# def p_attrval_member(psr_val):
#     'attrval : MEMBER'
#     # psr_val[0]="MEMBER(%s)" % psr_val[1]
#     #psr_val[0] = tuast.Member(psr_val[1])
#     psr_val[0] = { 'member' : psr_val[1] }

# @parser_rule
# def p_attrval_qual(psr_val):
#     'attrval :  QUAL'
#     psr_val[0] = { 'qual': psr_val[1] }
#     #print "QUAL(%s)" % psr_val[1]
#     #psr_val[0] = tuast.Qual(psr_val[1])

# @parser_rule
# def p_attrval_artificial(psr_val):
#     'attrval :  ARTIFICIAL'
#     # psr_val[0]="ARTIFICAL(%s)" % psr_val[1]
#     #psr_val[0] = tuast.Artificial(psr_val[1])
#     psr_val[0] = { 'artificial' : psr_val[1] }

# @parser_rule
# def p_attrval_signed(psr_val):
#     'attrval :  SIGNED'
#     # psr_val[0]="SIGNED(%s)" % psr_val[1]
#     #psr_val[0] = tuast.Signed(psr_val[1])
#     psr_val[0] = {'signed':psr_val[1]}

# @parser_rule
# def p_attrval_struct(psr_val):
#     'attrval :  STRUCT'
#     # psr_val[0]="STRUCT(%s)" % psr_val[1]
#     #psr_val[0] = tuast.Struct(psr_val[1])
#     psr_val[0] = { 'struct' : psr_val[1] }

# @parser_rule
# def p_attrval_constructor(psr_val):
#     'attrval :  CONSTRUCTOR'
#     # psr_val[0]="CONSTRUCTOR(%s)" % psr_val[1]
#     #psr_val[0] = tuast.VConstructor(psr_val[1])
#     psr_val[0] = {'constructor':psr_val[1]}

# @parser_rule
# def p_attrval_op(psr_val):
#     'attrval :  op_type'
#     # psr_val[0]="OP(%s)" % psr_val[1]
#     #psr_val[0] = tuast.Op(psr_val[1])
#     psr_val[0] = psr_val[1]

# @parser_rule
# def p_attrval_pseudo_tmpl(psr_val):
#     'attrval :  PSEUDO_TMPL PSEUDO_TMPL'
#     # psr_val[0]="PSEUDO_TMPL2(%s,%s)" % (psr_val[1],psr_val[2])
#     #psr_val[0] = tuast.PseudoTempl(psr_val[1], psr_val[2])
#     psr_val[0] = {'pseudo_tmpl':psr_val[1],
#                   'pseudo_tmpl2':psr_val[2]}

# @parser_rule
# def p_attrval_access(psr_val):
#     'attrval :  ACC '
#     # psr_val[0]="ACC(%s)" % psr_val[1]
#     #psr_val[0] = tuast.AccVal(psr_val[1])
#     psr_val[0] = { 'acc':psr_val[1]}

@parser_simple_rule
def p_attr_mngl(psr_val):
    'attrs : ATTR_MNGL NODE'
    #psr_val[0] = 'mngl'

@parser_simple_rule
def p_attr_chain(psr_val):
    'attrs : ATTR_CHAIN NODE'
    #psr_val[0] = 'chain'

@parser_simple_rule
def p_attrs_link(psr_val):
    'attrs :  ATTR_LINK LINK'

@parser_simple_rule
def p_attrs_body(psr_val):
    'attrs :  ATTR_BODY LINK'

@parser_simple_rule
def p_attrs_body2(psr_val):
    'attrs :  ATTR_BODY NODE'

# @parser_rule
# def p_attrval_node(psr_val):
#     'attrval : NODE'
#     #m = matches(psr_val)
#     #print "CHECK5 NODEREF %s" % psr_val.__dict__['slice'][1]
#     #print "attrval_node %s" % psr_val.__dict__
#     psr_val[0] = { 'node': psr_val[1] }

# @parser_rule
# def p_attrval_node_spec(psr_val):
#     'attrval : NODE SPEC'
#     # print "CHECK5 NODEREF %s" % psr_val[1]
#     #psr_val[0]="NodeRef(%s)" % psr_val[1]
#     #psr_val[0] = tuast.NodeRefSpec(psr_val[1], psr_val[2])
#     psr_val[0] = { 'node': psr_val[1],
#                    'spec' : psr_val[2]}

# @parser_rule
# def p_attrval_file(psr_val):
#     'attrval : BUILTIN_FILE'
#     #m = matches(psr_val)
#     # psr_val[0]= "FILE(%s)" % psr_val[1]
#     #psr_val[0] = tuast.FileBuiltin()
#     psr_val[0] = { 'file':psr_val[1]}

# @parser_rule
# def p_attrval_hxx_file(psr_val):
#     'attrval : HXX_FILE'
#     #m = matches(psr_val)
#     # psr_val[0]= "FILE(%s)" % psr_val[1]
#     #psr_val[0] = tuast.FilePos(psr_val[1])
#     psr_val[0] = {'hxx_file' :psr_val[1] }

# @parser_rule
# def p_attrval_float(psr_val):
#     'attrval : FLOAT'
#     # psr_val[0]="FLOAT(%s)" % p
#     #psr_val[0] = tuast.Float(psr_val[1])
#     psr_val[0] = { 'float' : psr_val[1] }

# @parser_rule
# def p_attrval_float_spec(psr_val):
#     'attrval : FLOAT SPEC'
#     # psr_val[0]="FLOAT(%s)" % p
#     #psr_val[0] = tuast.FloatSpec(psr_val[1], psr_val[2])
#     psr_val[0] = { 'float_spec':psr_val[1]}

# @parser_rule
# def p_attrval_lang(psr_val):
#     'attrval : LANG'
#     # psr_val[0]="lang(%s)" % p
#     #psr_val[0] = tuast.Lang(psr_val[1])
#     psr_val[0] = { 'lang':psr_val[1]}

@parser_simple_rule
def p_attrs_prec(psr_val):
    #           1     2         3
    'attrs :  ATTR_PREC SOMEINT2'
    goto_initial(psr_val)  # begin the string group
    #psr_val[0] = {'prec':psr_val[2]}

@parser_simple_rule
def p_attrs_algn(psr_val):
    #           1     2         3
    'attrs :  ATTR_ALGN SOMEINT'
    #psr_val[0] = std_attrs(psr_val)
    goto_initial(psr_val)  # begin the string group
    #psr_val[0] = {psr_val[1] :psr_val[2] }

# @parser_simple_rule
# def p_attrs_used(psr_val):
#     #           type_     2     3
#     'attrs : attrtype_used SOMEINT2'
#     goto_initial(psr_val)  # go back
#     #psr_val[0] = std_attrs(psr_val)
#     #psr_val[0] = {psr_val[1]:psr_val[2]}

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
def p_attrs_type6(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEINT2'
    goto_initial(psr_val)  # go back
    #print 'finished TYPE_ATTR NODE'
    #psr_val[0] = std_attrs(psr_val)
    psr_val[0] = { '__type__': 'type',
                   'node' : psr_val[2],
                   'int': psr_val[3],
                   'someint':psr_val[4],
    }
    
@parser_rule
def p_attrs_type3(psr_val):
    #           type_     2     3
    'type_attrs : TYPE_ATTR NODE INT SOMEHEX2'
    goto_initial(psr_val)  # go back
    #print 'finished TYPE_ATTR NODE'
    #psr_val[0] = std_attrs(psr_val)
    psr_val[0] = { '__type__': 'type',
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
    psr_val[0] = { '__type__': 'type',
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
    
#parser_rule
def p_attrs_strg3(psr_val):
    'str_attrs : STRG SOMESTRG'
    m=psr_val[2]
    if m:
        #print "simple string '%s'" % m
        psr_val[0] = tuast.String2(m)
    goto_initial(psr_val)
    
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
