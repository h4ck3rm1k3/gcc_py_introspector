'''
lexer
'''
  # import pprint
import ply.lex as lex
  # import ply.yacc as yacc
from ply.lex import TOKEN
import pprint
DEBUG = 0

states = (
    ('str','exclusive'),
    ('len','exclusive'),
    ('adr','exclusive'),
)

tokens = [
    'ATTR_OP',
    'ATTR_En',
    'OP0_ATTR',
    'OP1_ATTR',
    'TYPE_ATTR',
    'ADDR_ATTR',
    'ADDR_EXPR',
    'SPEC_ATTR',
    'SPEC_VALU',
    'CONSTRUCTOR',
    'QUAL',
    'FLOAT',
    'PSEUDO_TMPL',
    'STRG',
    'STRGLEN',
    "NODE",
    'SPEC',
    "BUILTIN_FILE",
    'HXX_FILE',
    'ARTIFICIAL',
    'LANG',
    'SIGNED',
    'LINK',
    'STRUCT',
    'ACC',
    'MEMBER',
    'NOTE',
    'SOMESTRG', # catchall
    'SOMEINT', # int
    'HEXVAL',
    'NTYPE_IDENTIFIER_NODE',

#    'R'
]


def make_re(tstr):
    '''
    create a regex like a|b|c
    '''
    items = [
        x.strip().rstrip() for x in tstr.split()
    ]
    newre = r'(%s)' % '|'.join(items)
    # print newre
    return newre

import sys

# create parser rules
def create_rules(tstr):
    for token in tstr.split():
        token = token.upper()
        func = lambda x: x
        rule = "ntype : %s" % token
        func.__doc__ = rule
        current_module = sys.modules[__name__]
        name = "p_%s" % (token.lower())
        #print "name %s(psr_val):\n    \'%s\'\n    return ntype_base(psr_val)\n" %(name, rule)
        setattr(current_module, name , func)


def emit_parser_rule(base_name, prefix):
    # parser
    rule = "%s_type : %s" % (prefix, base_name)
    parser_name = "p_%s" % (base_name.lower())
    #print "def %s(psr_val):\n    \'%s\'\n    psr_val[0] = %s_base(psr_val)\n" %(parser_name, rule, prefix)

def make_tokens(prefix,pattern,val_func, tstr):
    '''
    create tokens
    * prefix for the token name
    * pattern to create for each token with one %s
    * val_fun to process the data
    * tstr for the tokens

    '''
    for x in tstr.split():
        item = x.strip().rstrip()
        regex = pattern % item
        func = lambda x : val_func(x)
        func.regex = regex
        func.node = x
        func.prefix = prefix
        func.pattern = pattern
        func.val_func = val_func
                
        func.__doc__ = "check %s" % x
        current_module = sys.modules[__name__]
        base_name = "%s_%s" % (prefix, item.upper())
        name = "t_%s" % (base_name)
        tokens.append(base_name)
        emit_parser_rule(base_name, prefix)


        setattr(current_module, name , func)
        if DEBUG:
            print "created name %s regex %s"  %( name, regex )
            print "basename %s"  %( base_name )
            pprint.pprint({
             'm': current_module,
             'n': name ,
             'f' : func,
             'r' : func.__dict__,
             'f2' : func.val_func.__dict__,
             'f2d' : func.val_func.__doc__,
             'node' : func.node,
             'fd' : func.__doc__
         })

def ntype_value(tok) :
    return tok 

def t_NTYPE_IDENTIFIER_NODE(tok):
    r'identifier_node'
    return tok

