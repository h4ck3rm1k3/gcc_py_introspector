def array_type(**kwargs):
    return "array"

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
    if 'type' in kwargs:
        return kwargs['type']
    else:
        return {"addr_expr" : kwargs}




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

def void_type(**kwargs):
    return "void"

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

def _type(**kwargs):
    return {'type':kwargs}

def integer_type(**kwargs):
    return "int"

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
    if 'name' in kwargs:
        return "[" + str(kwargs['name']) + "]"
    else:
        return {"field_decl" : kwargs}
        

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
        # y=open('example.yaml','a')
        # j=open('example.json','a')
        # y.write(
        #print yaml.dump({"function": kwargs})
        # j.write(json.dumps({"function": kwargs}, 
        #                  sort_keys=True,
        #                  indent=4,
        #                  separators=(',', ': '))
        # )
        # y.close()
        # j.close()
        pprint.pprint({"function_decl" : kwargs})
        return "Func(" + str(kwargs['name']) + ")"

# special tree, name only
stree = {'exprs':
        {
            u'node:addr_expr': {
                u'fld:type': {
                    u'node:function_decl': u'78', #this could contain an entire function
                }
            }
        }
}

lookup = globals()

from graphviz import Digraph
from SPARQLWrapper import SPARQLWrapper, XML, N3, JSONLD, JSON, POST, GET, SELECT, CONSTRUCT, ASK, DESCRIBE
from SPARQLWrapper.Wrapper import _SPARQL_DEFAULT, _SPARQL_XML, _SPARQL_JSON, _SPARQL_POSSIBLE, _RDF_XML, _RDF_N3, _RDF_JSONLD, _RDF_POSSIBLE
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed

import prefix
import types
import json
import pprint
import json
import yaml
import types


def decl_expr(**kwargs):
    pass
f = {}

def rec(x):
    t = "Unknown"

    if 'rdf:type' in x:
        if  x['rdf:type']:
            t = x['rdf:type']
            t = t.replace('node:','')
        else:
            pass
        del x['rdf:type'] # get rid of this        
    args = {}

    for l in x:
        n = l.replace('fld:type','ftype')
        n = n.replace('fld:','')
        v = x[l]
        if type(v) is types.DictType:
            #pass
            v2 = rec(v)
            args[n] = v2 
                        
        elif type(v) in types.StringTypes:
            if n in ('ntype','type','scpe','chain'):
                pass
            elif v =='':
                pass
            else:
                if 'link:' in v:
                    v= v.replace('link:','')
                args[n] = v 
        else:
            #print type(v)
            pass
    f = None
    if t in lookup:
        f = lookup[t]
    elif "_" + t  in lookup:
        f = lookup['_' + t]
        
    return f(**args)



