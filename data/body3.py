#!/usr/bin/python
import pprint

def result_decl(**kwargs):
    return "return"

def var_decl(**kwargs):
    #pprint.pprint(kwargs)
    return kwargs['name']

def identifier_node(**kwargs):
    return kwargs['string']

######################

def call_expr(**kwargs):
    return {"call" : kwargs}

def decl_expr(**kwargs):
#    pprint.pprint({"decl_expr" : kwargs})
    #return {"decl_expr" : kwargs}
    return None

def expr(**kwargs):
#    pprint.pprint({"expr" : kwargs})
    return {"expr" : kwargs}

def cond_expr(**kwargs):
#    pprint.pprint({"cond_expr" : kwargs})
    return {"cond_expr" : kwargs}

def ne_expr(**kwargs):
#    pprint.pprint({"ne_expr" : kwargs})
    return {"ne_expr" : kwargs}

def addr_expr(**kwargs):
    #pprint.pprint({"addr_expr" : kwargs})
    return kwargs['type']

import yaml



def modify_expr(**kwargs):
#    pprint.pprint({"Modify":kwargs})
    return [ kwargs['OP0'], "=", kwargs['OP1'] ]

def truth_andif_expr(**kwargs):
#    pprint.pprint({"truth_andif_expr" : kwargs})
    return {"truth_andif_expr" : kwargs}

def nop_expr(**kwargs):
#    pprint.pprint({"nop_expr" : kwargs})
    #return {"nop" : kwargs}
    return kwargs['OP0']

def bind_expr(**kwargs):
#    pprint.pprint({"bind_expr" : kwargs})
    return {"bind" : kwargs}

def return_expr(**kwargs):
#    pprint.pprint({"return_expr" : kwargs})
    return {"ret" : kwargs}

def eq_expr(**kwargs):
#    pprint.pprint({"eq_expr" : kwargs})
    return [ kwargs['OP0'], "==", kwargs['OP1'] ]

            
def pointer_type(**kwargs):
#    pprint.pprint({"pointer_type" : kwargs})
    return {"ptr" : kwargs}

def component_ref(**kwargs):
#    pprint.pprint({"component_ref" : kwargs})
    return {"comp_ref" : kwargs}

def OP0(**kwargs):
    return kwargs

def OP1(**kwargs):
    return kwargs

def vars(**kwargs):
    #pprint.pprint({"vars" : kwargs})
    return {"vars" : kwargs}

def type(**kwargs):
    return {'type':kwargs}

def integer_cst(**kwargs):
    return kwargs['low']

def size(**kwargs):
    return kwargs

def note(**kwargs):
    return kwargs       

def low(**kwargs):
    #pprint.pprint({"low" : kwargs})
    return {"low" : kwargs}

def body(**kwargs):
    #pprint.pprint({"body" : kwargs})
    return {"body" : kwargs}

def used(**kwargs):
    return kwargs

def string(**kwargs):
    #pprint.pprint({"string" : kwargs})
    return {"string" : kwargs}

def string_cst(**kwargs):
    #pprint.pprint({"string_cst" : kwargs})
    return "\"" + kwargs['string'] + "\""
    
def srcp(**kwargs):
    return kwargs

def link(**kwargs):
    return kwargs

def fn(**kwargs):
    #pprint.pprint({"fn" : kwargs})
    return {"fn" : kwargs}

def name(**kwargs):
    #pprint.pprint({"name" : kwargs})
    return {"name" : kwargs}
    
def bpos(**kwargs):
    return kwargs

def algn(**kwargs):
    return kwargs

def field_decl(**kwargs):
    #pprint.pprint({"field_decl" : kwargs})
    return "[" + kwargs['name'] + "]"

def statement_list(**kwargs):
    #pprint.pprint({"statement_list" : kwargs})
    r = []
    for x in sorted(kwargs.keys()):
        v = kwargs[x]
        if v:
            r.append(kwargs[x])
    #return {"stmts" : kwargs}
    return r

def E2(**kwargs):
    return kwargs
def E8(**kwargs):
    return kwargs
def E5(**kwargs):
    return kwargs
def E4(**kwargs):
    return kwargs
def E7(**kwargs):
    return kwargs
def E6(**kwargs):
    return kwargs
def E1(**kwargs):
    return kwargs
def E0(**kwargs):
    pprint.pprint(kwargs)
    return kwargs
def E3(**kwargs):
    return kwargs

def Unknown():
    return "Unknown"

def function_decl(**kwargs):
    if kwargs['body'] == 'Unknown':
        pass
    else:
        print yaml.dump({"function": kwargs})
        #pprint.pprint({"function_decl" : kwargs})
        return "Func(" + kwargs['name'] + ")"
