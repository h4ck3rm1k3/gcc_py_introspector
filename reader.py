'''
reader module
'''

import sys
import re
import traceback
from tu import lex
from tuparser import parser
OPRE = r'op\s([0-9]+)\s*:\s\@'
ERE = r'\s([0-9]+)\s+:\s\@'
vals = {}

seen = {} 

def parse_l(l, debug):
    '''
    preprocessing of the line
    '''

    pval = None
    ptype = None
    if not l:
        raise Exception()
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
        print "LEX ERROR %s %s" % (ptype, pval)
        print l
        print exp
        print stack
        # raise exp

    if debug:
        print "Line %s" % l

    try:
        x = parser.parse(l, debug=debug)
        if not x:
            print "Line:%s" % l
            print "Stack:%s" % stack
            print "parser %s" % parser

            if not debug:
                x = parser.parse(l, debug=True)

        else:
            if debug:
                print("Results1 %s" % x)
            else:
                s = str(x)
                if not s in seen:
                    seen[s]=1
                    print("Results2 '%s'" % s)


    except Exception as exp:
        traceback.print_exc()
        print exp
        print "EXP Line:%s" % l
        print "EXP Stack:%s" % stack


def main():
    fd = open(sys.argv[1])
    if len(sys.argv) > 2:
        debug = True
    else:
        debug = False

    line = ""
    for l in fd.readlines():
        l = l.strip()
        if l[0] == '@':
            if line:
                parse_l(line, debug)
            line = l
        else:
            line = line + " " + l
    fd.close()

try:
    main()
except Exception as e:
    print "error %s" % e

#import pprint
#pprint.pprint(vals)
print "\n".join(sorted(seen.keys()))
