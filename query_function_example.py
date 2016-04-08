from graphviz import Digraph
from SPARQLWrapper import SPARQLWrapper, XML, N3, JSONLD, JSON, POST, GET, SELECT, CONSTRUCT, ASK, DESCRIBE
from SPARQLWrapper.Wrapper import _SPARQL_DEFAULT, _SPARQL_XML, _SPARQL_JSON, _SPARQL_POSSIBLE, _RDF_XML, _RDF_N3, _RDF_JSONLD, _RDF_POSSIBLE
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed

import prefix
import types
import json
import pprint

# special tree, name only
fdecl = {
    'name' : 'function decl tree',
    'exprs' :  {
        u'node:function_decl': {
            u'fld:body': {u'skip': u'yes'},
            u'fld:args': {u'node:parm_decl': u'45'},
            u'fld:mngl': {u'node:identifier_node': u'528'},
            u'fld:name': {u'node:identifier_node': u'3082'},
        },
    }
}

just_vals = {
    'name' : 'just values tree',
    'exprs' :  {
        u'node:function_decl': {
            u'fld:body': {u'skip': u'yes'},
            u'fld:args': {u'node:parm_decl': u'45'},
            u'fld:mngl': {u'node:identifier_node': u'528'},
            u'fld:name': {u'node:identifier_node': u'3082'},
        },
        
    }
}

stree = {
    'name' : 'addr expr tree',
    'exprs':
        {
            u'node:addr_expr': {
                u'fld:type': {
                    u'node:function_decl': fdecl, #this could contain an entire function
                }
            }
        }
}

           

tree = {
    'name' : 'main tree',
    'exprs':

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
            


        },
















# here are the types of objects that are ignored

        
        
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


             u'node:pointer_type': {
            u'fld:name': {u'node:type_decl': u'17'},
                               
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
    d={
        'node_id' : prefix.clean(s)
    }
    dt={
        'node_id' : None # literal has no type... 
    }
    #pprint.pprint(results)
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
    pprint.pprint({'query_results':d}, depth=2)
    return d, dt

import types

def recurse_ref(s, subtree):
    print "RECURSE for %s\n" % s
    print "using subtree : %s" % subtree['name']
    d,dt = query(s)
    pprint.pprint({"Got from db":d})
    if 'rdf:type' not in d:
        return d
    
    st = d['rdf:type']
    #print "st" + str(st)
    #pprint.pprint(dt)
    found = False


            
    if not 'exprs' in subtree:
        pprint.pprint({"bad subtree": subtree}, depth=2)
        raise Exception()
    lookup = subtree['exprs']
    
    for k in d:
        r = None # result of the field
        ot = dt[k]
        v = d[k]
        u = prefix.tg +v

        if type(st) is types.DictType:
            print 'skip' + st
            pprint.pprint({
                'case': 'is type',
                 'k' :k,
                 'ot' :ot,
                 'st' : st
            }, depth=2)
            #pprint.pprint(dt)
            #pass # no type
        elif not ot : # no type, a literal
            if k.startswith('fld:'):
                r =  prefix.clean(v) # just a literal
                pprint.pprint({
                    'case': 'is literal',
                    'k' :k,
                    'dt': dt,
                    'ot' :ot,
                    'st' : st
                }, depth=2)
                
                found = True
            else:
                pprint.pprint({
                    'case': 'is no field',
                    'k' :k,
                    'ot' :ot,
                    'st' : st,
                    'r' : r,
                    'v' : v,
                }, depth=2)

                r = v # we need to store the type field
                found = True
                
        elif st in lookup:
            if k in lookup[st]:
                if ot in lookup[st][k]:
                    subtree = lookup[st][k]
                    
                    if type(subtree) is types.DictType:
                        if 'exprs' in subtree:
                            r = recurse_ref(u, subtree)
                            pprint.pprint({"Subtree":r}, depth=2)
                        else:
                            r = recurse_ref(u, tree)
                            pprint.pprint({"tree":r}, depth=2)
                    else:
                        r = recurse_ref(u, tree)
                        pprint.pprint({"tree2":r}, depth=2)
                    found = True
                else:
                    pass # skip
        
        if not found:
            r = recurse_ref(u, just_vals ) # just get one level of info for types and such
            pprint.pprint({
                "missing" : True,
                'k' :k,
                'ot' :ot,
                'st' : st,
                'u' :u,
                'r' :r
            }, depth=2)
        d[k]=r
        
    pprint.pprint({"rec found":d}, depth=2)
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
        r= recurse_ref(x['a']['value'],tree)
        o = open("data/body2.py","w")
        o.write("deep={v2}".format(v2=pprint.pformat(r)))
        o.close()
    
start()
