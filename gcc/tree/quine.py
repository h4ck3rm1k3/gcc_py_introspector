#!/usr/bin/python
"""
a quine

First goal will be to generate normal python asts from the gcc nodes, 
and following that to generate python code from c.

The idea is that we have a self describing program that can emit itself.
The difference to normal quines is that we treat the emitting of the code as just a mode of the program itself.
We want to be able to :

query and fitler parts of the program relative to the current execution or any part.

* emit the full or partial source code
* emit the full or partial parse tree
* emit the full or partial ast graph
* emit the full or partial call stack
* emit the full or partial program memory
* emit the full or partial assembly code

We are going to want to connect :

1. gcc tree node definitions
2. the code the emits the tree codes
3. equivalent code in clang/llvm
4. python asts


Display on a website like 
http://www.pythontutor.com/

git@github.com:quantifiedcode/python-ast-visualizer.git

https://github.com/srossross/Meta
git@github.com:landscapeio/prospector.git
https://pypi.python.org/pypi/redhawk/
http://alexleone.blogspot.com/2010/01/python-ast-pretty-printer.html

"""

#~/py/python/Lib/ast.py
#~/py/python/Lib/test/test_ast.py
import ast

import sys
import os
home=os.environ['HOME']

# the unparser is embedded here.
#~/py/python/Tools/parser/unparse.py
#sys.path.append(home + "/py/python/Tools/parser")
import unparse

#tree = compile(source, filename, "exec", ast.PyCF_ONLY_AST)


# git@github.com:ActiveState/appdirs.git
sys.path.append(home + "/py/appdirs")
import appdirs

sys.path.append(home + "/py/Meta")
import meta

#git@github.com:alex/rply.git
sys.path.append(home + "/py/rply")
import rply

#https://github.com/PyCQA/baron
sys.path.append(home + "/py/baron")
import baron

#htts://github.com/Psycojoker/redbaron
sys.path.append(home + "/py/redbaron")
import redbaron.nodes

#htts://github.com/Psycojoker/redbaron
sys.path.append(home + "/py/lib2to3")
import redbaron.nodes
import pgen2.token
import tuparser

#hg clone https://bitbucket.org/takluyver/greentreesnakes
# Read: http://greentreesnakes.readthedocs.org/en/latest/nodes.html#literals
sys.path.append(home + "/py/greentreesnakes")

#TODO
# https://github.com/eliben/pycparser


#hg clone https://bitbucket.org/pypy/pypy
# pypy uses the internet ast.Num
sys.path.append(home + "/py/pypy")
#https://github.com/sota/pypy/blob/master/pypy/interpreter/pyparser/pytoken.py
#tokens from here

#git clone git@github.com:cython/cython.git
sys.path.append(home + "/py/cython")
import Cython.Compiler.ExprNodes

import pypy.interpreter.pyparser.pygram

import types

# pyflakes uses ast and NUM
#git@github.com:pyflakes/pyflakes.git
#sys.path.append(home + "/py/pyflakes")

#git@github.com:PyCQA/astroid.git
sys.path.append(home + "/py/astroid") # needs to be installed, python3 code
import astroid.node_classes
#astroid/node_classes.py

#git@github.com:PyCQA/pylint.git
sys.path.append(home + "/py/pylint")

# iast
#git clone git@github.com:brandjon/iast.git
sys.path.append(home + "/py/iast")

# consult
# ~/py/python/Parser/Python.asdl
import io
class PyAst:
    @classmethod
    def pyast(cls) :
        pass

    def get_ast_args(self):
        pass
    
    def ast_flip(self) :
        a = cls.pyast()
        if a :
            n = a(self.get_ast_args())
            if n:
                return cls.dounparse(n)
                
    @staticmethod
    def dounparse(tree):
        output = io.StringIO()       
        unparse.Unparser(tree, output)
        v = output.getvalue()
        output.close()
        return v
   
    @classmethod
    def verify(cls):
        print(cls.pyast())

class RedBaron:
    
    @classmethod
    def redbaron(cls):
        pass
    
    @classmethod
    def verify(cls):
        print(cls.redbaron())
    
class TuNode:

    @classmethod
    def tu_parser(cls):
        return None # not defined
    
    @classmethod
    def verify(cls):
        print(cls.token())

    @classmethod
    def token(cls):
        p = cls.tu_parser()
        if p:
            r = plyreflect.reflect(p)
            node_token = r['token_meta'][0]['token'].node
            return node_token
        else:
            return None

