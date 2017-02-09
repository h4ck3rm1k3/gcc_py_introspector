from graphviz import Digraph
from SPARQLWrapper import SPARQLWrapper, XML, N3, JSONLD, JSON, POST, GET, SELECT, CONSTRUCT, ASK, DESCRIBE
from SPARQLWrapper.Wrapper import _SPARQL_DEFAULT, _SPARQL_XML, _SPARQL_JSON, _SPARQL_POSSIBLE, _RDF_XML, _RDF_N3, _RDF_JSONLD, _RDF_POSSIBLE
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed

tg = 'http://introspector.xyz/projects/bash/build/eval.c.001t.tu#'
fld = 'http://introspector.xyz/gcc/field_types.owl#'
types='http://introspector.xyz/gcc/structure.owl#'
qual = 'http://introspector.xyz/gcc/qual.owl#'

prefixes = """
    PREFIX tg: <http://introspector.xyz/projects/bash/build/eval.c.001t.tu#>
    PREFIX fld: <http://introspector.xyz/gcc/field_types.owl#>
    PREFIX node: <http://introspector.xyz/gcc/node_types.owl#>
    PREFIX link: <http://introspector.xyz/gcc/link.owl#>
"""

fields = [
    #'chain', # dangerous... used too many times. need to qualify name
    #'chan',
    #'cnst',
    #'csts',
    #'domn',
    #'elts',
    #'flds',
    #'link',
    #'scpe',
    #'tag',
    #'type',
    #'unql',
    #'used',
    #'valu',
    #u'algn',
    #u'argt',
    #u'bpos',
    #u'high',
    #u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type',
    #u'max',
    #u'min',
    #u'source_file',

    'E0',
    'E1',
    'E10',
    'E11',
    'E12',
    'E13',
    'E14',
    'E15'
    'E16',
    'E2',
    'E3',
    'E4',
    'E5',
    'E6',
    'E7',
    'E8',
    'E9',

    'OP0',
    'OP1',
    'OP2',
    
    # 'args',
     'body',
    # 'cond',
    # 'expr',
     'fn',
     'init',
    # 'labl',
    # 'low',
    # 'mngl',
     'name',
    # 'note',
    # 'orig',
    # 'prec',
    # 'prms',
    # 'ptd',
    # 'purp',
    # 'qual',
    # 'refd',
    # 'retn',
    # 'sign',
    # 'size',
    # 'spec',
    # 'srcp',
     'string',
    # 'vars',   
]
#FILTER (?b != link:undefined)


import json
import pprint


dot = Digraph(comment='Example')
def q(q):
    sparql = SPARQLWrapper("http://localhost:8080/sparql")
    sparql.setQuery(prefixes + q)
    sparql.setReturnFormat(JSON)
    sparql.setMethod(GET)
    result = sparql.query()
    results = result.convert();
    return results

# print out what field types occur
def ftypes():
    t = {}
    results = q( """
    SELECT ?p WHERE {
    ?s ?p ?o.    } group by ?p""")
    for x in results['results']['bindings']:
        t[(x['p']['value'].replace(fld,''))]=1

    pprint.pprint( list(t.keys()))
    
#ftypes()
def clean(x):
    return x.replace(tg,"").replace(types,"").replace(fld,"").replace(qual,"").replace(":","_")
                      
for fld in fields:
    selectQuery = """
    SELECT ?s  ?o WHERE {
    ?s fld:%s ?o.    }""" % fld

    results = q(selectQuery)
    
    for x in results['results']['bindings']:
        a = clean(x['s']['value'])

        b = clean(x['o']['value'])
        if b == "http_//introspector.xyz/gcc/link.owl#undefined":
            pass
        elif b == "http_//introspector.xyz/gcc/artificial.owl#artificial" :
            pass
        else:
            dot.edge(a, b, label=str(fld))

print((dot.source)) 
