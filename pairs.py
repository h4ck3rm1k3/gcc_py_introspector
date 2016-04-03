# addr_expr   Starred
# array_type Tuple
# bind_expr Lambda
# call_expr Call
# component_ref ? Attribute

# decl_expr Complex
import pprint
import inspect

import sys
import os
home=os.environ['HOME']

sys.path.append(home + "/py/Meta")
import meta

def p(**kwargs):
    stack = inspect.stack()
    kwargs['__stack'] = stack
    pprint.pprint( kwargs)
    
class Tu:
    def __init__(self, name):
        self.name = name
    def __call__(a, b):
        p(a=a, b=b)

import compiler.ast
import ast

class Reflect:
    def __init__(self, f):
        self.func = f
        s = inspect.getsource(f)
        s = """
def reflect(x):
    pass
        
""" + s
        print s
        tree = ast.parse(s)
        #mod2 = meta.decompile(f)
        #source2 = meta.dump_python_source(mod2)
        p(a=self,
          m=tree.__dict__,
          d2=ast.dump(tree),
          s2=s,
          d=self.__dict__,
          f=f,
          fd=f.__dict__,
        )

    #def __call__(a, b):
    #    p(a=a, b=b, f=self.func)

def tu(name):
    return Tu(name)

def reflect(m):
    return Reflect(m)

from ast import *

#@tu("eq_expr")
class EqExpr:

    @reflect
    def example():
        f = 1
        if f == 1:
            print "body"

    @reflect
    def reflection_of_example():
        ref= ast.Module(        
            ast.FunctionDef(
            name='example',
            args=
            ast.arguments(
                args=[], vararg=None, kwarg=None, defaults=[]
            ),
            body=[
                ast.Assign(
                    targets=[
                        ast.Name(
                            id='f', ctx=ast.Store())
                    ],
                    value=ast.Num(n=1)),
                ast.If(test=ast.Compare(
                        left=ast.Name(
                            id='f',
                            ctx=ast.Load()),
                    ops=[ast.Eq()], comparators=[ast.Num(n=1)]),
                       body=[
                           ast.Print(dest=None, values=[ast.Str(s='body')], nl=True)],
                   orelse=[])],
            decorator_list=[])
        )
    
    def reflection_of_reflection_of_example(self):
         r=Module(body=[FunctionDef(name='reflect', args=arguments(args=[Name(id='x', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Pass(), FunctionDef(name='reflection_of_example', args=arguments(args=[], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='ref', ctx=Store())], value=Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Module', ctx=Load()), args=[Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='FunctionDef', ctx=Load()), args=[], keywords=[keyword(arg='name', value=Str(s='example')), keyword(arg='args', value=Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='arguments', ctx=Load()), args=[], keywords=[keyword(arg='args', value=List(elts=[], ctx=Load())), keyword(arg='vararg', value=Name(id='None', ctx=Load())), keyword(arg='kwarg', value=Name(id='None', ctx=Load())), keyword(arg='defaults', value=List(elts=[], ctx=Load()))], starargs=None, kwargs=None)), keyword(arg='body', value=List(elts=[Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Assign', ctx=Load()), args=[], keywords=[keyword(arg='targets', value=List(elts=[Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Name', ctx=Load()), args=[], keywords=[keyword(arg='id', value=Str(s='f')), keyword(arg='ctx', value=Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Store', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None))], starargs=None, kwargs=None)], ctx=Load())), keyword(arg='value', value=Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Num', ctx=Load()), args=[], keywords=[keyword(arg='n', value=Num(n=1))], starargs=None, kwargs=None))], starargs=None, kwargs=None), Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='If', ctx=Load()), args=[], keywords=[keyword(arg='test', value=Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Compare', ctx=Load()), args=[], keywords=[keyword(arg='left', value=Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Name', ctx=Load()), args=[], keywords=[keyword(arg='id', value=Str(s='f')), keyword(arg='ctx', value=Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Load', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None))], starargs=None, kwargs=None)), keyword(arg='ops', value=List(elts=[Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Eq', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)], ctx=Load())), keyword(arg='comparators', value=List(elts=[Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Num', ctx=Load()), args=[], keywords=[keyword(arg='n', value=Num(n=1))], starargs=None, kwargs=None)], ctx=Load()))], starargs=None, kwargs=None)), keyword(arg='body', value=List(elts=[Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Print', ctx=Load()), args=[], keywords=[keyword(arg='dest', value=Name(id='None', ctx=Load())), keyword(arg='values', value=List(elts=[Call(func=Attribute(value=Name(id='ast', ctx=Load()), attr='Str', ctx=Load()), args=[], keywords=[keyword(arg='s', value=Str(s='body'))], starargs=None, kwargs=None)], ctx=Load())), keyword(arg='nl', value=Name(id='True', ctx=Load()))], starargs=None, kwargs=None)], ctx=Load())), keyword(arg='orelse', value=List(elts=[], ctx=Load()))], starargs=None, kwargs=None)], ctx=Load())), keyword(arg='decorator_list', value=List(elts=[], ctx=Load()))], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None))], decorator_list=[Name(id='reflect', ctx=Load())])], decorator_list=[])])
         
e=EqExpr()
e.reflection_of_reflection_of_example()

# field_decl
# function_decl
# identifier_node
# integer_cst Num
# integer_type
# modify_expr Assign
# ne_expr
# nop_expr
# pointer_type
# result_decl
# return_expr
# statement_list
# string_cst Str
# cond_expr IfExp
# truth_andif_expr IfExp
# var_decl
# void_type



# ?Set?
# ?Dict?
# ?Ellipsis?
# ?NameConstant


# Attriubtes
# body=body
