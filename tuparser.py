'''
reader
'''

import ply.yacc as yacc
  # Get the token map from the lexer.  This is required.

from tu import tokens
#print(tokens)

import tuast  # import Link


def p_node(psr_val):
    'node : NODE NTYPE attrs'
    # print "CHECK1 NODE %s" % psr_val[1]
    # print "CHECK1 TYPE %s" % psr_val[2]
    #print "CHECK1 ATTRS %s" % psr_val[3]
    # psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    psr_val[0] = tuast.Node(psr_val[2], psr_val[1], psr_val[3])


def p_node_constructor(psr_val):
    #            1             2
    'node : NODE CONSTRUCTOR attrs'
    #print "CHECK LIST1 %s" % psr_val[3]
    # psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    psr_val[0] = tuast.NodeConstructor(psr_val[2], psr_val[1], psr_val[3])


def p_attrs(psr_val):
    #           1     2     3
    'attrs :  ATTR attrval attrs'
    # print "CHECK2 ATTR %s" % psr_val[1]
    # print "CHECK attrval %s" % psr_val[2]
    #print "CHECK LIST2 %s" % psr_val[3]

    #psr_val[0] = "%s:%s,%s" % (psr_val[1],psr_val[2],psr_val[3])
    if psr_val[3] :
        current_list = psr_val[3]
        #print "CHECK3 attrval %s" % current_list
        node = tuast.Attr(psr_val[1], psr_val[2])
        #print "CHECK3 nose %s" % node
        current_list.append(node)
        #print "CHECK3 list %s" % current_list
        result = current_list
        #print "CHECK3 res %s" % result
    else:
#        print "CHECK31 attrval %s" % psr_val[3]
        result = [tuast.Attr(psr_val[1], psr_val[2])]

    #print "check result %s" % result
    psr_val[0] = result


def std_attrs(psr_val):
    type_str=psr_val[1]
    assert(type_str)
    #print "CHECK2 TYPE_ATTR %s" % type_str
    #print "CHECK attrval %s" % psr_val[2]
    node = tuast.Attr(type_str, psr_val[2])
    if psr_val[3] :
        current_list = psr_val[3]
        if isinstance(current_list,list):
            current_list.append(node)
        else:
            current_list = [current_list, node]
        result = current_list
    else:
        result = node
    return result

def p_attrs_type(psr_val):
    #           1     2     3
    'attrs :  TYPE_ATTR attrval attrs'
    psr_val[0] = std_attrs(psr_val)

def p_attrs_op0(psr_val):
    #           1     2     3
    'attrs :  OP0_ATTR attrval attrs'
    psr_val[0] = std_attrs(psr_val)
    
def p_attrs_done(psr_val):
    'attrs : '
    # print "final attrs %s" % p
    #print (stack)
    psr_val[0] = [] # empty list

def p_attrs_spec2(psr_val):
    #            1          2        3        4
    'attrs :  SPEC_ATTR SPEC_VALU SPEC_VALU attrs'
    # this manages a list of tiems
    # print "CHECK2 ATTR %s" % psr_val[1]
    # print "CHECK val %s" % psr_val[2]
    # print "CHECK list3 %s" % psr_val[4]
    psr_val[0] = psr_val[4].append(tuast.SpecAttr(psr_val[1], psr_val[2], psr_val[3]))

    # psr_val[0] = "%s:%s,%s" % (
    #     "test1:%s" % psr_val[1],
    #     tuast.Spec(psr_val[2]),
    #     "test3:%s" % psr_val[3]
    # )

def p_attrs_spec1(psr_val):
    #           1          2       3
    'attrs :  SPEC_ATTR SPEC_VALU attrs'
    # print "CHECK5 ATTR %s" % psr_val[1]
    # print "CHECK5 val %s" % psr_val[2]
    # print "CHECK list5 %s" % psr_val[3]
    #    psr_val[0] = "%s:TEST1:%s,TEST2:%s" % (psr_val[1],psr_val[2],psr_val[3])
    if psr_val[3]:
        node_list = psr_val[3]
        node_list.append(tuast.SpecAttr2(psr_val[1], psr_val[2]))
        psr_val[0] = node_list
    else:
        psr_val[0] = [tuast.SpecAttr2(psr_val[1], psr_val[2])]
    #print "RESULT %s" % psr_val[0]

def p_attrs_note(psr_val):
    'attrs :  NOTE'
    # psr_val[0]="NOTE(%s)" % p
    psr_val[0] = tuast.NoteAttr(psr_val[1])


