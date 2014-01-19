import sys
import re
from tu import lex
from tuparser import parser
OPRE=r'op\s([0-9]+)\s*:\s\@'
ERE=r'\s([0-9]+)\s+:\s\@'
vals={}

def parse_l(l):
    '''
    preprocessing of the line
    '''
    global vals
    pval = None
    ptype= None
    if not l:
        raise Exception()
    if l[0]!='@':
        raise Exception()
    stack = []
    #array element 0
    x=re.search(ERE,l)
    while(x):
        n= x.group(1)
        #print ("Find %s in %s" % (n,l))
        l = re.sub(r'\s%s\s+:\s\@' % n," E%s :@" % n,l)
        x=re.search(ERE,l)
    # replace op 0
    x=re.search(OPRE,l)
    while(x):
        n= x.group(1)
        #print ("Find %s in %s" % (n,l))
        l = re.sub(r'op\s%s\s*:\s\@' % n," OP%s :@" % n,l)
        x=re.search(OPRE,l)
    try :
        lex.input(l)
        for tok in iter(lex.token, None):
            pval = repr(tok.value)
            ptype= repr(tok.type)
            if ptype not in vals:
                vals[ptype]={}
            vals[ptype][pval]=1
            stack.append(ptype) #,pval

    except Exception, exp:
        print "LEX ERROR %s %s" % (ptype, pval)
        print l
        print exp
        print stack
        #raise exp

    #print "Line %s" % l

    try:
        x = parser.parse(l) 
        if not x:
            print "Line:%s" % l
            print "Stack:%s" % stack
        else:
            #print ("Results %s" % x)
            pass

    except:
        print "Line:%s" % l

def main():
    fd = open(sys.argv[1])
    line =""
    for l in fd.readlines():
        l = l.strip()
        if l[0]=='@' :
            if (line):
                parse_l(line)
            line = l
        else:
            line = line +" "+ l
    fd.close()

try:
    main()
except Exception, e:
    print "error %s" % e

#pprint.pprint(vals)
