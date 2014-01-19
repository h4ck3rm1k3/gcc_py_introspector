'''
lexer
'''
import pprint
import ply.lex as lex
import ply.yacc as yacc

def make_re(s):
    '''
    create a regex like a|b|c
    '''
    items = [
        x.strip().rstrip() for x in s.split()
    ]
    newre= r'(%s)' % '|'.join(items)
    #print newre
    return newre

NTYPES = """
addr_expr
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
gt_expr
handler
identifier_node
if_stmt
indirect_ref
integer_cst
integer_type
label_decl
lang_type
le_expr
lshift_expr
lt_expr
member_ref
method_type
minus_expr
modop_expr
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
postdecrement_expr
postincrement_expr
predecrement_expr
preincrement_expr
ptrmem_cst
real_cst
real_type
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
"""

t_NTYPE = r'%s\s?' % make_re(NTYPES)
#print(t_NTYPE)

tokens = (
    'CONSTRUCTOR',
    'QUAL',
    'FLOAT',
    'PSEUDO_TMPL',
    'STRG',
    "NODE",
    "SPACE",
    'SPEC',
    "NTYPE",
    "ATTR",
    "BUILTIN_FILE",
    'SCOPE',
    "INTCONST",
    'HXX_FILE',
    'ARTIFICIAL',
    'LANG',
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
    'NOTE',
    'R'
)
t_PSEUDO_TMPL='pseudo|tmpl'
t_DTYPE='long|int'


# can be used as a node type or a note
t_CONSTRUCTOR = 'constructor'

def t_STRG(t):
    r'strg:\s+(.+)\s+lngt:\s\d+'
    strval = t.lexer.lexmatch.group(2)
    #print ("CHECK:%s" % strval)
    t.value = strval
    return t

#t_STRG2 = r'.+\s+lngt:\s\d+?'
t_QUAL=  r'c\s|v\s|cv\s|r\s'
t_LANG=  r'C\s'
t_R=  r'\sr\s'

def t_NODE(t):
    r'\@(\d+)'
    strval = t.lexer.lexmatch.group(4)
    #print ("NODEID:%s" % strval)
    t.value = strval
    return t

def t_SPACE(t):
    r'\s+'
    pass

t_ERROR = 'error_mark'
#try_block|scope_ref|component_ref|indirect_ref|template_type_parm|template_parm_index|[a-z_]+_(cst|decl|expr|type|stmt)|identifier_node|tree_list|tree_vec|statement_list)\s?'

#FIELDS
FIELD='''
cnst
csts
clnp
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
cls
crnt
cond
dcls
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
inst
lang
line
link
lngt
low
max
min
mngl
name
note
nst
orig
prec
prms
parm
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
spec
srcp
sts
tag
then
type
unql
used
valu
vfld
mbr
addr
csts
ctor
decl
nmsp
val
'''
def t_ATTR(t):
    strval = t.lexer.lexmatch.group(7)
    t.value = strval
    #print "FIELD chec:%s" % (t.lexer.lexmatch.groups())
    #    print "FIELD:%s(%s)" % (t.type, strval)
    return t

FIELD_STR = r'%s\s?' %  make_re(FIELD)
t_ATTR.__doc__=r'(%s|E\d+|OP\d+)\s*:' % FIELD_STR


t_BUILTIN_FILE = r'\<built\-in\>:0'
t_HXX_FILE = r'(yes_no_type.hpp|[\-\+A-Za-z_\-0-9]+(\.(h|hdl|txx|tcc|hpp|cxx|hxx))?):\d+'
t_SIGNED = 'signed|unsigned'
t_SCOPE = r'\:\:'
t_INTCONST = r'(\-)?\d+'
t_FLOAT=r'[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?'
t_ARTIFICIAL = 'artificial'
t_LINK = 'static|undefined|extern'
t_ACC='pub|priv|prot|bitfield'
t_STRUCT = 'struct|union'
t_MEMBER = 'constructor|member|destructor|binfo|pure|virt|mutable|ptrmem'
t_NOTE= 'operator|conversion'
t_SPEC='spec'

#OPERATORS

def t_OP(t):
    strval = t.lexer.lexmatch.group(2)
    t.value = strval
    #print "OP%s" % strval
    return t
t_OP.__doc__='operator\s+(%s)\s' % (
    make_re('''
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
    '''))


t_INTERNAL='\*INTERNAL\*'
#spec: pure spec: virt

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

lex.lex()



