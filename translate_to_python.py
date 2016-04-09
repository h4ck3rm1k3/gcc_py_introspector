#!/usr/bin/python

import yaml
import data.body2
import types
import pprint
import sys
from ast import *

def get_args(args):
    arg_list =[]
    for e in range(0,20):
        n = "fld:E"+str(e)
        if n in args:
            arg_list.append(args[n])
        else:            
            return arg_list


class VoidType:
    pass

class IntType:
    pass

def addr_expr(**kwargs) :

    if 'fld:type' in kwargs:
        return kwargs['fld:type']
    elif 'fld:OP0' in kwargs:
        return kwargs['fld:OP0']
    else:
        return kwargs

class ArrayType:
    pass

def array_type(**kwargs) :
    return ArrayType()

def bind_expr(**kwargs):
    # a list of times, the name contains the return object... may need to use that.
    return kwargs['fld:body']

    
def call_expr(**kwargs):
    
    return Call(
        func=kwargs['fld:fn'],
        args=get_args(kwargs), # TODO
        keywords=[],
        starargs=[],
        kwargs=[]
    )

def component_ref(**kwargs):
    return Subscript(
        value=kwargs['fld:OP0'],
        slice=kwargs['fld:OP1'],
    )

def cond_expr(**kwargs):
    return If(
        test=kwargs['fld:OP0'],
        body=kwargs['fld:OP1'],
        orelse=None,
        )


def decl_expr(**kwargs):
    pass
def eq_expr(**kwargs):
    return Compare(
        left=kwargs['fld:OP0'],
        ops=[Eq()],
        comparators=[
            kwargs['fld:OP1']
            ]
        )

class FieldDecl:
    def __init__(self, args):
        self.args=args

def field_decl(**kwargs):
    return FieldDecl(kwargs)

class FunctionRef:
    """
    for functions with undefined bodies, we use this class to mark them.
    """
    def __init__(self, name):
        self.name=name
        
def function_decl(**kwargs):
    if kwargs['fld:body'] != 'undefined':
        return FunctionDef(
            name=str(kwargs['fld:name']),
            args=[], # TODO
            body=kwargs['fld:body'],
            decorator_list=[],
            returns=None)
    else:
        return FunctionRef(str(kwargs['fld:name']))

class NameWrapper:
    def __init__(self, id):
        self._id=id
    def __str__(self):
        return self._id
        
def identifier_node(**kwargs):
    if 'fld:string' in kwargs:
        return NameWrapper(
            id=kwargs['fld:string']
        )
    else:
        #pprint.pprint ({'no string':kwargs})
        pass

def integer_cst(**kwargs):
    return Num(kwargs['fld:low'])

def integer_type(**kwargs):
    return IntType()

def modify_expr(**kwargs):
    return Assign(
        targets=[
            kwargs['fld:OP0']
        ],
        value=kwargs['fld:OP1']
    ),
    
    
def ne_expr(**kwargs):
    if 'fld:OP0' in kwargs:
        return Compare(
            left=kwargs['fld:OP0'],
            ops=[NotEq()],
            comparators=[
                kwargs['fld:OP1']
            ]
        )
    else:
        #pprint.pprint(kwargs)
        raise kwargs

class NopExpr:
    def __init__(self, args):
        self.args=args

def nop_expr(**kwargs):
    return NopExpr(kwargs)

class PointerType:
    pass

def pointer_type(**kwargs):
    return PointerType()

class ResultDecl:
    def __init__(self, args):
        self.args=args

def result_decl(**kwargs):
    return ResultDecl(kwargs)

def get_value(t):
    if isinstance(t, Assign):
        return t.value
        #pprint.pprint({"check" : t.__dict__})
    
def return_expr(**kwargs):
    #pprint.pprint({"Return Expr" : kwargs['fld:expr'][0].__dict__})
    return Return(get_value(kwargs['fld:expr'][0]))

def statement_list(**kwargs):
    return get_args(kwargs)

def string_cst(**kwargs):
    return Str(kwargs['fld:string'])

def truth_andif_expr(**kwargs):

    return BoolOp(
            values=[kwargs['fld:OP0']],
            op=And(),
            comparators=[
                kwargs['fld:OP1']
            ]
        )


class VarDecl:
    def __init__(self, args):
        self.name=str(args['fld:name'])
        self.args=args

def var_decl(**kwargs):
    return VarDecl(kwargs)
    
def void_type(**kwargs):
    return VoidType()

_lookup = globals()

class Unknown:
    def __init__(self, args):
        self.args=args

def unknown(**kwargs):
    return Unknown(kwargs)


def lookup(x):
    if x in _lookup:
        return _lookup[x]
    elif "_" + x  in _lookup:
        return_lookup['_' + x]
    else:
        print "unknown " + x
        return unknown

class DeclExpr:
    def __init__(self, args):
        self.args=args
    
def decl_expr(**kwargs):
    return DeclExpr(kwargs)

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
    else:
        #pprint.pprint(x)
        #raise Exception
        pass
    
    f = lookup(t)
    
    #body = t + "("
    attrs = {}
    #subobj = []   
    for l in x:
        n = l #.replace('fld:type','ftype')
        v = x[l]
        if type(v) is types.DictType:
            #pprint.pprint({"Before ref": v })
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

    #pprint.pprint({'f':f,'i':attrs})
    r = f(**attrs)
    # debug the input and output
    #pprint.pprint({'o':r,'i':attrs})
    return r


new_ast = rec(data.body2.deep)

import unparse

# now lets try and unparse it....
unparse.Unparser(new_ast, sys.stdout)


#for x in f:
#    print "def %s(**kwargs):\n                pass" % x