def p_attrs_strg(psr_val):
    'attrs : STRG'
    # print "CHECKSTR %s" % psr_val[1]
    #psr_val[0]="STRG(%s)" % psr_val[1]
    psr_val[0] = [tuast.String(psr_val[1])]


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
    # psr_val[0]="OTHER(%s)" % psr_val[1]
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
    'attrval :  OP'
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


def p_attrval_access_spec(psr_val):
    'attrval :  ACC SPEC_VALU'
    # psr_val[0]="ACC2(%s,%s)" % (psr_val[1],psr_val[2])
    psr_val[0] = tuast.AccSpec(psr_val[1], psr_val[2])


def p_attrval_link(psr_val):
    'attrval :  LINK'
    # "LINK(%s)" %
    psr_val[0] = tuast.Link(psr_val[1])


def p_attrval_node(psr_val):
    'attrval : NODE'
    # v = "NodeRef(%s)" % psr_val[1]
    # print "CHECK5 NODEREF %s" % v
    psr_val[0] = tuast.NodeRef(psr_val[1])


def p_attrval_node_spec(psr_val):
    'attrval : NODE SPEC'
    # print "CHECK5 NODEREF %s" % psr_val[1]
    #psr_val[0]="NodeRef(%s)" % psr_val[1]
    psr_val[0] = tuast.NodeRefSpec(psr_val[1], psr_val[2])


def p_attrval_file(psr_val):
    'attrval : BUILTIN_FILE'
    # psr_val[0]= "FILE(%s)" % psr_val[1]
    psr_val[0] = tuast.FileBuiltin()


def p_attrval_hxx_file(psr_val):
    'attrval : HXX_FILE'
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

def p_node_addr_expr_type(psr_val):
    'node : NODE ADDR_EXPR TYPE_ATTR NODE OP0_ATTR NODE '
    #        1     2           3       4       5    6
    psr_val[0] = tuast.AddrExprTyped(psr_val[2], psr_val[1], psr_val[4], psr_val[6])