# the following are node types
make_tokens("NTYPE", "(?P<val>%s)",ntype_value,"""
aggr_init_expr
alignof_expr
array_ref
array_type
arrow_expr
baselink
bind_expr
binfo
bit_and_expr
bit_ior_expr
bit_not_expr
bit_xor_expr
boolean_type
bound_template_template_parm
break_stmt
call_expr
case_label_expr
cast_expr
complex_type
component_ref
compound_expr
convert_expr
cond_expr
const_cast_expr
const_decl
continue_stmt
ctor_initializer
decl_expr
decltype_type
dl_expr
do_stmt
dotstar_expr
dynamic_cast_expr
enumeral_type
eq_expr
error_mark
expr_stmt
field_decl
for_stmt
function_decl
function_type
ge_expr
goto_expr
gt_expr
handler
if_stmt
indirect_ref
integer_cst
integer_type
label_decl
lang_type
le_expr
lshift_expr
lt_expr
label_expr
member_ref
mem_ref
method_type
minus_expr
modop_expr
modify_expr
mult_expr
namespace_decl
ne_expr
negate_expr
nop_expr
nw_expr
offset_type
overload
parm_decl
plus_expr
pointer_type
pointer_plus_expr
postdecrement_expr
postincrement_expr
predecrement_expr
preincrement_expr
ptrmem_cst
real_cst
real_type
result_decl
record_type
reference_type
reinterpret_cast_expr
return_expr
rshift_expr
scope_ref
sizeof_expr
statement_list
static_cast_expr
string_cst
switch_stmt
switch_expr
tag_defn
target_expr
template_decl
template_id_expr
template_parm_index
template_template_parm
template_type_parm
throw_expr
trait_expr
translation_unit_decl
tree_list
tree_vec
trunc_div_expr
trunc_mod_expr
truth_and_expr
truth_andif_expr
truth_not_expr
truth_orif_expr
try_block
type_decl
typeid_expr
typename_type
typeof_type
union_type
using_decl
using_stmt
var_decl
vector_type
void_type
while_stmt
""")


t_PSEUDO_TMPL = 'pseudo|tmpl'
#t_DTYPE = 'long|int'

# can be used as a node type or a note
t_CONSTRUCTOR = 'constructor'


def t_STRG(tok):
    r'strg:\s+'
    print 'enter str state'
    tok.lexer.begin('str')  # begin the string group
    #strval = tok.lexer.lexmatch.group("val")
    #strlen = int(tok.lexer.lexmatch.group("len"))
    #print "String start %s" % strval 
    #tok.value = strval # only take the first n chars given by the len 
    return tok


def t_STRGLEN(tok):
    r'lngt:\s*'  # (?P<len>\d+)
    tok.lexer.begin('len')  # begin the string group
    print 'len token'
    #strval = tok.lexer.lexmatch.group("val")
    #strlen = int(tok.lexer.lexmatch.group("len"))
    #print "StringLen: '%d'" % strlen 
    #print "String:" + strval + ";Length:" + str(strlen)
    #tok.value = strlen
    return tok


t_LANG = r'C\s'
#t_R = r'\sr\s'


def t_QUAL(tok):
    r'c\s|v\s|cv\s|r\s'
    strval = tok.value
    #print ("QUAL:%s" % strval)
    #tok.value = strval
    return tok


def t_NODE(tok):
    r'\@(?P<val>\d+)'
    #print "Match %s" % (tok.lexer.lexmatch)
    strval = tok.lexer.lexmatch.group("val")
    #print ("NODEID:%s" % strval)
    #y =0

    # for x in tok.lexer.lexmatch.groups():
    #     y = y + 1
    #     print ("test:%d %s" % (y, x))

    tok.value = strval
    return tok


def t_SPACE(tok):
    r'\s+'
    pass

#t_ERROR = 'error_mark'


@TOKEN(r'(?P<val>addr_expr)\s?')
def t_ADDR_EXPR(tok) :
    tok.value = str(tok.lexer.lexmatch.group("val"))
    #print("NTYPE ADDR EXPR %s " % tok.value)
    return tok

def t_OP0_ATTR(tok):
    r'(?P<val>OP0)\s*:'
    #count_non_null(tok)
    tok.value = str(tok.lexer.lexmatch.group("val"))
    #print("OP0_ATTR %s " % tok.value)
    return tok

def t_OP1_ATTR(tok):
    r'(?P<val>OP1)\s*:'
    tok.value = str(tok.lexer.lexmatch.group("val"))
    return tok

def t_TYPE_ATTR(tok):
    r'type\s*:'
    tok.value = 'type'
    #print("TYPE_ATTR:%s" % tok.value)
    return tok

# attributes like 'address: 5fa31238843838' in the newer compilers
def t_ADDR_ATTR(tok):
    r'addr\s*:\s*'
    tok.lexer.begin('adr')  # begin the string group
    tok.value = 'addr'
    print("ADDR_ATTR:%s" % tok.value)
    return tok


def t_ATTR_En(tok):
    '''(%s|E\d+)\s*:'''
    tok.value = tok.value.replace(" :","")
    return tok

def count_non_null(tok):
    count = 0 
    for v in tok.lexer.lexmatch.groups():
        if v is not None :
            print "check %s %d"  % (v, count)
        count = count + 1

