#!/usr/bin/python
import pprint

def result_decl(**kwargs):
    return "return"

def var_decl(**kwargs):
    #pprint.pprint(kwargs)
    return kwargs['name']

def identifier_node(**kwargs):
        return kwargs['string']

def call_expr(**kwargs):
    #pprint.pprint({"call" : kwargs})
    return kwargs

def addr_expr(**kwargs):
    #pprint.pprint({"addr_expr" : kwargs})
    return kwargs['type']

def function_decl(**kwargs):
    #pprint.pprint({"function_decl" : kwargs})
    return "Func(" + kwargs['name'] + ")"

def modify_expr(**kwargs):
    pprint.pprint({"Modify":kwargs})
    return kwargs

def pointer_type(**kwargs):
                pass

def component_ref(**kwargs):
                pass
def OP0(**kwargs):
                pass
def OP1(**kwargs):
                pass
def vars(**kwargs):
                pass

def truth_andif_expr(**kwargs):
                pass
def type(**kwargs):
                pass
def integer_cst(**kwargs):
         return kwargs['low']
def size(**kwargs):
                pass
def note(**kwargs):
                pass
       

def low(**kwargs):
                pass
def body(**kwargs):
                pass
def used(**kwargs):
                pass
def string(**kwargs):
                pass
def return_expr(**kwargs):
                pass
def string_cst(**kwargs):
                pass
    
def nop_expr(**kwargs):
                pass
def srcp(**kwargs):
                pass
def eq_expr(**kwargs):
                pass
def link(**kwargs):
                pass
def bind_expr(**kwargs):
                pass
def fn(**kwargs):
                pass
def name(**kwargs):
                pass
def decl_expr(**kwargs):
                pass
def expr(**kwargs):
                pass
def cond_expr(**kwargs):
                pass
def ne_expr(**kwargs):
                pass
    
def bpos(**kwargs):
                pass
def algn(**kwargs):
                pass
def field_decl(**kwargs):
                pass
def statement_list(**kwargs):
                pass
def E2(**kwargs):
                pass
def E8(**kwargs):
                pass
def E5(**kwargs):
                pass
def E4(**kwargs):
                pass
def E7(**kwargs):
                pass
def E6(**kwargs):
                pass
def E1(**kwargs):
                pass
def E0(**kwargs):
                pass
def E3(**kwargs):
                pass

def Unknown():
    pass