tree = {'exprs':

        {
            u'node:addr_expr': {
                u'fld:OP0': {
                    u'node:pointer_type': u'90'
                },
                u'fld:type': {
                    #u'node:function_decl': u'78', this could contain an entire function
                    u'node:string_cst': u'9',
                    u'node:var_decl': u'3'
                }
            },
        u'node:array_ref': {u'fld:OP0': {u'node:component_ref': u'3'},
                               u'fld:OP1': {u'node:var_decl': u'3'}},
           u'node:bind_expr': {u'fld:body': {u'node:return_expr': u'30',
                                             u'node:statement_list': u'24'},
                               u'fld:vars': {u'node:var_decl': u'21'}},
           u'node:bit_and_expr': {u'fld:OP0': {u'node:array_ref': u'1',
                                               u'node:component_ref': u'2',
                                               u'node:convert_expr': u'4',
                                               u'node:nop_expr': u'3',
                                               u'node:parm_decl': u'2',
                                               u'node:plus_expr': u'3'},
                                  u'fld:OP1': {u'node:bit_not_expr': u'1',
                                               u'node:integer_cst': u'13',
                                               u'node:var_decl': u'1'}},
           u'node:bit_ior_expr': {u'fld:OP0': {u'node:array_ref': u'1',
                                               u'node:bit_and_expr': u'3',
                                               u'node:bit_ior_expr': u'1',
                                               u'node:nop_expr': u'1'},
                                  u'fld:OP1': {u'node:bit_and_expr': u'2',
                                               u'node:lshift_expr': u'3',
                                               u'node:var_decl': u'1'}},
           u'node:bit_not_expr': {u'fld:OP0': {u'node:var_decl': u'1'}},
           u'node:call_expr': {u'fld:E0': {u'node:ge_expr': u'6',
                                           u'node:integer_cst': u'10',
                                           u'node:nop_expr': u'23',
                                           u'node:parm_decl': u'18',
                                           u'node:var_decl': u'7'},
                               u'fld:E1': {u'node:integer_cst': u'12',
                                           u'node:nop_expr': u'13',
                                           u'node:parm_decl': u'8',
                                           u'node:var_decl': u'2'},
                               u'fld:E2': {u'node:integer_cst': u'8',
                                           u'node:parm_decl': u'6',
                                           u'node:var_decl': u'2'},
                               u'fld:E3': {u'node:integer_cst': u'5',
                                           u'node:parm_decl': u'2'},
                               u'fld:fn': {u'node:addr_expr': u'76',
                                           u'node:parm_decl': u'1'}},
           u'node:case_label_expr': {u'fld:low': {u'node:integer_cst': u'4'},
                                     u'fld:name': {u'node:label_decl': u'5'}},
           u'node:component_ref': {u'fld:OP0': {u'node:indirect_ref': u'25',
                                                u'node:var_decl': u'1'},
                                   u'fld:OP1': {u'node:field_decl': u'26'}},
           u'node:compound_expr': {u'fld:OP0': {u'node:modify_expr': u'2'},
                                   u'fld:OP1': {u'node:integer_cst': u'2'}},
           u'node:cond_expr': {u'fld:OP0': {u'node:eq_expr': u'12',
                                            u'node:gt_expr': u'2',
                                            u'node:le_expr': u'2',
                                            u'node:lt_expr': u'2',
                                            u'node:ne_expr': u'28',
                                            u'node:truth_andif_expr': u'14',
                                            u'node:truth_orif_expr': u'4'},
                               u'fld:OP1': {u'node:bind_expr': u'2',
                                            u'node:call_expr': u'16',
                                            u'node:cond_expr': u'1',
                                            u'node:convert_expr': u'2',
                                            u'node:goto_expr': u'12',
                                            u'node:modify_expr': u'9',
                                            u'node:nop_expr': u'5',
                                            u'node:statement_list': u'17'},
                               u'fld:OP2': {u'node:call_expr': u'4',
                                            u'node:cond_expr': u'3',
                                            u'node:goto_expr': u'12',
                                            u'node:integer_cst': u'2',
                                            u'node:nop_expr': u'6',
                                            u'node:parm_decl': u'2',
                                            u'node:return_expr': u'1'}},
           u'node:const_decl': {#u'fld:chain': {u'node:const_decl': u'462',
                                #               u'node:type_decl': u'26'},
                                u'fld:cnst': {u'node:integer_cst': u'488'},
                                u'fld:name': {u'node:identifier_node': u'488'},
                                #u'fld:scpe': {u'node:translation_unit_decl': u'488'}
                            },
           u'node:convert_expr': {u'fld:OP0': {u'node:addr_expr': u'1',
                                               u'node:call_expr': u'1',
                                               u'node:parm_decl': u'9',
                                               u'node:rshift_expr': u'3'}},
           u'node:eq_expr': {u'fld:OP0': {u'node:call_expr': u'2',
                                          u'node:nop_expr': u'16',
                                          u'node:parm_decl': u'1',
                                          u'node:var_decl': u'6'},
                             u'fld:OP1': {u'node:integer_cst': u'12',
                                          u'node:nop_expr': u'7',
                                          u'node:parm_decl': u'6'}},
           u'node:field_decl': {
               #u'fld:bpos': {u'node:integer_cst': u'562'},
               #u'fld:chain': {u'node:field_decl': u'427'},
               u'fld:name': {u'node:identifier_node': u'545'},
            u'fld:orig': {u'node:field_decl': u'2'},
               #u'fld:size': {u'node:integer_cst': u'562'}
                            },
           u'node:function_decl': {u'fld:args': {u'node:parm_decl': u'45'},
                                   u'fld:body': {u'node:bind_expr': u'51'},
                                   #u'fld:chain': {u'node:function_decl': u'3059',
                                   #               u'node:type_decl': u'3',
                                   #               u'node:var_decl': u'19'},
                                   u'fld:mngl': {u'node:identifier_node': u'528'},
                                   u'fld:name': {u'node:identifier_node': u'3082'},
                                   #u'fld:scpe': {u'node:translation_unit_decl': u'2767'}
                               },
           u'node:ge_expr': {u'fld:OP0': {u'node:component_ref': u'6'},
                             u'fld:OP1': {u'node:component_ref': u'6'}},
           u'node:goto_expr': {u'fld:labl': {u'node:label_decl': u'46'}},
           u'node:gt_expr': {u'fld:OP0': {u'node:var_decl': u'2'},
                             u'fld:OP1': {u'node:integer_cst': u'2'}},
           u'node:indirect_ref': {u'fld:OP0': {u'node:call_expr': u'2',
                                               u'node:nop_expr': u'3',
                                               u'node:parm_decl': u'38',
                                               u'node:pointer_plus_expr': u'18',
                                               u'node:postincrement_expr': u'7',
                                               u'node:var_decl': u'15'}},
           u'node:label_decl': {u'fld:name': {u'node:identifier_node': u'1'},
                                #u'fld:scpe': {u'node:function_decl': u'47'}
                            },
           u'node:label_expr': {u'fld:name': {u'node:label_decl': u'42'}},
           u'node:le_expr': {u'fld:OP0': {u'node:nop_expr': u'1',
                                          u'node:parm_decl': u'1',
                                          u'node:plus_expr': u'2'},
                             u'fld:OP1': {u'node:integer_cst': u'4'}},
           u'node:lshift_expr': {u'fld:OP0': {u'node:bit_and_expr': u'3',
                                              u'node:integer_cst': u'3'},
                                 u'fld:OP1': {u'node:bit_and_expr': u'3',
                                              u'node:integer_cst': u'3'}},
           u'node:lt_expr': {u'fld:OP0': {u'node:var_decl': u'2'},
                             u'fld:OP1': {u'node:integer_cst': u'1',
                                          u'node:var_decl': u'1'}},
           u'node:modify_expr': {u'fld:OP0': {u'node:array_ref': u'2',
                                              u'node:indirect_ref': u'11',
                                              u'node:parm_decl': u'1',
                                              u'node:result_decl': u'50',
                                              u'node:var_decl': u'49'},
                                 u'fld:OP1': {u'node:bit_and_expr': u'1',
                                              u'node:bit_ior_expr': u'4',
                                              u'node:call_expr': u'18',
                                              u'node:compound_expr': u'2',
                                              u'node:cond_expr': u'14',
                                              u'node:convert_expr': u'4',
                                              u'node:indirect_ref': u'1',
                                              u'node:integer_cst': u'34',
                                              u'node:modify_expr': u'1',
                                              u'node:ne_expr': u'3',
                                              u'node:nop_expr': u'6',
                                              u'node:parm_decl': u'2',
                                              u'node:plus_expr': u'1',
                                              u'node:pointer_plus_expr': u'1',
                                              u'node:postincrement_expr': u'1',
                                              u'node:preincrement_expr': u'1',
                                              u'node:trunc_div_expr': u'1',
                                              u'node:var_decl': u'18'}},
           u'node:mult_expr': {u'fld:OP0': {u'node:nop_expr': u'2',
                                            u'node:var_decl': u'1'},
                               u'fld:OP1': {u'node:integer_cst': u'2',
                                            u'node:parm_decl': u'1'}},
           u'node:ne_expr': {u'fld:OP0': {u'node:bit_and_expr': u'3',
                                          u'node:call_expr': u'9',
                                          u'node:component_ref': u'1',
                                          u'node:modify_expr': u'2',
                                          u'node:nop_expr': u'25',
                                          u'node:parm_decl': u'1',
                                          u'node:var_decl': u'18'},
                             u'fld:OP1': {u'node:integer_cst': u'48',
                                          u'node:parm_decl': u'11'}},
           u'node:nop_expr': {u'fld:OP0': {u'node:addr_expr': u'13',
                                           u'node:array_ref': u'1',
                                           u'node:bit_ior_expr': u'1',
                                           u'node:call_expr': u'7',
                                           u'node:component_ref': u'2',
                                           u'node:convert_expr': u'3',
                                           u'node:indirect_ref': u'40',
                                           u'node:modify_expr': u'3',
                                           u'node:mult_expr': u'3',
                                           u'node:nop_expr': u'3',
                                           u'node:parm_decl': u'24',
                                           u'node:plus_expr': u'3',
                                           u'node:postincrement_expr': u'3',
                                           u'node:var_decl': u'31'}},
           u'node:parm_decl': {u'fld:chain': {u'node:parm_decl': u'48'},
                               u'fld:name': {u'node:identifier_node': u'93'},
                               #u'fld:scpe': {u'node:function_decl': u'93'},
                               #u'fld:size': {u'node:integer_cst': u'93'}
                           }
                            ,
           u'node:plus_expr': {u'fld:OP0': {u'node:nop_expr': u'2',
                                            u'node:parm_decl': u'6',
                                            u'node:var_decl': u'2'},
                               u'fld:OP1': {u'node:integer_cst': u'9',
                                            u'node:var_decl': u'1'}},
           u'node:pointer_plus_expr': {u'fld:OP0': {u'node:indirect_ref': u'2',
                                                    u'node:parm_decl': u'17'},
                                       u'fld:OP1': {u'node:integer_cst': u'1',
                                                    u'node:nop_expr': u'18'}},
           u'node:postdecrement_expr': {u'fld:OP0': {u'node:var_decl': u'1'},
                                        u'fld:OP1': {u'node:integer_cst': u'1'}},
           u'node:postincrement_expr': {u'fld:OP0': {u'node:component_ref': u'6',
                                                     u'node:indirect_ref': u'1',
                                                     u'node:parm_decl': u'2',
                                                     u'node:var_decl': u'3'},
                                        u'fld:OP1': {u'node:integer_cst': u'12'}},
           u'node:preincrement_expr': {u'fld:OP0': {u'node:parm_decl': u'3',
                                                    u'node:var_decl': u'9'},
                                       u'fld:OP1': {u'node:integer_cst': u'12'}},
           u'node:result_decl': {
               #u'fld:scpe': {u'node:function_decl': u'49'},
               #                  u'fld:size': {u'node:integer_cst': u'49'}
           },
           u'node:return_expr': {u'fld:expr': {u'node:modify_expr': u'50'}},
           u'node:rshift_expr': {u'fld:OP0': {u'node:parm_decl': u'3'},
                                 u'fld:OP1': {u'node:integer_cst': u'3'}},
           u'node:statement_list': {u'fld:E0': {u'node:call_expr': u'4',
                                                u'node:case_label_expr': u'1',
                                                u'node:decl_expr': u'21',
                                                u'node:goto_expr': u'2',
                                                u'node:modify_expr': u'14'},
                                    u'fld:E1': {u'node:call_expr': u'4',
                                                u'node:case_label_expr': u'1',
                                                u'node:cond_expr': u'7',
                                                u'node:decl_expr': u'8',
                                                u'node:goto_expr': u'12',
                                                u'node:label_expr': u'4',
                                                u'node:modify_expr': u'4',
                                                u'node:postincrement_expr': u'1',
                                                u'node:switch_expr': u'1'},
                                    u'fld:E10': {u'node:cond_expr': u'2',
                                                 u'node:label_expr': u'1',
                                                 u'node:modify_expr': u'2'},
                                    u'fld:E11': {u'node:call_expr': u'1',
                                                 u'node:cond_expr': u'1',
                                                 u'node:modify_expr': u'1',
                                                 u'node:postdecrement_expr': u'1',
                                                 u'node:return_expr': u'1'},
                                    u'fld:E12': {u'node:cond_expr': u'1',
                                                 u'node:goto_expr': u'1',
                                                 u'node:modify_expr': u'1',
                                                 u'node:return_expr': u'1'},
                                    u'fld:E13': {u'node:case_label_expr': u'1',
                                                 u'node:label_expr': u'1',
                                                 u'node:modify_expr': u'1'},
                                    u'fld:E14': {u'node:call_expr': u'1',
                                                 u'node:cond_expr': u'2'},
                                    u'fld:E15': {u'node:label_expr': u'1',
                                                 u'node:return_expr': u'1'},
                                    u'fld:E16': {u'node:return_expr': u'1'},
                                    u'fld:E2': {u'node:call_expr': u'2',
                                                u'node:case_label_expr': u'1',
                                                u'node:cond_expr': u'3',
                                                u'node:convert_expr': u'1',
                                                u'node:decl_expr': u'2',
                                                u'node:goto_expr': u'2',
                                                u'node:label_expr': u'8',
                                                u'node:modify_expr': u'4',
                                                u'node:preincrement_expr': u'2',
                                                u'node:return_expr': u'6'},
                                    u'fld:E3': {u'node:call_expr': u'2',
                                                u'node:cond_expr': u'4',
                                                u'node:decl_expr': u'2',
                                                u'node:label_expr': u'3',
                                                u'node:modify_expr': u'4',
                                                u'node:preincrement_expr': u'6'},
                                    u'fld:E4': {u'node:call_expr': u'2',
                                                u'node:cond_expr': u'6',
                                                u'node:decl_expr': u'1',
                                                u'node:label_expr': u'7',
                                                u'node:modify_expr': u'1',
                                                u'node:preincrement_expr': u'3',
                                                u'node:return_expr': u'1'},
                                    u'fld:E5': {u'node:call_expr': u'1',
                                                u'node:cond_expr': u'7',
                                                u'node:goto_expr': u'3',
                                                u'node:label_expr': u'4',
                                                u'node:modify_expr': u'5'},
                                    u'fld:E6': {u'node:call_expr': u'1',
                                                u'node:cond_expr': u'3',
                                                u'node:goto_expr': u'1',
                                                u'node:label_expr': u'10',
                                                u'node:modify_expr': u'3',
                                                u'node:return_expr': u'2'},
                                    u'fld:E7': {u'node:bind_expr': u'1',
                                                u'node:case_label_expr': u'1',
                                                u'node:cond_expr': u'3',
                                                u'node:goto_expr': u'1',
                                                u'node:label_expr': u'1',
                                                u'node:modify_expr': u'3',
                                                u'node:return_expr': u'6'},
                                    u'fld:E8': {u'node:cond_expr': u'3',
                                                u'node:label_expr': u'2',
                                                u'node:modify_expr': u'2',
                                                u'node:return_expr': u'1'},
                                    u'fld:E9': {u'node:cond_expr': u'4',
                                                u'node:modify_expr': u'1'}},
           u'node:switch_expr': {u'fld:body': {u'node:statement_list': u'1'},
                                 u'fld:cond': {u'node:var_decl': u'1'}},
           u'node:tree_list': {u'fld:chan': {u'node:tree_list': u'2714'},
                               u'fld:purp': {u'node:identifier_node': u'488'},
                               u'fld:valu': {u'node:integer_cst': u'488'}},
           u'node:trunc_div_expr': {u'fld:OP0': {u'node:nop_expr': u'3',
                                                 u'node:plus_expr': u'1'},
                                    u'fld:OP1': {u'node:integer_cst': u'4'}},
           u'node:truth_andif_expr': {u'fld:OP0': {u'node:eq_expr': u'1',
                                                   u'node:ne_expr': u'13',
                                                   u'node:truth_andif_expr': u'6'},
                                      u'fld:OP1': {u'node:eq_expr': u'2',
                                                   u'node:le_expr': u'2',
                                                   u'node:ne_expr': u'15',
                                                   u'node:truth_and_expr': u'1'}},
           u'node:truth_orif_expr': {u'fld:OP0': {u'node:eq_expr': u'4',
                                                  u'node:truth_orif_expr': u'2'},
                                     u'fld:OP1': {u'node:eq_expr': u'6'}},
           u'node:type_decl': {#u'fld:chain': {u'node:const_decl': u'26',
                               #               u'node:function_decl': u'5',
                               #               u'node:type_decl': u'460'},
                               u'fld:name': {u'node:identifier_node': u'318'},
               #u'fld:scpe': {u'node:translation_unit_decl': u'449'}
           },
           u'node:var_decl': {#u'fld:chain': {u'node:function_decl': u'18',
                              #               u'node:label_decl': u'1',
                              #               u'node:var_decl': u'106'},
                              u'fld:init': {u'node:indirect_ref': u'3',
                                            u'node:integer_cst': u'6',
                                            u'node:lshift_expr': u'3',
                                            u'node:trunc_div_expr': u'3',
                                            u'node:var_decl': u'2'},
                              u'fld:name': {u'node:identifier_node': u'146'},
                              #u'fld:scpe': {u'node:function_decl': u'34',
                              #              u'node:translation_unit_decl': u'112'},
                              #u'fld:size': {u'node:integer_cst': u'134'}
           },

            u'node:enumeral_type': {
            #{u'fld:csts': {u'node:tree_list': u'31'},
                                   u'fld:max': {u'node:integer_cst': u'31'},
                                   u'fld:min': {u'node:integer_cst': u'31'},
                                   u'fld:name': {u'node:identifier_node': u'9',
                                                 u'node:type_decl': u'5'},
                                   u'fld:size': {u'node:integer_cst': u'31'},
                                   #u'fld:unql': {u'node:enumeral_type': u'5'}
                               },

    u'node:integer_type': {u'fld:max': {u'node:integer_cst': u'188'},
                           u'fld:min': {u'node:integer_cst': u'188'},
                           u'fld:name': {u'node:identifier_node': u'2',
                                         u'node:type_decl': u'157'},
                           u'fld:size': {u'node:integer_cst': u'188'},
                           #u'fld:unql': {u'node:integer_type': u'144'}
                       },

        },

        
 'types': {
           u'node:array_ref': {u'fld:type': {u'node:integer_type': u'3'}},
           u'node:array_type': {u'fld:domn': {u'node:integer_type': u'49'},
                                u'fld:elts': {u'node:integer_type': u'36',
                                              u'node:pointer_type': u'7',
                                              u'node:record_type': u'14'},
                                u'fld:name': {u'node:type_decl': u'8'},
                                #u'fld:size': {u'node:integer_cst': u'49'},
                                u'fld:unql': {u'node:array_type': u'12'}},
           u'node:bind_expr': {u'fld:type': {u'node:void_type': u'54'}},
           u'node:bit_and_expr': {u'fld:type': {u'node:integer_type': u'15'}},
           u'node:bit_ior_expr': {u'fld:type': {u'node:integer_type': u'6'}},
           u'node:bit_not_expr': {u'fld:type': {u'node:integer_type': u'1'}},
           u'node:boolean_type': {u'fld:name': {u'node:type_decl': u'1'},
                                  u'fld:size': {u'node:integer_cst': u'1'}},
           u'node:call_expr': {u'fld:type': {u'node:integer_type': u'46',
                                             u'node:pointer_type': u'12',
                                             u'node:real_type': u'1',
                                             u'node:void_type': u'18'}},
           u'node:case_label_expr': {u'fld:type': {u'node:void_type': u'5'}},
           u'node:complex_type': {u'fld:name': {u'node:type_decl': u'4'},
                                  u'fld:size': {u'node:integer_cst': u'5'}},
           u'node:component_ref': {u'fld:type': {u'node:array_type': u'3',
                                                 u'node:enumeral_type': u'1',
                                                 u'node:integer_type': u'2',
                                                 u'node:pointer_type': u'20'}},
           u'node:compound_expr': {u'fld:type': {u'node:integer_type': u'2'}},
           u'node:cond_expr': {u'fld:type': {u'node:integer_type': u'11',
                                             u'node:pointer_type': u'3',
                                             u'node:void_type': u'50'}},
           u'node:const_decl': {u'fld:type': {u'node:enumeral_type': u'488'}},
           u'node:convert_expr': {u'fld:type': {u'node:integer_type': u'11',
                                                u'node:pointer_type': u'2',
                                                u'node:void_type': u'1'}},
           u'node:decl_expr': {u'fld:type': {u'node:void_type': u'34'}},
           u'node:enumeral_type': {u'fld:csts': {u'node:tree_list': u'31'},
                                   #u'fld:max': {u'node:integer_cst': u'31'},
                                   #u'fld:min': {u'node:integer_cst': u'31'},
                                   #u'fld:name': {u'node:identifier_node': u'9',
                                   #              u'node:type_decl': u'5'},
                                   #u'fld:size': {u'node:integer_cst': u'31'},
                                   u'fld:unql': {u'node:enumeral_type': u'5'}},
           u'node:eq_expr': {u'fld:type': {u'node:integer_type': u'25'}},
           u'node:field_decl': {
               #u'fld:scpe': {u'node:record_type': u'459',
               #                               u'node:union_type': u'103'},
                                u'fld:type': {u'node:array_type': u'42',
                                              u'node:enumeral_type': u'4',
                                              u'node:integer_type': u'290',
                                              u'node:pointer_type': u'169',
                                              u'node:real_type': u'2',
                                              u'node:record_type': u'29',
                                              u'node:union_type': u'26'}},
           u'node:function_decl': {u'fld:type': {u'node:function_type': u'3082'}},
           u'node:function_type': {u'fld:name': {u'node:type_decl': u'45'},
                                   u'fld:prms': {u'node:tree_list': u'1102'},
                                   u'fld:retn': {u'node:boolean_type': u'22',
                                                 u'node:complex_type': u'13',
                                                 u'node:integer_type': u'487',
                                                 u'node:pointer_type': u'310',
                                                 u'node:real_type': u'66',
                                                 u'node:record_type': u'4',
                                                 u'node:vector_type': u'58',
                                                 u'node:void_type': u'154'},
                                   u'fld:size': {u'node:integer_cst': u'1114'},
                                   u'fld:unql': {u'node:function_type': u'51'}},
           u'node:ge_expr': {u'fld:type': {u'node:integer_type': u'6'}},
           u'node:goto_expr': {u'fld:type': {u'node:void_type': u'46'}},
           u'node:gt_expr': {u'fld:type': {u'node:integer_type': u'2'}},
           u'node:indirect_ref': {u'fld:type': {u'node:integer_type': u'47',
                                                u'node:pointer_type': u'11',
                                                u'node:record_type': u'25'}},
           u'node:integer_cst': {u'fld:type': {u'node:integer_type': u'455',
                                               u'node:pointer_type': u'12'}},
           u'node:integer_type': {u'fld:max': {u'node:integer_cst': u'188'},
                                  u'fld:min': {u'node:integer_cst': u'188'},
                                  u'fld:name': {u'node:identifier_node': u'2',
                                                u'node:type_decl': u'157'},
                                  u'fld:size': {u'node:integer_cst': u'188'},
                                  u'fld:unql': {u'node:integer_type': u'144'}},
           u'node:label_decl': {u'fld:type': {u'node:void_type': u'47'}},
           u'node:label_expr': {u'fld:type': {u'node:void_type': u'42'}},
           u'node:le_expr': {u'fld:type': {u'node:integer_type': u'4'}},
           u'node:lshift_expr': {u'fld:type': {u'node:integer_type': u'6'}},
           u'node:lt_expr': {u'fld:type': {u'node:integer_type': u'2'}},
           u'node:modify_expr': {u'fld:type': {u'node:integer_type': u'76',
                                               u'node:pointer_type': u'36',
                                               u'node:real_type': u'1'}},
           u'node:mult_expr': {u'fld:type': {u'node:integer_type': u'3'}},
           u'node:ne_expr': {u'fld:type': {u'node:integer_type': u'59'}},
           u'node:nop_expr': {u'fld:type': {u'node:integer_type': u'103',
                                            u'node:pointer_type': u'34'}},
           u'node:parm_decl': {u'fld:argt': {u'node:integer_type': u'49',
                                             u'node:pointer_type': u'44'},
                               u'fld:type': {u'node:integer_type': u'49',
                                             u'node:pointer_type': u'44'}},
           u'node:plus_expr': {u'fld:type': {u'node:integer_type': u'10'}},
           u'node:pointer_plus_expr': {u'fld:type': {u'node:pointer_type': u'19'}},
           u'node:pointer_type': {u'fld:name': {u'node:type_decl': u'17'},
                                  u'fld:ptd': {u'node:array_type': u'7',
                                               u'node:function_type': u'77',
                                               u'node:integer_type': u'40',
                                               u'node:pointer_type': u'18',
                                               u'node:real_type': u'6',
                                               u'node:record_type': u'129',
                                               u'node:union_type': u'2',
                                               u'node:vector_type': u'3',
                                               u'node:void_type': u'9'},
                                  u'fld:size': {u'node:integer_cst': u'291'},
                                  u'fld:unql': {u'node:pointer_type': u'62'}},
           u'node:postdecrement_expr': {u'fld:type': {u'node:integer_type': u'1'}},
           u'node:postincrement_expr': {u'fld:type': {u'node:integer_type': u'1',
                                                      u'node:pointer_type': u'11'}},
           u'node:preincrement_expr': {u'fld:type': {u'node:integer_type': u'7',
                                                     u'node:pointer_type': u'5'}},
           u'node:real_type': {u'fld:name': {u'node:type_decl': u'9'},
                               u'fld:size': {u'node:integer_cst': u'9'},
                               u'fld:unql': {u'node:real_type': u'2'}},
           u'node:record_type': {u'fld:flds': {u'node:field_decl': u'177'},
                                 u'fld:name': {u'node:identifier_node': u'89',
                                               u'node:type_decl': u'69'},
                                 u'fld:size': {u'node:integer_cst': u'177'},
                                 u'fld:unql': {u'node:record_type': u'79'}},
           u'node:reference_type': {u'fld:refd': {u'node:pointer_type': u'1'},
                                    u'fld:size': {u'node:integer_cst': u'1'}},
           u'node:result_decl': {u'fld:type': {u'node:integer_type': u'41',
                                               u'node:pointer_type': u'7',
                                               u'node:real_type': u'1'}},
           u'node:return_expr': {u'fld:type': {u'node:void_type': u'51'}},
           u'node:rshift_expr': {u'fld:type': {u'node:integer_type': u'3'}},
           u'node:string_cst': {u'fld:type': {u'node:array_type': u'9'}},
           u'node:switch_expr': {u'fld:type': {u'node:integer_type': u'1'}},
           u'node:tree_list': {u'fld:valu': {u'node:boolean_type': u'9',
                                             u'node:complex_type': u'12',
                                             u'node:enumeral_type': u'15',
                                             u'node:integer_type': u'811',
                                             u'node:pointer_type': u'1227',
                                             u'node:real_type': u'89',
                                             u'node:record_type': u'3',
                                             u'node:reference_type': u'3',
                                             u'node:union_type': u'6',
                                             u'node:vector_type': u'105',
                                             u'node:void_type': u'4'}},
           u'node:trunc_div_expr': {u'fld:type': {u'node:integer_type': u'4'}},
           u'node:truth_and_expr': {u'fld:type': {u'node:integer_type': u'1'}},
           u'node:truth_andif_expr': {u'fld:type': {u'node:integer_type': u'20'}},
           u'node:truth_orif_expr': {u'fld:type': {u'node:integer_type': u'6'}},
           u'node:type_decl': {u'fld:type': {u'node:array_type': u'8',
                                             u'node:boolean_type': u'1',
                                             u'node:complex_type': u'5',
                                             u'node:enumeral_type': u'31',
                                             u'node:function_type': u'45',
                                             u'node:integer_type': u'161',
                                             u'node:pointer_type': u'17',
                                             u'node:real_type': u'8',
                                             u'node:record_type': u'167',
                                             u'node:union_type': u'48',
                                             u'node:void_type': u'2'}},
           u'node:union_type': {u'fld:flds': {u'node:field_decl': u'50'},
                                u'fld:name': {u'node:identifier_node': u'5',
                                              u'node:type_decl': u'13'},
                                u'fld:size': {u'node:integer_cst': u'50'},
                                u'fld:unql': {u'node:union_type': u'14'}},
           u'node:var_decl': {u'fld:type': {u'node:array_type': u'14',
                                            u'node:integer_type': u'95',
                                            u'node:pointer_type': u'30',
                                            u'node:record_type': u'7'}},
           u'node:vector_type': {u'fld:size': {u'node:integer_cst': u'12'},
                                 u'fld:unql': {u'node:vector_type': u'1'}},
           u'node:void_type': {u'fld:name': {u'node:type_decl': u'5'},
                               u'fld:unql': {u'node:void_type': u'4'}}}}

