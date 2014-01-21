'''
reader 
'''

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from tu import tokens
from tu import *

def p_node(p):
    'node : NODE NTYPE attrs'
    #print "CHECK1 NODE %s" % p[1]
    #print "CHECK1 TYPE %s" % p[2]
    #print "CHECK1 ATTRS %s" % p[3]
    p[0] = "%s(id: %s, %s )" % (p[2],p[1],p[3])

def p_node_constructor(p):
    'node : NODE CONSTRUCTOR attrs'
    p[0] = "%s(id: %s, %s )" % (p[2],p[1],p[3])

def p_attrs(p):
    'attrs :  ATTR attrval attrs'
    #print "CHECK2 ATTR %s" % p[1]
    #print "CHECK val %s" % p[2]
    #print "CHECK list %s" % p[3]
    p[0] = "%s:%s,%s" % (p[1],p[2],p[3])

def p_attrs_spec2(p):
    'attrs :  SPEC_ATTR SPEC_VALU SPEC_VALU attrs'
    #print "CHECK2 ATTR %s" % p[1]
    #print "CHECK val %s" % p[2]
    #print "CHECK list %s" % p[3]
    p[0] = "%s:%s,%s" % (p[1],p[2],p[3])

def p_attrs_spec1(p):
    'attrs :  SPEC_ATTR SPEC_VALU attrs'
    #print "CHECK2 ATTR %s" % p[1]
    #print "CHECK val %s" % p[2]
    #print "CHECK list %s" % p[3]
    p[0] = "%s:%s,%s" % (p[1],p[2],p[3])

def p_attrs_note(p):
    'attrs :  NOTE'
    p[0]="NOTE(%s)" % p

def p_attrval_note(p):
    'attrval :  NOTE'
    p[0]="NOTE(%s)" % p

def p_attrs_done(p):
    'attrs : '
    #    print ("DONE")
    #    print "CHECK3 %s" % p
    #    print "CHECK3 %s" % p[0]
    p[0]=""

def p_attrs_STRG(p):
    'attrs : STRG'
#    print "CHECKSTR %s" % p[1]
    p[0]=p[1]

def p_attrs_MEMBER(p):
    'attrs : MEMBER'
    p[0]=p[1]

def p_attrval_MEMBER(p):
    'attrval : MEMBER'
    p[0]=p[1]

def p_attrval_qual(p):
    'attrval :  QUAL'
    p[0]="OTHER(%s)" % p

def p_attrval_artificial(p):
    'attrval :  ARTIFICIAL'
    p[0]="ARTIFICAL(%s)" % p

def p_attrval_signed(p):
    'attrval :  SIGNED'
    p[0]="SIGNED(%s)" % p

def p_attrval_struct(p):
    'attrval :  STRUCT'
    p[0]="STRUCT(%s)" % p

def p_attrval_constructor(p):
    'attrval :  CONSTRUCTOR'
    p[0]="CONSTRUCTOR(%s)" % p

def p_attrval_op(p):
    'attrval :  OP'
    p[0]="OP(%s)" % p


def p_attrval_PSEUDO_TMPL2(p):
    'attrval :  PSEUDO_TMPL PSEUDO_TMPL'
    p[0]="PSEUDO_TMPL(%s)" % p

def p_attrval_PSEUDO_TMPL(p):
    'attrval :  PSEUDO_TMPL'
    p[0]="PSEUDO_TMPL(%s)" % p

def p_attrval_access(p):
    'attrval :  ACC '
    p[0]="ACC(%s)" % p

def p_attrval_access_spec(p):
    'attrval :  ACC SPEC_VALU'
    p[0]="ACC(%s)" % p

def p_attrval_access2(p):
    'attrval :  ACC ACC'
    p[0]="ACC(%s)" % p

# er.py:58: Symbol 'C' used, but not defined as a token or a rule
# WARNING: Token 'LANG' defined, but not used
# WARNING: Token 'MEMBER' defined, but not used
# WARNING: Token 'SPACE' defined, but not used
# WARNING: Token 'R' defined, but not used
# WARNING: Token 'ERROR' defined, but not used
# WARNING: Token 'INTCONST' defined, but not used
# WARNING: Token 'SCOPE' defined, but not used
# WARNING: Token 'STRG2' defined, but not used
# WARNING: Token 'DTYPE' defined, but not used
# WARNING: Token 'INTERNAL' defined, but not used
# WARNING: Token 'OP' defined, but not used
# WARNING: Token 'PSEUDO_TMPL' defined, but not used

def p_attrval_link(p):
    'attrval :  LINK'
    p[0]="LINK(%s)" % p

def p_attrval_node(p):
    'attrval : NODE'
#    print "CHECK5 NODEREF %s" % p[1]
    p[0]="NodeRef(%s)" % p[1]

def p_attrval_node_SPEC(p):
    'attrval : NODE SPEC'
#    print "CHECK5 NODEREF %s" % p[1]
    p[0]="NodeRef(%s)" % p[1]


def p_attrval_FILE(p):
    'attrval : BUILTIN_FILE'
    p[0]= "FILE(%s)" % p[1]

def p_attrval_HXXFILE(p):
    'attrval : HXX_FILE'
    p[0]= "FILE(%s)" % p[1]

# def p_attrval_float2(p): # used in algn
#     'attrval : FLOAT'
#     p[0]="FLOAT(%s)" % p

def p_attrval_float(p):
    'attrval : FLOAT'
    p[0]="FLOAT(%s)" % p

def p_attrval_float_SPEC(p):
    'attrval : FLOAT SPEC'
    p[0]="FLOAT(%s)" % p

def p_attrval_LANG(p):
    'attrval : LANG'
    p[0]="lang(%s)" % p




# Build the parser
parser = yacc.yacc()

#   result = parser.parse(s)

# Error rule for syntax errors
def p_error(p):
    print "Check Syntax error in input! %s" % p
    #print "Line Number: %s" % p.lineno(2)
    #print "Line Pos: %s" % p.lexpos(2)
    print ("Parser %s" % parser)
