#!/usr/bin/python

import yaml
import data.body2
import types
import pprint

from ast import *

#print yaml.dump(deep)

# tmap = {
#     'function_decl':'FunctionDef',
#     'identifier_node':'Name',
#     'bind_expr':'Assign',
#     'var_decl':'Assign',
#     #'var_decl':'Assign',    
# }

def addr_expr(**kwargs) :
    pass
def array_type(**kwargs) :
    pass
def bind_expr(**kwargs):
    pass
def call_expr(**kwargs):
    pass
def component_ref(**kwargs):
    pass
def cond_expr(**kwargs):
    pass
def decl_expr(**kwargs):
    pass
def eq_expr(**kwargs):
    pass
def field_decl(**kwargs):
    pass
def function_decl(**kwargs):
    pass

def identifier_node(**kwargs):
    if 'fld:string' in kwargs:
        return Name(kwargs['fld:string'])
    else:
        pprint.pprint ({'no string':kwargs})

def integer_cst(**kwargs):
    pass
def integer_type(**kwargs):
    pass
def modify_expr(**kwargs):
    pass
def ne_expr(**kwargs):
    pass
def nop_expr(**kwargs):
    pass
def pointer_type(**kwargs):
    pass
def result_decl(**kwargs):
    pass
def return_expr(**kwargs):
    pass
def statement_list(**kwargs):
    pass
def string_cst(**kwargs):
    pass
def truth_andif_expr(**kwargs):
    pass
def var_decl(**kwargs):
    pass
def void_type(**kwargs):
    pass
_lookup = globals()

def lookup(x):
    if x in _lookup:
        f = _lookup[x]
    elif "_" + x  in _lookup:
        f = _lookup['_' + x]
    return f

# arguments
# Assign
# Call
# Compare
# Eq
# Expr
# If
# Load
# Module
# Name
# Num
# Store
# Str

def decl_expr(**kwargs):
    pass
of = {}

def rec(x,i=0):
    t = "Unknown"
    indent = i * "  "

    if 'rdf:type' in x:
        if  x['rdf:type']:
            t = x['rdf:type']
            t = t.replace('node:','')
            #if t not in f: # seen
            #    f[t]='ntype'
        else:
            #pprint.pprint(x)
            pass
        del x['rdf:type'] # get rid of this

    f = lookup(t)
    
    #body = t + "("
    attrs = {}
    #subobj = []   
    for l in x:
        n = l #.replace('fld:type','ftype')
        v = x[l]
        if type(v) is types.DictType:
            v2 = rec(v,i+1)
            attrs[n] = v2

                        
        elif type(v) in types.StringTypes:
            if n in ('ntype','type','scpe','chain'):
                pass
            elif v =='':
                pass
            else:
                if 'link:' in v:
                    v= v.replace('link:','')
            attrs[n] = v
    attrs['rdf:type']=t
    pprint.pprint(attrs)
    return f(**attrs)


print rec(data.body2.deep)

#for x in f:
#    print "def %s(**kwargs):\n                pass" % x