f = {}
skip= {
    'fld:source_file' :1 # dont need this in the document
}
def query(s):
    results = prefix.q( """  
SELECT ?a ?p ?o ?t  WHERE {
    <%s> ?p ?o.
    optional {
       ?o rdf:type ?t.
    }
}
    """ % s)
    d={}
    dt={}
    for x in results['results']['bindings']:
        v = prefix.clean(x['o']['value'])
        t = None
        if 't' in x:
            t = prefix.clean(x['t']['value'])
        else:
            #pprint.pprint(x)
            pass # have no node type

        k = x['p']['value']
        k = prefix.clean(k)
        if k not in d:
            if k not in skip:
                d[k]=v  # the value of the field
                dt[k]=t # the domain type of the field object
        else:
            #d[k]=[d[k],v]
            raise Exception("duplicate")
    
    return d, dt

# recurse
def recurse(s, deep=True):
    #print "RECURSE for %s\n" % s
    d,dt = query(s)
    #pprint.pprint({"Got from db":d})
    if 'rdf:type' not in d:
        return d
    if not deep:
        return d
    st = d['rdf:type']
    #print "st" + str(st)
    #pprint.pprint(dt)
    found = False
    
    for k in d:
        r = None # result of the field
        ot = dt[k]
        v = d[k]
        u = prefix.tg +v

        if type(st) is types.DictType:
            raise Exception("")
            pprint.pprint({
                'k' :k,
                'ot' :ot,
                'st' : st
            })
            #pprint.pprint(dt)
            pass # no type
        elif not ot : # no type, a literal
            if k.startswith('fld:'):
                r =  prefix.clean(v) # just a literal
                found = True
            else:
                r = v # we need to store the type field
                found = True
                
        elif st in tree['exprs']:
            if k in tree['exprs'][st]:
                if ot in tree['exprs'][st][k]:
                    r = recurse(u)
                    found = True
                else:
                    pass # skip
        
        if not found:
            if st in stree['exprs']:
                if k in stree['exprs'][st]:
                    if ot in stree['exprs'][st][k]:
                        r = recurse(u, False)
                        #pprint.pprint(r)
                        found = True
                    else:
                        pass

        if not found:
            r = recurse(u, False) # just get one level of info for types and such

        d[k]=r

    return (d)

# print out what field types occur
def start():
    t = {}
    results = prefix.q( """  
SELECT ?a  WHERE {
  ?a fld:srcp 'eval.c:216'.
  ?a fld:name  [ fld:string 'parse_command'].
  ?a rdf:type nt:function_decl.
}
""")               
    for x in results['results']['bindings']:
        print x['a']['value']
        r= recurse(x['a']['value'])
        pprint.pprint(rec(r))


start()

