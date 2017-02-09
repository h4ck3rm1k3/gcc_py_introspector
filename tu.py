'''
lexer
'''

import ply.lex as lex
  # import ply.yacc as yacc
from ply.lex import TOKEN
import pprint2
DEBUG = 0
import sys
from attributes import token_rule
from utils import goto_state,  emit_parser_rule

states = (
    ('str','exclusive'),
    ('sign','exclusive'), # main attribute
    ('len','exclusive'),
    ('prec','exclusive'),
    ('algn','exclusive'),
    ('adr','exclusive'),
#    ('type','exclusive'),
)

tokens = [
    'LEN',
    'SPEC_REGISTER',
    'ATTR_ALGN',
    'ATTR_SIGN',
    'ATTR_PREC',
    'ATTR_OP',
    'ATTR_En',
    'OP0_ATTR',
    'OP1_ATTR',
    'TYPE_ATTR',
    'ADDR_ATTR',
    'ADDR_EXPR',
#    'ASM_EXPR',
#    'SAVE_EXPR',
#    'PREDICT_EXPR',
    'SPEC_ATTR',
    'SPEC_VALU',
    'CONSTRUCTOR',
    'QUAL',
#    'FLOAT',
#    'PSEUDO_TMPL',
    'STRG',
#    'STRGLEN',
    "NODE",
#    "TNODE",
#    'SPEC',
    "BUILTIN_FILE",
    'HXX_FILE',
    'ARTIFICIAL',
#    'LANG',
    'SIGNED',
    'LINK',
    'STRUCT',
#    'ACC',
    'MEMBER',
#    'NOTE',
    'SOMESTRG', # catchall
    'SOMEINT', # int
    'SOMEINT2', # int
    'SOMEHEX2', # int
    'SOMEHEX3', # int
    'SOMEHEX4', # int
    'HEXVAL',
    'NTYPE_IDENTIFIER_NODE',
    # special names
 #   'LONG',
    'INT',
 #   'UNSIGNED',
#    'STRGLEN2'
]

@token_rule
def attr_val(tok):

    val = None
    #print("IN ATTR:%s" % tok.value)
    #print("UNMATCHED ATTR:%s" % tok.value)
    tok.value = tok.value.replace(":","")
    tok.value = tok.value.replace(" ","")
    return tok

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
            #print "created name %s regex %s"  %( name, regex )
            #print "basename %s"  %( base_name )
            pprint2.pprint({
             'm': current_module,
             'n': name ,
             'f' : func,
             'r' : func.__dict__,
             'f2' : func.val_func.__dict__,
             'f2d' : func.val_func.__doc__,
             'node' : func.node,
             'fd' : func.__doc__
         })


@token_rule
def t_NTYPE_IDENTIFIER_NODE(tok):
    r'identifier_node'
    return tok

@token_rule
def t_NTYPE_SAVE_EXPR(tok):
    r'save_expr'
    return tok

# this is a generic rule for all generated rules
@token_rule
def ntype_value(tok) :
    return tok 

