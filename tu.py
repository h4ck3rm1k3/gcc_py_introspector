
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'PSEUDO_TMPL',
    'STRG',
    "NODE",
    "SPACE",
    "NTYPE",
    "ATTR",
    "BUILTIN_FILE",
    'SCOPE',
    "INTCONST",
    'HXX_FILE',
    'ARTIFICIAL',
    "C",
    'ERROR',
    'SIGNED',
    'LINK',
    'STRUCT',
    'ACC',
    'DTYPE',
    'MEMBER',
    'INTERNAL',
    'STRG2',
    'OP',

)
t_PSEUDO_TMPL='pseudo|tmpl'
t_DTYPE='long|int'
t_STRG  = r'strg:\s+.+\s+lngt:\s\d+'
#t_STRG2 = r'.+\s+lngt:\s\d+?'
t_C='c |C '
t_NODE= r'\@\d+'
t_SPACE= r'\s+'
t_ERROR = 'error_mark'
t_NTYPE = r'[a-z_]+_(cst|decl|expr)|identifier_node|tree_list|tree_vec|int_type'
t_ATTR =  r'(cls|spcs|hdlr|then|else|alis|inst|spec|orig|body|link|accs|bpos|argt|name|scpe|low|high|tag|flds|low|ptd|mngl|args|purp|link|valu|chan|fncs|binf|vfld|prec|sign|min|max|srcp|lngt|lang|dcls|type|elts|domn|qual|retn|prms|clas|unql|nst|rslt|sts|srcp|note|chain|bases|refd|base|init|size|algn|used|OP\d+)\s?:'
t_BUILTIN_FILE = r'\<built\-in\>:0'
t_HXX_FILE = r'[\-\+A-Za-z_\-0-9]+(\.(h|hdl|txx|tcc|hpp|cxx|hxx))?:\d+'
t_SIGNED = 'signed|unsigned'
t_SCOPE = r'\:\:'
t_INTCONST = r'(\-)?\d+'
t_ARTIFICIAL = 'artificial'
t_LINK = 'static|undefined|extern'
t_ACC='pub|priv|prot'
t_STRUCT = 'struct'
t_MEMBER = 'constructor|member|destructor|binfo|pure|virt|mutable|bitfield|ptrmem'

t_OP='operator\s+(assign|xor|rshift|lshift|new|or|delete|and|eq|ne|call|lt|vecdelete|spec)'
t_INTERNAL='\*INTERNAL\*'

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

lex.lex()
import sys
fd = open(sys.argv[1])
import re


line =""

def parse_l(l):
    stack = []
    
    x=re.search(r'\s([0-9]+)\s+:\s\@',l)
    while(x):
        n= x.group(1)
        #print ("Find %s in %s" % (n,l))
        l = re.sub(r'\s%s\s+:\s\@' % n," OP%s :@" % n,l)
        x=re.search(r'\s([0-9]+)\s+:\s\@',l)

    try :


        lex.input(l)

        for tok in iter(lex.token, None):
            ptype= repr(tok.type)
            pval = repr(tok.value)
            stack.append([ptype,pval])

    except Exception, exp:
        print ptype, pval
        print l
        print exp
        print stack
        raise exp

for l in fd.readlines():

    if l[0]=='@'  :
        parse_l(line)
        line =""
    else:
        line = line + l    

fd.close()     


