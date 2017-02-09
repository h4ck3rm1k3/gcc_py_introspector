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

#def Unknown():
#    return "Unknown"

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
seen = {}

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
        if type(v) is dict:
            #pass
            v2 = rec(v)
            args[n] = v2 
                        
        elif type(v) in str:
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
    else:
        pprint.pprint(
            {
                't':t,
                'f':f,
                'args':args,
                'x':x,
            }, depth=3)
        return None

    return f(**args)

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

def recurse(s, deep=0):

    if s in seen:
        #print "Seen"
        return "skipthis"

    seen[s]=1
    if deep > 1000:
        #print "Too Deep"
        return {"too deep": s}
    
    d,dt = query(s)
    #pprint.pprint({"Got from db":d})
    if 'rdf:type' not in d:
        return d

    st = d['rdf:type']
    #print "st" + str(st)
    #pprint.pprint({"data type": dt})
   
    for k in d:
        found = False
        
        if k in ('fld:qual',
                 'fld:string',
                 'fld:chain'):
            continue
        r = None # result of the field
        ot = dt[k]
        v = d[k]
        u = prefix.tg +v
        # pprint.pprint({
        #     "Check field " : {
        #         'k' :k,
        #         'u' :u,
        #         'ot' :ot,
        #         'st' : st
        #     }})
        if type(st) is dict:
            raise Exception("")
        
            #pprint.pprint(dt)
            pass # no type
        elif not ot : # no type, a literal
            if k.startswith('fld:'):
                r =  prefix.clean(v) # just a literal
                found = True
            else:
                r = v # we need to store the type field
                found = True
                
        #print "going to recurse to "+ u
        if not found:
            r = recurse(u, deep + 1)
        d[k]=r

    # save        
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
        print(x['a']['value'])
        r= recurse(x['a']['value'])
        pprint.pprint(rec(r))


start()

