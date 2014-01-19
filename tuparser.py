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

def p_attrs(p):
    'attrs :  ATTR attrval attrs'
    #print "CHECK2 ATTR %s" % p[1]
    #print "CHECK val %s" % p[2]
    #print "CHECK list %s" % p[3]
    p[0] = "%s:%s,%s" % (p[1],p[2],p[3])

def p_attrs_done(p):
    'attrs : '
    #    print ("DONE")
    #    print "CHECK3 %s" % p
    #    print "CHECK3 %s" % p[0]
    p[0]=""

def p_attrval_qual(p):
    'attrval :  QUAL'
    p[0]="QUAL(%s)" % p

def p_attrval_node(p):
    'attrval : NODE'
#    print "CHECK5 NODEREF %s" % p[1]
    p[0]="NodeRef(%s)" % p[1]


def p_attrval_FILE(p):
    'attrval : BUILTIN_FILE'
    p[0]= "FILE(%s)" % p[1]

def p_attrval_float(p):
    'attrval : FLOAT'
    p[0]="FLOAT(%s)" % p


# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input! %s" % p

# Build the parser
parser = yacc.yacc()

#   result = parser.parse(s)
