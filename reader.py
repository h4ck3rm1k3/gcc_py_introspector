'''
reader module
'''

import sys
import re
import traceback
from tu import lex
from tuparser import parser
import pprint

OPRE = r'op\s([0-9]+)\s*:\s\@'
ERE = r'\s([0-9]+)\s+:\s\@'
vals = {}
seen = {} 

deps = {}

def report(x,l):
    #print("Results1 %s -> %s | %s" % (x.node_id, x.keys(),l))
    assert(x)
    k = x.keys()
    assert(k)
#    print l
    #print k
#    pprint.pprint(x.__dict__)
    deps[x.node_id]=k



def lex(l, debug, error_file):
    """
    try and lex the input
    this function was removed, it is used to test the lexer.
    """
    try:
        lex.input(l)
        for tok in iter(lex.token, None):
            pval = repr(tok.value)
            ptype = repr(tok.type)
            if ptype not in vals:
                vals[ptype] = {}
            vals[ptype][pval] = 1
            stack.append(ptype)  # ,pval

    except Exception as exp:
        error_file.write(l + "\n")
        print "LEX ERROR1 %s %s" % (ptype, pval)
        print l
        print exp
        print stack
        # raise exp
    if debug:
        print "Line %s" % l

def parse_l(l, debug, error_file):
    '''
    preprocessing of the line
    '''

    pval = None
    ptype = None

    # if the line is empty
    if not l:
        raise Exception()
    # or does not start with @ 
    if l[0] != '@':
        raise Exception()

    stack = []

    # array element 0
    x = re.search(ERE, l)
    while x:
        n = x.group(1)
        # print ("Find %s in %s" % (n,l))
        l = re.sub(r'\s%s\s+:\s\@' % n, " E%s :@" % n, l)
        x = re.search(ERE, l)

    # replace op 0
    x = re.search(OPRE, l)
    while x:
        n = x.group(1)
        # print ("Find %s in %s" % (n,l))
        l = re.sub(r'op\s%s\s*:\s\@' % n, " OP%s :@" % n, l)
        x = re.search(OPRE, l)

    # now try and parse the input
    try:
        x = parser.parse(l, debug=debug)
        
        if not x:
            error_file.write(l + "\n")
            print "Error on Line:%s" % l
            #print "Stack:%s" % stack
            #print "parser %s" % parser
            #if not debug:
            #    x = parser.parse(l, debug=True)
        else:
            report(x,l)
            if debug:
                print("Results1 %s" % x)
            else:
                s = str(x)
                if not s in seen:
                    seen[s]=1
                    if debug:
                        print("Results2 '%s'" % s)

        if debug :
            print "Stack:%s" % stack
            print "parser %s" % parser

    except Exception as exp:
        print "parse error : "+ l + "\n"
        error_file.write(l + "\n")
        traceback.print_exc()
        print exp
        print "EXP Line:%s" % l
        print "EXP Stack:%s" % stack
    
    #print "Stack:%s" % stack


def main():
    """
    Reader for a tu file
    """
    fd = open(sys.argv[1])

    # open the error file in case there are any errors they will be written here.
    error_file = open(sys.argv[1] + ".err", "w")
    if len(sys.argv) > 2:
        debug = True
    else:
        debug = False

    line = ""
    for l in fd.readlines():
        l = l.strip()
        if len(l) <= 0  :
            continue

        if l[0] == '@':
            if line:
                parse_l(line, debug, error_file)
            line = l
        else:
            line = line + " " + l
    fd.close()

    if line:
        parse_l(line, debug, error_file)

try:
    main()
except Exception as e:
    print "error %s" % e

print "data=%s" % pprint.pformat(deps)

#print "\n".join(sorted(seen.keys()))