class NodeType(TuNode, PyAst):
    @classmethod
    def verify(cls):
        pprint.pprint ({
            "Token" : cls.token(),
            "ast" : PyAst.verify(), #cls.ast_flip()
        })

class Constant(NodeType):
    pass
    
    
class IntegerConstant(Constant):

    @classmethod
    def pyast(cls) :
        return ast.Num

    #def pypy():
    #    return pyast()

    def pypy_tokens():
        return pypy.interpreter.pyparser.pygram.tokens.NUMBER

    def asteroid ():
        return astroid.node_classes.Const # shared

    def cython():
        return Cython.Compiler.ExprNodes.IntNode

    @classmethod
    def tu_parser(cls):
        return tuparser.p_ntype_integer_cst

    def PythonToken():
        return pgen2.token.NUMBER
        # ~/py/python/Include/token.h same as in

    @classmethod
    def redbaron(cls):
        return redbaron.nodes.IntNode

#  https://github.com/inducer/pycparserext

#https://github.com/eliben/pycparser
sys.path.append(home + "/py/pycparser")
import pycparser

#~/py/pycparser/pycparser/c_lexer.py

class IntegerConstantDecimal(IntegerConstant):
    def py_cparser():
        return pycparser.c_lexer.t_INT_CONST_DEC
    #INT_CONST_DEC

class IntegerConstantOctal(IntegerConstant):
    def py_cparser():
        return pycparser.c_lexer.t_INT_CONST_OCT

class IntegerConstantHex(IntegerConstant):
    def py_cparser():
        return pycparser.c_lexer.t_INT_CONST_HEX

class IntegerConstantBin(IntegerConstant):
    def py_cparser():
        return pycparser.c_lexer.t_INT_CONST_BIN

# class NumericTypeInteger:
#     def types():
#         return types.IntType
#     def python_type():
#         return int

# class NumericTypeLong:
#     def types():
#         return types.LongType
#     def python_type():
#         return long

# class NumericTypeFloat:
#     def types():
#         return types.FloatType
#     def python_type():
#         return float


class StringConstant(Constant):
    @classmethod
    def pyast(cls) :
        return ast.Str

    #def pypy():
    #    return pyast()

    def pypy_tokens():
        #pypy/interpreter/pyparser/pytoken.py
        return pypy.interpreter.pyparser.pygram.tokens.STRING

    def asteroid ():
        return astroid.node_classes.Const # shared

    def cython():
        return Cython.Compiler.ExprNodes.StringNode

    @classmethod
    def tu_parser(cls):
        return tuparser.p_ntype_string_cst

    def PythonToken():
        return pgen2.token.STRING
        # ~/py/python/Include/token.h same as in

    @classmethod
    def redbaron(cls):
        return redbaron.nodes.StringNode

# ~/py/python/Lib/lib2to3/
#~/py/redbaron/redbaron/nodes.py

# conversions we want to support :
# convert to/from python ast
# convert to/from xpath expression
# convert to/from xlst ...
# convert to/from python text
# convert to/from tree.tu
# convert to/from c
#   see https://github.com/eliben/pycparser/blob/master/pycparser/c_generator.py
# convert to/from rdf
# convert to/from some yaml format
# convert to/from some json format
# convert to/from assembler.....
# convert to/from network package
import inspect
import pprint
import plyreflect

def main(args):

    # let do a simple walk over the classes and verify them
    g = globals()
    for x in g:
        v = g[x]
        if inspect.isclass(v) :
            print("Class:"+ x)
            #n = v()
            v.verify()
            # test getting the gcc translation unit codes

            # test creating a 
            #dounparse
            
            # for k in p.__dict__:
            #     print k
            #     print p.__dict__[k]
            # for f in inspect.getmembers(p):
            #     pprint.pprint( f)

            # for f in inspect.getmembers(v):

            #     if inspect.ismethod(f[1]):
            #         print "Calling"+ x + "." +f[0]
            #         #print f[1]
            #         r =  v.__dict__[f[0]]()
            #     else:
            #         #print "What?" + str(f)
            #         pass

            # for f in dir(v):
            #     m = v.__dict__[f]
            #     print f, m

if __name__=='__main__':
    main(sys.argv[1:])