# addr_expr |OP0
# addr_expr |OP0|type
# aggr_init_expr |decl|E0|fn |ctor|type
# aggr_init_expr |decl|E1|E0|fn |ctor|type
# aggr_init_expr |decl|E2|E1|E0|fn |ctor|type
# aggr_init_expr |decl|E5|E4|E3|E2|E1|E0|fn |ctor|type
# aggr_init_expr |decl|E6|E5|E4|E3|E2|E1|E0|fn |ctor|type
# alignof_expr |type
# array_ref |OP1|OP0
# array_ref |OP1|OP0|type
# array_type |domn|elts|algn
# array_type |domn|elts|algn|size
# array_type |domn|elts|algn|size|unql
# array_type |domn|elts|algn|size|unql|name
# array_type |domn|elts|algn|size|unql|qual
# array_type |domn|elts|algn|unql
# array_type |domn|elts|algn|unql|name
# array_type |domn|elts|algn|unql|name|qual
# array_type |domn|elts|algn|unql|qual
# array_type |elts|algn
# array_type |elts|algn|unql
# array_type |elts|algn|unql|qual
# arrow_expr|
# arrow_expr |type
# baselink|
# bind_expr |body
# binfo |bases|spec|type
# binfo |bases|type
# binfo |binf|accs|bases|spec|type
# binfo |binf|accs|bases|type
# binfo |binf|accs|binf|accs|bases|spec|type
# binfo |binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|bases|type
# binfo |binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|binf|accs|bases|type
# bit_and_expr |OP1|OP0
# bit_and_expr |OP1|OP0|type
# bit_ior_expr |OP1|OP0
# bit_ior_expr |OP1|OP0|type
# bit_not_expr |OP0
# bit_not_expr |OP0|type
# bit_xor_expr |OP1|OP0
# boolean_type |algn|size|name
# boolean_type |algn|size|unql|name
# boolean_type |algn|size|unql|name|qual
# bound_template_template_parm |algn|name
# bound_template_template_parm |algn|unql|name
# bound_template_template_parm |algn|unql|name|qual
# break_stmt |line|type
# call_expr |E0|fn 
# call_expr |E0|fn |type
# call_expr |E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|fn 
# call_expr |E1|E0|fn 
# call_expr |E1|E0|fn |type
# call_expr |E2|E1|E0|fn 
# call_expr |E2|E1|E0|fn |type
# call_expr |E3|E2|E1|E0|fn 
# call_expr |E3|E2|E1|E0|fn |type
# call_expr |E4|E3|E2|E1|E0|fn 
# call_expr |E4|E3|E2|E1|E0|fn |type
# call_expr |E5|E4|E3|E2|E1|E0|fn 
# call_expr |E6|E5|E4|E3|E2|E1|E0|fn 
# call_expr |E7|E6|E5|E4|E3|E2|E1|E0|fn 
# call_expr |E8|E7|E6|E5|E4|E3|E2|E1|E0|fn 
# call_expr |E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|fn 
# call_expr |fn 
# call_expr |fn |type
# case_label_expr |low |name|type
# case_label_expr |name|type
# cast_expr |OP0|type
# cast_expr |type
# complex_type |algn|size
# complex_type |algn|size|name
# complex_type |algn|size|unql|name
# complex_type |algn|size|unql|name|qual
# component_ref |OP1|OP0
# component_ref |OP1|OP0|type
# compound_expr |OP1|OP0
# compound_expr |OP1|OP0|type
# cond_expr |OP2|OP1|OP0
# cond_expr |OP2|OP1|OP0|type
# const_cast_expr |OP0|type
# const_decl |cnst|chain|note|srcp|type
# const_decl |cnst|chain|note|srcp|type|name
# const_decl |cnst|chain|srcp|scpe|type|name
# const_decl |cnst|note|srcp|type
# const_decl |cnst|note|srcp|type|name
# const_decl |cnst|srcp|scpe|type|name
# constructor|lngt
# constructor|val |lngt
# constructor|val |val |lngt
# constructor|val |val |val |lngt
# constructor|val |val |val |val |lngt
# constructor|val |val |val |val |val |lngt
# constructor|val |val |val |val |val |val |lngt
# constructor|val |val |val |val |val |val |val |lngt
# constructor|val |val |val |val |val |val |val |val |lngt
# constructor|val |val |val |val |val |val |val |val |val |lngt
# constructor|val |val |val |val |val |val |val |val |val |val |lngt
# constructor|val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |lngt
# constructor|val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |lngt
# constructor|val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |val |lngt
# continue_stmt |line|type
# ctor_initializer|
# decl_expr |type
# decltype_type |algn
# dl_expr |type
# do_stmt |cond|body|line|type
# dotstar_expr|
# dynamic_cast_expr |OP0|type
# enumeral_type |csts|max |min |sign|prec|algn|size|name
# enumeral_type |csts|max |min |sign|prec|algn|size|unql|name
# enumeral_type |csts|max |min |sign|prec|algn|size|unql|name|qual
# enumeral_type |csts|sign|prec|algn|name
# enumeral_type |max |min |sign|prec|algn|size|name
# eq_expr |OP1|OP0
# eq_expr |OP1|OP0|type
# error_mark|
# expr_stmt |expr|line|type
# field_decl |accs|chain|srcp|scpe|type|name
# field_decl |algn|accs|chain|srcp|scpe|type|name
# field_decl |algn|spec|accs|chain|srcp|scpe|type|name
# field_decl |bpos|algn|size|accs|chain|note|srcp|scpe|type
# field_decl |bpos|algn|size|accs|chain|note|srcp|scpe|type|name
# field_decl |bpos|algn|size|accs|chain|srcp|scpe|type
# field_decl |bpos|algn|size|accs|chain|srcp|scpe|type|name
# field_decl |bpos|algn|size|accs|note|srcp|scpe|type
# field_decl |bpos|algn|size|accs|srcp|scpe|type
# field_decl |bpos|algn|size|accs|srcp|scpe|type|name
# field_decl |bpos|algn|size|spec|accs|chain|srcp|scpe|type|name
# for_stmt |body|cond|init|line|type
# for_stmt |body|expr|cond|init|line|type
# for_stmt |body|init|line|type
# function_decl |body|link|body|args|note|accs|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|args|note|accs|note|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|args|note|accs|note|note|srcp|scpe|type|name
# function_decl |body|link|body|args|note|accs|note|srcp|scpe|type|name
# function_decl |body|link|body|args|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|args|note|note|accs|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|args|note|note|accs|note|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|args|note|note|accs|note|note|srcp|scpe|type|name
# function_decl |body|link|body|args|note|note|accs|note|srcp|scpe|type|name
# function_decl |body|link|body|args|note|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|args|note|note|spec|accs|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|args|note|note|spec|accs|note|srcp|scpe|type|name
# function_decl |body|link|body|args|note|note|srcp|scpe|type|name
# function_decl |body|link|body|args|note|spec|accs|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|args|note|spec|accs|note|srcp|scpe|type|name
# function_decl |body|link|body|args|note|srcp|scpe|type|name
# function_decl |body|link|body|note|accs|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|note|accs|note|srcp|scpe|type|name
# function_decl |body|link|body|note|chain|srcp|scpe|type|name
# function_decl |body|link|body|note|srcp|scpe|type|name
# function_decl |link|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|accs|note|srcp|scpe|type|mngl|name
# function_decl |link|args|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|args|accs|note|note|chain|note|srcp|scpe|type|mngl|name
# function_decl |link|args|accs|note|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|args|accs|note|note|srcp|scpe|type|mngl|name
# function_decl |link|args|accs|note|srcp|scpe|type|mngl|name
# function_decl |link|args|chain|note|srcp|type|mngl|name
# function_decl |link|args|chain|srcp|scpe|type|mngl|name
# function_decl |link|args|lang|chain|srcp|scpe|type|name
# function_decl |link|args|note|accs|note|chain|note|srcp|scpe|type|mngl|name
# function_decl |link|args|note|accs|note|chain|note|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|note|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|args|note|accs|note|chain|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|note|accs|note|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|args|note|accs|note|note|srcp|scpe|type|mngl|name
# function_decl |link|args|note|accs|note|note|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|note|accs|note|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|args|note|spec|accs|note|chain|note|srcp|scpe|type|mngl|name
# function_decl |link|args|note|spec|accs|note|chain|note|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|note|spec|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|args|note|spec|accs|note|chain|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|note|spec|accs|note|note|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|note|spec|accs|note|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|note|spec|spec|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|args|note|spec|spec|accs|note|chain|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|note|spec|spec|accs|note|srcp|scpe|type|orig|mngl|name
# function_decl |link|args|spec|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|args|spec|accs|note|srcp|scpe|type|mngl|name
# function_decl |link|args|srcp|scpe|type|mngl|name
# function_decl |link|body|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|accs|note|srcp|scpe|type|mngl|name
# function_decl |link|body|accs|note|srcp|scpe|type|name
# function_decl |link|body|args|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|args|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|accs|note|note|chain|note|srcp|scpe|type|name
# function_decl |link|body|args|accs|note|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|args|accs|note|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|accs|note|note|note|srcp|scpe|type|name
# function_decl |link|body|args|accs|note|note|srcp|scpe|type|mngl|name
# function_decl |link|body|args|accs|note|note|srcp|scpe|type|name
# function_decl |link|body|args|accs|note|srcp|scpe|type|mngl|name
# function_decl |link|body|args|accs|note|srcp|scpe|type|name
# function_decl |link|body|args|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|args|chain|srcp|scpe|type|name
# function_decl |link|body|args|lang|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|accs|note|chain|note|srcp|scpe|type|name
# function_decl |link|body|args|note|accs|note|chain|note|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|args|note|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|accs|note|chain|srcp|scpe|type|orig|mngl|name
# function_decl |link|body|args|note|accs|note|chain|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|accs|note|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|args|note|accs|note|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|accs|note|note|srcp|scpe|type|mngl|name
# function_decl |link|body|args|note|accs|note|note|srcp|scpe|type|name
# function_decl |link|body|args|note|accs|note|note|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|accs|note|srcp|scpe|type|name
# function_decl |link|body|args|note|accs|note|srcp|scpe|type|orig|mngl|name
# function_decl |link|body|args|note|accs|note|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|args|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|note|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|note|accs|note|chain|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|note|accs|note|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|note|accs|note|note|srcp|scpe|type|name
# function_decl |link|body|args|note|note|accs|note|srcp|scpe|type|name
# function_decl |link|body|args|note|note|accs|note|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|note|spec|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|spec|accs|note|chain|note|srcp|scpe|type|name
# function_decl |link|body|args|note|spec|accs|note|chain|note|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|spec|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|args|note|spec|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|spec|accs|note|chain|srcp|scpe|type|orig|mngl|name
# function_decl |link|body|args|note|spec|accs|note|chain|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|spec|accs|note|note|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|spec|accs|note|srcp|scpe|type|name
# function_decl |link|body|args|note|spec|accs|note|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|spec|spec|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|note|spec|spec|accs|note|chain|srcp|scpe|type|orig|name
# function_decl |link|body|args|note|spec|spec|accs|note|srcp|scpe|type|name
# function_decl |link|body|args|note|srcp|scpe|type|mngl|name
# function_decl |link|body|args|note|srcp|scpe|type|name
# function_decl |link|body|args|spec|accs|note|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|args|spec|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|spec|accs|note|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|spec|accs|note|note|srcp|scpe|type|name
# function_decl |link|body|args|spec|accs|note|srcp|scpe|type|mngl|name
# function_decl |link|body|args|spec|accs|note|srcp|scpe|type|name
# function_decl |link|body|args|spec|spec|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|spec|spec|accs|note|note|chain|srcp|scpe|type|name
# function_decl |link|body|args|spec|spec|accs|note|srcp|scpe|type|name
# function_decl |link|body|args|srcp|scpe|type|mngl|name
# function_decl |link|body|args|srcp|scpe|type|name
# function_decl |link|body|chain|srcp|scpe|type|mngl|name
# function_decl |link|body|chain|srcp|scpe|type|name
# function_decl |link|body|lang|chain|note|srcp|scpe|type|name
# function_decl |link|body|lang|chain|note|srcp|type|mngl|name
# function_decl |link|body|lang|chain|note|srcp|type|name
# function_decl |link|body|lang|chain|srcp|scpe|type|name
# function_decl |link|body|lang|note|srcp|scpe|type|name
# function_decl |link|body|note|accs|note|chain|srcp|scpe|type|name
# function_decl |link|body|note|accs|note|srcp|scpe|type|name
# function_decl |link|body|note|chain|srcp|scpe|type|name
# function_decl |link|body|srcp|scpe|type|mngl|name
# function_decl |link|body|srcp|scpe|type|name
# function_decl |link|chain|srcp|scpe|type|mngl|name
# function_decl |link|srcp|scpe|type|mngl|name
# function_type |prms|retn|algn|size
# function_type |prms|retn|algn|size|unql
# function_type |prms|retn|algn|size|unql|name
# function_type |retn|algn|size
# ge_expr |OP1|OP0
# ge_expr |OP1|OP0|type
# gt_expr |OP1|OP0
# gt_expr |OP1|OP0|type
# handler |body|line
# handler |body|parm|line|type
# identifier_node |note
# identifier_node |STR
# if_stmt |else|then|cond|line|type
# if_stmt |then|cond|line|type
# indirect_ref |OP0
# indirect_ref |OP0|type
# integer_cst |low |high|type
# integer_cst |low |type
# integer_type |max |min |sign|prec|algn|size
# integer_type |max |min |sign|prec|algn|size|name
# integer_type |max |min |sign|prec|algn|size|unql|name
# integer_type |max |min |sign|prec|algn|size|unql|name|qual
# label_decl |srcp
# lang_type |algn|name
# le_expr |OP1|OP0
# le_expr |OP1|OP0|type
# lshift_expr |OP1|OP0
# lshift_expr |OP1|OP0|type
# lt_expr |OP1|OP0
# lt_expr |OP1|OP0|type
# member_ref|
# method_type |prms|retn|clas|algn|size
# method_type |prms|retn|clas|algn|size|unql
# minus_expr |OP1|OP0
# minus_expr |OP1|OP0|type
# modop_expr|
# mult_expr |OP1|OP0
# mult_expr |OP1|OP0|type
# namespace_decl |alis|chain|srcp|scpe|type|orig|name
# namespace_decl |chain|srcp|scpe|type|name
# namespace_decl |dcls|chain|srcp|scpe|type|mngl
# namespace_decl |dcls|chain|srcp|scpe|type|name
# namespace_decl |dcls|lang|chain|srcp|scpe|type|name
# namespace_decl |dcls|lang|srcp|name
# namespace_decl |dcls|srcp|scpe|name
# namespace_decl |dcls|srcp|scpe|type|name
# namespace_decl |srcp|scpe|type|name
# ne_expr |OP1|OP0
# ne_expr |OP1|OP0|type
# negate_expr |OP0
# negate_expr |OP0|type
# nop_expr |OP0|type
# nw_expr |type
# offset_type |cls |ptd |note|algn|size
# offset_type |cls |ptd |note|algn|size|unql|name
# offset_type |cls |ptd |note|algn|size|unql|name|qual
# offset_type |cls |ptd |note|algn|size|unql|qual
# overload |chan|crnt
# overload |crnt
# parm_decl |used|algn|argt|chain|srcp|scpe|type|name
# parm_decl |used|algn|argt|chain|srcp|type
# parm_decl |used|algn|argt|chain|srcp|type|name
# parm_decl |used|algn|argt|srcp|scpe|type
# parm_decl |used|algn|argt|srcp|scpe|type|name
# parm_decl |used|algn|argt|srcp|type
# parm_decl |used|algn|argt|srcp|type|name
# parm_decl |used|algn|chain|srcp|scpe|type
# parm_decl |used|algn|chain|srcp|scpe|type|name
# parm_decl |used|algn|size|argt|chain|note|srcp|scpe|type|name
# parm_decl |used|algn|size|argt|chain|note|srcp|scpe|type|orig|name
# parm_decl |used|algn|size|argt|chain|note|srcp|type|name
# parm_decl |used|algn|size|argt|chain|srcp|scpe|type
# parm_decl |used|algn|size|argt|chain|srcp|scpe|type|name
# parm_decl |used|algn|size|argt|chain|srcp|scpe|type|orig|name
# parm_decl |used|algn|size|argt|chain|srcp|type
# parm_decl |used|algn|size|argt|chain|srcp|type|name
# parm_decl |used|algn|size|argt|lang|chain|srcp|scpe|type|name
# parm_decl |used|algn|size|argt|lang|chain|srcp|scpe|type|orig|name
# parm_decl |used|algn|size|argt|lang|srcp|scpe|type|name
# parm_decl |used|algn|size|argt|lang|srcp|scpe|type|orig|name
# parm_decl |used|algn|size|argt|note|srcp|scpe|type|name
# parm_decl |used|algn|size|argt|note|srcp|scpe|type|orig|name
# parm_decl |used|algn|size|argt|note|srcp|type|name
# parm_decl |used|algn|size|argt|srcp|scpe|type
# parm_decl |used|algn|size|argt|srcp|scpe|type|name
# parm_decl |used|algn|size|argt|srcp|scpe|type|orig
# parm_decl |used|algn|size|argt|srcp|scpe|type|orig|name
# parm_decl |used|algn|size|argt|srcp|type
# parm_decl |used|algn|size|argt|srcp|type|name
# parm_decl |used|algn|size|chain|note|srcp|scpe|type|name
# parm_decl |used|algn|size|chain|srcp|scpe|type
# parm_decl |used|algn|size|chain|srcp|scpe|type|name
# parm_decl |used|algn|size|note|srcp|scpe|type|name
# parm_decl |used|algn|size|srcp|scpe|type
# parm_decl |used|algn|size|srcp|scpe|type|name
# parm_decl |used|algn|srcp|scpe|type
# parm_decl |used|algn|srcp|scpe|type|name
# plus_expr |OP1|OP0
# plus_expr |OP1|OP0|type
# pointer_type |ptd |algn|size
# pointer_type |ptd |algn|size|name
# pointer_type |ptd |algn|size|unql
# pointer_type |ptd |algn|size|unql|name
# pointer_type |ptd |algn|size|unql|name|qual
# pointer_type |ptd |algn|size|unql|qual
# postdecrement_expr |OP0
# postdecrement_expr |OP0|type
# postincrement_expr |OP0
# postincrement_expr |OP0|type
# predecrement_expr |OP0
# predecrement_expr |OP0|type
# preincrement_expr |OP0
# preincrement_expr |OP0|type
# ptrmem_cst |mbr |clas|type
# real_cst |valu|type
# real_type |prec|algn|size
# real_type |prec|algn|size|name
# real_type |prec|algn|size|unql|name
# real_type |prec|algn|size|unql|name|qual
# record_type |binf|flds|tag |accs|base|accs|base|algn|size|name
# record_type |binf|flds|tag |accs|base|accs|base|algn|size|unql|name
# record_type |binf|flds|tag |accs|base|algn|size|name
# record_type |binf|flds|tag |accs|base|algn|size|unql|name
# record_type |binf|flds|tag |accs|base|algn|size|unql|name|qual
# record_type |binf|flds|tag |algn|size|name
# record_type |binf|flds|tag |algn|size|unql|name
# record_type |binf|flds|tag |algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|spec|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|spec|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|accs|spec|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|accs|spec|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|accs|spec|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|accs|spec|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|spec|base|accs|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|spec|base|accs|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|spec|base|accs|base|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|spec|base|accs|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|spec|base|accs|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|spec|base|accs|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|spec|base|accs|spec|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|spec|base|accs|spec|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|spec|base|accs|spec|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|spec|base|algn|size|name
# record_type |binf|fncs|flds|tag |accs|spec|base|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|spec|base|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |accs|spec|base|vfld|algn|size|name
# record_type |binf|fncs|flds|tag |accs|spec|base|vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |accs|spec|base|vfld|algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |algn|size|name
# record_type |binf|fncs|flds|tag |algn|size|unql|name
# record_type |binf|fncs|flds|tag |algn|size|unql|name|qual
# record_type |binf|fncs|flds|tag |vfld|algn|size|name
# record_type |binf|fncs|flds|tag |vfld|algn|size|unql|name
# record_type |binf|fncs|flds|tag |vfld|algn|size|unql|name|qual
# record_type |cls |ptd |note|algn|size
# record_type |cls |ptd |note|algn|size|unql|name
# record_type |cls |ptd |note|algn|size|unql|qual
# record_type |flds|tag |algn|size|name
# record_type |flds|tag |algn|size|unql|name|qual
# record_type |tag |algn|name
# record_type |tag |algn|unql|name
# record_type |tag |algn|unql|name|qual
# reference_type |refd|algn|size
# reference_type |refd|algn|size|unql|name
# reference_type |refd|algn|size|unql|qual
# reinterpret_cast_expr |OP0|type
# return_expr |expr|type
# return_expr |type
# rshift_expr |OP1|OP0
# rshift_expr |OP1|OP0|type
# scope_ref|
# scope_ref |type
# sizeof_expr |type
# statement_list|
# statement_list |E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E1|E0
# statement_list |E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E24|E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E25|E24|E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E2|E1|E0
# statement_list |E32|E31|E30|E29|E28|E27|E26|E25|E24|E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E33|E32|E31|E30|E29|E28|E27|E26|E25|E24|E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E34|E33|E32|E31|E30|E29|E28|E27|E26|E25|E24|E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E3|E2|E1|E0
# statement_list |E43|E42|E41|E40|E39|E38|E37|E36|E35|E34|E33|E32|E31|E30|E29|E28|E27|E26|E25|E24|E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E4|E3|E2|E1|E0
# statement_list |E5|E4|E3|E2|E1|E0
# statement_list |E6|E5|E4|E3|E2|E1|E0
# statement_list |E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E8|E7|E6|E5|E4|E3|E2|E1|E0
# statement_list |E9|E8|E7|E6|E5|E4|E3|E2|E1|E0
# static_cast_expr |OP0|type
# string_cst |STR|type
# switch_stmt |body|cond|line|type
# tag_defn |type
# target_expr |clnp|init|decl|type
# target_expr |init|decl|type
# template_decl |prms|inst|rslt|chain|srcp|scpe|type|name
# template_decl |prms|inst|rslt|srcp|scpe|type|name
# template_decl |prms|rslt|chain|note|srcp|scpe|type|name
# template_decl |prms|rslt|chain|note|srcp|type|name
# template_decl |prms|rslt|chain|srcp|scpe|type|name
# template_decl |prms|rslt|chain|srcp|scpe|type|orig|name
# template_decl |prms|rslt|note|srcp|scpe|type|name
# template_decl |prms|rslt|note|srcp|type|name
# template_decl |prms|rslt|srcp|scpe|type|name
# template_decl |prms|rslt|srcp|scpe|type|orig|name
# template_decl |prms|spcs|inst|rslt|chain|srcp|scpe|type|name
# template_decl |prms|spcs|inst|rslt|srcp|scpe|type|name
# template_id_expr|
# template_id_expr |type
# template_parm_index|
# template_template_parm |algn|name
# template_type_parm |algn|name
# template_type_parm |algn|unql|name
# template_type_parm |algn|unql|name|qual
# throw_expr |OP0|type
# throw_expr |type
# trait_expr|
# translation_unit_decl|
# tree_list |chan|valu
# tree_list |chan|valu|purp
# tree_list |valu
# tree_list |valu|purp
# tree_vec |E0|lngt
# tree_vec |E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E1|E0|lngt
# tree_vec |E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E24|E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E25|E24|E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E26|E25|E24|E23|E22|E21|E20|E19|E18|E17|E16|E15|E14|E13|E12|E11|E10|E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E2|E1|E0|lngt
# tree_vec |E3|E2|E1|E0|lngt
# tree_vec |E4|E3|E2|E1|E0|lngt
# tree_vec |E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# tree_vec |E9|E8|E7|E6|E5|E4|E3|E2|E1|E0|lngt
# trunc_div_expr |OP1|OP0
# trunc_div_expr |OP1|OP0|type
# trunc_mod_expr |OP1|OP0
# trunc_mod_expr |OP1|OP0|type
# truth_andif_expr |OP1|OP0
# truth_andif_expr |OP1|OP0|type
# truth_not_expr |OP0
# truth_not_expr |OP0|type
# truth_orif_expr |OP1|OP0
# truth_orif_expr |OP1|OP0|type
# try_block |hdlr|body|line|type
# type_decl |chain|note|srcp|scpe|type|name
# type_decl |chain|note|srcp|type
# type_decl |chain|note|srcp|type|name
# type_decl |chain|note|type|name
# type_decl |chain|srcp|scpe|type|name
# type_decl |chain|type
# type_decl |chain|type|name
# type_decl |note|srcp|scpe|type|name
# type_decl |note|srcp|type
# type_decl |note|srcp|type|name
# type_decl |srcp|scpe|type|name
# type_decl |srcp|type|name
# type_decl |type
# type_decl |type|name
# typeid_expr |type
# typename_type |algn|name
# typename_type |algn|unql|name
# typename_type |algn|unql|name|qual
# typeof_type |algn
# typeof_type |algn|unql|name
# union_type |binf|flds|tag |algn|size|name
# union_type |binf|flds|tag |algn|size|unql|name
# union_type |binf|flds|tag |algn|size|unql|name|qual
# union_type |binf|fncs|flds|tag |algn|size|name
# union_type |binf|fncs|flds|tag |algn|size|unql|name
# union_type |tag |algn|name
# union_type |tag |algn|unql|name
# using_decl |chain|srcp|scpe|type|name
# using_stmt |nmsp|line|type
# var_decl |used|algn|accs|chain|srcp|scpe|type|mngl|name
# var_decl |used|algn|accs|chain|srcp|scpe|type|name
# var_decl |used|algn|chain|srcp|scpe|type|name
# var_decl |used|algn|init|accs|chain|srcp|scpe|type|name
# var_decl |used|algn|init|chain|srcp|scpe|type|name
# var_decl |used|algn|init|link|chain|srcp|scpe|type|name
# var_decl |used|algn|init|link|note|srcp|scpe|type|name
# var_decl |used|algn|init|link|srcp|scpe|type|name
# var_decl |used|algn|init|srcp|scpe|type|name
# var_decl |used|algn|link|srcp|scpe|type|name
# var_decl |used|algn|size|accs|chain|srcp|scpe|type|mngl|name
# var_decl |used|algn|size|accs|chain|srcp|scpe|type|name
# var_decl |used|algn|size|chain|note|srcp|type|name
# var_decl |used|algn|size|chain|srcp|scpe|type|name
# var_decl |used|algn|size|init|accs|chain|srcp|scpe|type|mngl|name
# var_decl |used|algn|size|init|accs|chain|srcp|scpe|type|name
# var_decl |used|algn|size|init|chain|note|srcp|type|name
# var_decl |used|algn|size|init|chain|srcp|scpe|type|name
# var_decl |used|algn|size|init|link|accs|chain|srcp|scpe|type|mngl|name
# var_decl |used|algn|size|init|link|chain|srcp|scpe|type|mngl|name
# var_decl |used|algn|size|init|link|srcp|scpe|type|mngl|name
# var_decl |used|algn|size|init|link|srcp|scpe|type|name
# var_decl |used|algn|size|init|srcp|scpe|type|name
# var_decl |used|algn|size|lang|chain|srcp|scpe|type|name
# var_decl |used|algn|size|link|chain|srcp|scpe|type|mngl|name
# var_decl |used|algn|size|note|srcp|type
# var_decl |used|algn|size|srcp|scpe|type
# var_decl |used|algn|size|srcp|scpe|type|name
# var_decl |used|algn|srcp|scpe|type|name
# vector_type |algn|size
# vector_type |algn|size|unql|qual
# void_type |algn|name
# void_type |algn|unql|name
# void_type |algn|unql|name|qual
# while_stmt |body|cond|line|type

# Build the parser
parser = yacc.yacc()


#   result = parser.parse(s)

# Error rule for syntax errors
def p_error(psr_val):
    print "Check Syntax error in input! %s" % psr_val
    # print "Line Number: %s" % psr_val.lineno(2)
    # print "Line Pos: %s" % psr_val.lexpos(2)
    print("Parser %s" % parser)


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


#WARNING: Token 'R' defined, but not used
#WARNING: Token 'ERROR' defined, but not used
#WARNING: Token 'INTCONST' defined, but not used
#WARNING: Token 'SCOPE' defined, but not used
#WARNING: Token 'STRG2' defined, but not used
#WARNING: Token 'DTYPE' defined, but not used
#WARNING: Token 'INTERNAL' defined, but not used
