#!/usr/bin/python
"""
a quine

import sys,inspect;sys.stdout.write(inspect.getsource(inspect.currentframe()))
"""

#~/py/python/Lib/ast.py
#~/py/python/Lib/test/test_ast.py

#import ast



import ast

import sys
import os
home=os.environ['HOME']

#~/py/python/Tools/parser/unparse.py
#sys.path.append(home + "/py/python/Tools/parser")
import unparse

# git@github.com:ActiveState/appdirs.git
sys.path.append(home + "/py/appdirs")
import appdirs

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

#hg clone https://bitbucket.org/pypy/pypy
# pypy uses the internet ast.Num
sys.path.append(home + "/py/pypy")

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


class IntegerConstant:

    @staticmethod
    def pyast() :
        return ast.Num
    
    #def pypy():
    #    return pyast()

    def pypy_tokens():
        return pypy.interpreter.pyparser.pygram.tokens.NUMBER

    def asteroid ():
        return astroid.node_classes.Const # shared
    
    def cython():
        return Cython.Compiler.ExprNodes.IntNode

    @staticmethod
    def tu_parser():
        return tuparser.p_ntype_integer_cst
        
    def PythonToken():
        return pgen2.token.NUMBER
        # ~/py/python/Include/token.h same as in
        
    def redbaron():
        return redbaron.nodes.IntNode

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


class StringConstant:
    def pyast() :
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

    @staticmethod
    def tu_parser():
        return tuparser.p_ntype_string_cst
        
    def PythonToken():
        return pgen2.token.STRING
        # ~/py/python/Include/token.h same as in
        
    def redbaron():
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
# convert to/from rdf
# convert to/from some yaml format
# convert to/from some json format
# convert to/from assembler.....
# convert to/from network package
import inspect
import pprint
import plyreflect

def main(args):

    g = globals()
    for x in g:
        v = g[x]
        if inspect.isclass(v) :
            print "Class:"+ x
            n = v()

            p = v.tu_parser()
            r = plyreflect.reflect(p)
            pprint.pprint({"ply reflection": r})
            
            for k in p.__dict__:
                print k
                print p.__dict__[k]
            for f in inspect.getmembers(p):
                pprint.pprint( f)
                            
            for f in inspect.getmembers(v):
                
                if inspect.ismethod(f[1]):
                    print "Calling"+ x + "." +f[0]
                    #print f[1]
                    r =  v.__dict__[f[0]]()
                else:
                    #print "What?" + str(f)
                    pass
                
            # for f in dir(v):
            #     m = v.__dict__[f]
            #     print f, m

if __name__=='__main__':
    main(sys.argv[1:])
