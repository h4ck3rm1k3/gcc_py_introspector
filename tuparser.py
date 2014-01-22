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
    psr_val[0] = tuast.String(psr_val[1])


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
