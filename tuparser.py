'''
reader
'''
from attributes import parser_rule,parser_node_rule, parser_simple_rule
# this first rule is synthetic and matches any nodes

start = 'anynode'

#@parser_rule
def p_any_node(psr_val):
    'anynode : node '
    # the node declaration
    psr_val[0]=psr_val[1]

import pprint2
import ply.yacc as yacc # Get the token map from the lexer.  This is required.
from tu import tokens
import tuast  # import Link
from utils import goto_initial, create_list, merge_list

# the first rule is important
import nodes

@parser_rule
def p_node_id(psr_val):
    # the identifier node declaration
    'node : NODE HEXVAL attr_list' # len_attrs
    psr_val[0] = { 'node' : nodes.declare(psr_val[1]),
                   'hexval' :psr_val[2],
                   'attr_list' : psr_val[3]
    }
    goto_initial(psr_val)  # begin the string group

@parser_rule
def p_node_constructor(psr_val):
    #            1             2
    'node : NODE CONSTRUCTOR LEN idx_val_list attr_list'
    #print "CHECK LIST1 %s" % psr_val[3]
    # #psr_val[0] = "%s(id: %s, %s )" % (psr_val[2],psr_val[1],psr_val[3])
    #psr_val[0] = tuast.NodeConstructor(psr_val[2], psr_val[1], psr_val[3])
    psr_val[0] = {
        '__type__' :'constructor',
        'node' : nodes.declare(psr_val[1]),
        'len' : psr_val[2],
        'idx_val' : psr_val[3],
        'attr_list' : psr_val[4],
    }
    #psr_val[0] = merge_list({'__type__':'attr_list', 'attrs': { 'type' : '' }, 'list': psr_val[2]})


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
    nd = nodes.reference(psr_val[2],'idx')
    nd2 = nodes.reference(psr_val[4],'val')
    psr_val[0] = { 'idx':psr_val[1],
                   'nodes': nd,
                   'attrval': psr_val[3],
                   'node2': nd2
    }
    #nd.ref(psr_val[0])
    #nd2.ref(psr_val[0])

@parser_rule
def p_idx_val_list(psr_val):
    'idx_val_list : idx_val_item idx_val_list'
    psr_val[0] = [psr_val[1],psr_val[2]]

@parser_rule
def p_idx_val_list2(psr_val):
    'idx_val_list : idx_val_item'
    psr_val[0] = [psr_val[1]]





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


#@parser_rule
def p_attr_lista(psr_val):
    'attr_list : attrs'
    psr_val[0] = psr_val[1]


#@parser_rule
def p_attr_list3(psr_val):
    'attr_list : type_attrs attr_list'
    #psr_val[0] = {'type_attrs'psr_val[1],psr_val[2]{
    psr_val[0] = merge_list(
        {
            '__type__':'attr_list',
            'attrs': psr_val[1],
            'list': psr_val[2]
        }
    )

# @parser_rule
# def p_attr_link(psr_val):
#     'attrtype : ATTR_LINK'
#     psr_val[0] = 'link'

# @parser_rule
# def p_attrval_link(psr_val):
#     'attrval :  LINK'
#     # "LINK(%s)" %
#     #psr_val[0] = tuast.Link(psr_val[1])
#     psr_val[0] = psr_val[1]


def p_error(psr_val):
    print "Check Syntax error in input! %s" % psr_val
    #print "Line Number: %s" % psr_val.lineno
    #print "Line Pos: %s" % psr_val.lexpos
    print("Parser %s" % parser)
    raise Exception('error %s' % psr_val)
    #pass





## autogenerated follows


#@parser_rule
def p_attr_list2a(psr_val):
    'attr_list : str_attrs'
    psr_val[0] = psr_val[1]

#@parser_rule
def p_attr_list(psr_val):
    'attr_list : attrs attr_list'
    psr_val[0] = merge_list({'__type__':'attr_list', 'attrs': psr_val[1], 'list': psr_val[2]})

#@parser_rule
def p_attr_list4a(psr_val):
    'attr_list : addr_attrs'
    psr_val[0] = psr_val[1]

#@parser_rule
def p_attr_list_empty(psr_val):
    'attr_list : '

#@parser_rule
def p_attr_list3a(psr_val):
    'attr_list : type_attrs'
    psr_val[0] = psr_val[1]


        
from tu_attrs import *
from generated_rules import *
from generated_rules2 import *

parser = yacc.yacc()