# the following are node types
make_tokens("NTYPE", "(?P<val>%s)",ntype_value,"""
aggr_init_expr
alignof_expr
asm_expr
save_expr
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
bit_field_ref
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
pointer_bounds_type
pointer_plus_expr
postdecrement_expr
postincrement_expr
predecrement_expr
preincrement_expr
predict_expr
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
truth_or_expr
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


#t_PSEUDO_TMPL = 'pseudo|tmpl'
#t_DTYPE = 'long|int'

# can be used as a node type or a note
t_CONSTRUCTOR = 'constructor'



@token_rule
def t_STRG(tok):
    r'strg:\s*'
    #print 'enter str state'
    goto_state(tok,'str')  # begin the string group
    #strval = tok.lexer.lexmatch.group("val")
    #strlen = int(tok.lexer.lexmatch.group("len"))
    #print "String start"
    #tok.value = strval # only take the first n chars given by the len 
    return tok


@token_rule
def t_LEN(tok): # constructor length
    r'lngt:\s*(\d+)'  # (?P<len>\d+)
    #goto_state(tok,'len')  # begin the string group
    #print 'constructor lngt: token'
    return tok


#t_LANG = r'C\s'
#t_R = r'\sr\s'



@token_rule
def t_QUAL(tok):
    r'c\s|v\s|cv\s|r\s'
    strval = tok.value
    #print ("QUAL:%s" % strval)
    #tok.value = strval
    return tok



@token_rule
def t_NODE(tok):
    r'\@(?P<val>\d+)(\s+|$)'
    #print "Match %s" % (tok.lexer.lexmatch)
    strval = tok.lexer.lexmatch.group("val")
    #print ("NODEID:%s" % strval)
    #y =0

    # for x in tok.lexer.lexmatch.groups():
    #     y = y + 1
    #     print ("test:%d %s" % (y, x))

    tok.value = strval
    return tok



@token_rule
def t_SPACE(tok):
    r'\s+'
    pass

#t_ERROR = 'error_mark'


@TOKEN(r'(?P<val>addr_expr)\s?')

@token_rule
def t_ADDR_EXPR(tok) :
    #tok.value = str(tok.lexer.lexmatch.group("val"))
    #tok.value = "SOMEADDR"
    #print("NTYPE ADDR EXPR %s " % tok.value)
    return tok


@token_rule
def t_OP0_ATTR(tok):
    r'(?P<val>OP0)\s*:'
    #count_non_null(tok)
    #tok.value = str(tok.lexer.lexmatch.group("val"))
    #tok.value = "SOMEADDR"
    print("OP0_ATTR %s " % tok.value)
    return tok


@token_rule
def t_OP1_ATTR(tok):
    r'(?P<val>OP1)\s*:'
    tok.value = str(tok.lexer.lexmatch.group("val"))
    return tok


# attributes like 'address: 5fa31238843838' in the newer compilers

@token_rule
def t_ADDR_ATTR(tok):
    r'addr\s*:\s*'
    #tok.value = 'addr'
    #print("entering ADDR_ATTR:%s" % tok.value)
    goto_state(tok,'adr')  # begin the string group
    return tok



@token_rule
def t_ATTR_En(tok):
    '(E\d+)\s*:'
    tok.value = tok.value.replace(" :","")
    return tok


@token_rule
def t_ATTR_OP(tok):
    '''(?P<val>OP\d+)\s*:'''
    # count_non_null(tok)
    tok.value = tok.lexer.lexmatch.group("val")
    #print("ATTR:%s" % tok.value)
    #print("OPATTR:%s" % tok.value)
    return tok


@token_rule
def t_ATTR_PREC(tok):
    r'prec\s*:\s*'
    tok.value = 'prec'
    #print("entering ADDR_PREC:%s" % tok.value)
    goto_state(tok,'prec')  # begin the string group
    return tok


@token_rule
def t_ATTR_ALGN(tok):
    r'algn\s*:\s*'
    tok.value = 'algn'
    #print("entering ADDR_ALGN:%s" % tok.value)
    goto_state(tok,'algn')  # begin the string group
    return tok


@token_rule
def t_ATTR_SIGN(tok):
    r'sign\s*:\s*'
    tok.value = 'sign'
    #print("entering ATTR_SIGN:%s" % tok.value)
    goto_state(tok,'sign') 
    return tok
        

@token_rule
def t_sign_SIGNED(tok):
    r'signed' #|unsigned
    #print 'found signed'
    goto_state(tok,'INITIAL')  # end the capture
    return tok


@token_rule
def t_SIGNED(tok):
    r'signed|unsigned'
    #print 'found signed'
    goto_state(tok,'INITIAL')  # end the capture
    return tok


#sign
#prec
#algn
# removing lngt
# this next call creates tokens for the following fields
# each field can be used to give a new key value pair to a node
# the field name is used to construct a function for recieving it.
#alis
make_tokens("ATTR", "(?P<val>%s)\s*:",attr_val, '''
accs
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
prms
ptd
purp
qual
refd
retn
rslt
scpe
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


@token_rule
def t_SPEC_ATTR(tok):
    r'spec:\s*'
    #strval = tok.lexer.lexmatch.group("val")
    #tok.value = strval
    # print "SPEC_ATTR:%s(%s)" % (t.type, strval)
    return tok



t_BUILTIN_FILE = r'\<built\-in\>:0'

@token_rule
def t_HXX_FILE(tok):
    r'(yes_no_type.hpp|[\-\+A-Za-z_\-0-9]+(\.(h|hdl|c|txx|tcc|hpp|cpp|cxx|hxx|pb\.h|pb\.c))?):\d+'
    #tok.value = "SOMEFILE" # strval
    return tok

#t_SCOPE = r'\:\:'
#t_INTCONST = r'(\-)?\d+'
#t_FLOAT = r'[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?'
t_ARTIFICIAL = r'artificial'
t_LINK = r'static|undefined|extern'
#t_ACC = r'pub|priv|prot'
t_STRUCT = r'struct|union'
t_MEMBER = r'member|destructor|binfo|ptrmem'
#t_NOTE = r'operator|conversion'
#t_SPEC = r'spec\s'
t_SPEC_VALU = r'mutable|bitfield|pure|virt'


def op_token_value(tok) :
    '''
    OP token
    '''
    strval = tok.lexer.lexmatch.group("val")
    tok.value = strval
    # print "OP%s" % strval
    return tok


@token_rule
def t_adr_HEXVAL(tok) :
    '(?P<hexval>[0-9a-f]+)(\s|$)'
    #tok.value = "HEXVAL" #int(tok.lexer.lexmatch.group("hexval"),16)
    #print("hexval1 %s " % tok.value)
    goto_state(tok,'INITIAL')
    return tok

# ## string values

@token_rule
def t_INT(tok):
    r'int:\s+'
    return tok




@token_rule
def t_str_SOMESTRG(tok):
    r'(?P<val>.+\s*)(lngt:\s*(\d+)\s*|$)' # some string
    #strval = tok.lexer.lexmatch.group("val")
    #print "String: '%s'" % strval 
    #tok.value = "SOMESTR" # strval
    goto_state(tok,'INITIAL')  # begin the string group
    return tok


@token_rule
def t_prec_algn_len_SOMEINT(tok):
    r'(?P<val>\d+)\s*' # some int
    strval = tok.lexer.lexmatch.group("val")
    #print "INT: '%s'" % strval 
    #tok.value = strval
    #tok.value = "SOMEINT"
    goto_state(tok,'INITIAL')
    return tok


######################################################################
# type goes into a special state with 

@token_rule
def t_TYPE_ATTR(tok):
    r'type\s*:\s*'
    #goto_state(tok,'type')
    #print("begin TYPE_ATTR: '%s'" % tok.value)
    tok.value = 'type'
    return tok



@token_rule
def t_SPEC_REGISTER(t):
    r'register'
    return t


@token_rule
def t_SOMEINT2(tok):
    r'(?P<val>(0x)?\-?\d+)\s+' # some int
    strval = tok.lexer.lexmatch.group("val")
    #print "INT const: '%s'" % strval 
    #tok.value = strval
    #tok.value = "SOMEINT"
    return tok


@token_rule
def t_adr_SOMEHEX2(tok):
    r'(?P<val>0x[0-9a-h]+)(\s|$)' # some int
    strval = tok.lexer.lexmatch.group("val")
    #print "HEX2 const: '%s'" % strval 
    #tok.value = "SOMEHEX2"
    return tok


@token_rule
def t_SOMEHEX2(tok):
    r'(?P<val>0x[0-9a-h]+)(\s|$)' # some int
    strval = tok.lexer.lexmatch.group("val")
    #print "HEX2 const: '%s'" % strval 
    tok.value = strval
    #tok.value = "SOMEHEX2b"
    return tok


@token_rule
def t_adr_SOMEHEX3(tok):
    r'(?P<val>[0-9a-h]+)(\s|$)' # some int
    strval = tok.lexer.lexmatch.group("val")
    #print "HEX3 const: '%s'" % strval 
    tok.value = strval
    #tok.value = "SOMEHEX3"
    return tok


@token_rule
def t_adr_SOMEHEX4(tok):
    r'(?P<val>[0-9a-h]+)(\s|$)' # some hex
    strval = tok.lexer.lexmatch.group("val")
    #print "HEX4 const: '%s'" % strval 
    tok.value = strval
    #tok.value = "SOMEHEX4"
    return tok


@token_rule
def t_SOMEHEX4(tok):
    r'(?P<val>[0-9a-h]+)(\s|$)' # some hex
    strval = tok.lexer.lexmatch.group("val")
    #print "HEX4 const: '%s'" % strval 
    tok.value = strval
    #tok.value = "SOMEHEX4b"
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



@token_rule
def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value, ))


@token_rule
def t_str_error(t):
    raise TypeError("Unknown str text '%s'" % (t.value, ))


@token_rule
def t_prec_error(t):
    raise TypeError("Unknown prec text '%s'" % (t.value, ))


@token_rule
def t_adr_error(t):
    raise TypeError("Unknown adr text '%s'" % (t.value, ))


@token_rule
def t_len_error(t):
    raise TypeError("Unknown len text '%s'" % (t.value, ))


@token_rule
def t_algn_error(t):
    raise TypeError("Unknown len text '%s'" % (t.value, ))


@token_rule
def t_sign_error(t):
    raise TypeError("Unknown sign text '%s'" % (t.value, ))


#g_lex = lex.lex(debug=1)
g_lex = lex.lex()

if __name__ == '__main__':
    g_lex.runmain()

#g_lex = lex.lex()