def t_ATTR_OP(tok):
    '''(?P<val>OP\d+)\s*:'''
    # count_non_null(tok)
    tok.value = tok.lexer.lexmatch.group("val")
    #print("ATTR:%s" % tok.value)
    #print("OPATTR:%s" % tok.value)
    return tok



def attr_val(tok):

    val = None
    #print("IN ATTR:%s" % tok.value)
    #print("UNMATCHED ATTR:%s" % tok.value)
    tok.value = tok.value.replace(":","")
    tok.value = tok.value.replace(" ","")
    return tok

# removing lngt
# this next call creates tokens for the following fields
# each field can be used to give a new key value pair to a node
# the field name is used to construct a function for recieving it.
make_tokens("ATTR", "(?P<val>%s)\s*:",attr_val, '''
accs
algn
alis
args
argt
base
bases
binf
body
bpos
chain
chan
clas
clnp
cls
cnst
cond
crnt
csts
ctor
dcls
decl
domn
else
elts
expr
flds
fn
fncs
hdlr
high
init
idx
inst
lang
labl
line
link
low
max
mbr
min
mngl
name
nmsp
note
nst
orig
parm
prec
prms
ptd
purp
qual
refd
retn
rslt
scpe
sign
size
spcs
srcp
sts
tag
then
unql
used
val
vars
valu
vfld
''')

def t_SPEC_ATTR(tok):
    '''
    spec attr
    '''
    strval = tok.lexer.lexmatch.group("val")
    tok.value = strval
    # print "SPEC_ATTR:%s(%s)" % (t.type, strval)
    return tok

t_SPEC_ATTR.__doc__ = r'(?P<val>%s)\s*:' % make_re('spec')

t_BUILTIN_FILE = r'\<built\-in\>:0'
t_HXX_FILE = r'(yes_no_type.hpp|' + \
             r'[\-\+A-Za-z_\-0-9]+(\.(h|hdl|c|txx|tcc|hpp|cpp|cxx|hxx|pb\.h|pb\.c))?):\d+'
t_SIGNED = 'signed|unsigned'
#t_SCOPE = r'\:\:'
#t_INTCONST = r'(\-)?\d+'
#t_FLOAT = r'[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?'
t_ARTIFICIAL = r'artificial'
t_LINK = r'static|undefined|extern'
t_ACC = r'pub|priv|prot'
t_STRUCT = r'struct|union'
t_MEMBER = r'member|destructor|binfo|ptrmem'
t_NOTE = r'operator|conversion'
t_SPEC = r'spec\s'
t_SPEC_VALU = r'mutable|bitfield|pure|virt'


def op_token_value(tok) :
    '''
    OP token
    '''
    strval = tok.lexer.lexmatch.group("val")
    tok.value = strval
    # print "OP%s" % strval
    return tok

# sub state tokens
@TOKEN(r'(?P<hexval>[0-9a-f]+)')
def t_adr_HEXVAL(tok) :
    tok.value = int(tok.lexer.lexmatch.group("hexval"),16)
    print("hexval %s " % tok.value)
    return tok

def t_str_SOMESTRG(tok):
    r'(?P<val>\w+)\s*' # some string
    strval = tok.lexer.lexmatch.group("val")
    print "String: '%s'" % strval 
    tok.value = strval
    return tok

def t_len_SOMEINT(tok):
    r'(?P<val>\d+)\s*' # some int
    strval = tok.lexer.lexmatch.group("val")
    print "INT: '%s'" % strval 
    tok.value = strval
    return tok

make_tokens("OPERATOR", r'operator\s+(?P<val>%s)\s',op_token_value,"""
    add
    and
    andassign
    addr
    assign
    call
    compound
    delete
    deref
    div
    divassign
    eq
    ge
    gt
    le
    lnot
    lshift
    lshiftassign
    lt
    minus
    minusassign
    mult
    multassign
    ne
    neg
    new
    or
    orassign
    plus
    plusassign
    postdec
    postinc
    predec
    preinc
    rshift
    vecdelete
    vecnew
    xor
    xorassign
    not
    pos
    ref
    rshiftassign
    subs
""")


def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value, ))

def t_str_error(t):
    raise TypeError("Unknown text '%s'" % (t.value, ))

def t_adr_error(t):
    raise TypeError("Unknown text '%s'" % (t.value, ))

def t_len_error(t):
    raise TypeError("Unknown text '%s'" % (t.value, ))

#g_lex = lex.lex(debug=1)
g_lex = lex.lex()

if __name__ == '__main__':
    g_lex.runmain()

#g_lex = lex.lex()
