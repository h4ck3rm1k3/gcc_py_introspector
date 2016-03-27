from graphviz import Digraph
from SPARQLWrapper import SPARQLWrapper, XML, N3, JSONLD, JSON, POST, GET, SELECT, CONSTRUCT, ASK, DESCRIBE
from SPARQLWrapper.Wrapper import _SPARQL_DEFAULT, _SPARQL_XML, _SPARQL_JSON, _SPARQL_POSSIBLE, _RDF_XML, _RDF_N3, _RDF_JSONLD, _RDF_POSSIBLE
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed

tg = 'http://introspector.xyz/projects/bash/build/eval.c.001t.tu#'
fld = 'http://introspector.xyz/gcc/field_types.owl#'
types='http://introspector.xyz/gcc/structure.owl#'
nt   ='http://introspector.xyz/gcc/node_types.owl#'
qual = 'http://introspector.xyz/gcc/qual.owl#'

prefixes = """
    PREFIX tg: <http://introspector.xyz/projects/bash/build/eval.c.001t.tu#>
    PREFIX fld: <http://introspector.xyz/gcc/field_types.owl#>
    PREFIX node: <http://introspector.xyz/gcc/node_types.owl#>
    PREFIX link: <http://introspector.xyz/gcc/link.owl#>
"""

fields = [
    #'elts',
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
    #u'algn',
    'args',
    #u'argt',
    'body',
    #u'bpos',
    #'chain', # dangerous... used too many times. need to qualify name
    'chan',
    #'cnst',
    'cond',
    #'csts',
    #'domn',
    'expr',
    #'flds',
    'fn',
    #u'high',
    #u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type',
    'init',
    'labl',
    #'link',
    'low',
    #u'max',
    #u'min',
    'mngl',
    'name',
    'note',
    'orig',
    'prec',
    'prms',
    'ptd',
    'purp',
    'qual',
    'refd',
    'retn',
    #'scpe',
    'sign',
    'size',
    #u'source_file',
    'spec',
    'srcp',
    'string',
    #'tag',
    #'type',
    #'unql',
    #'used',
    #'valu',
    'vars',   
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
    SELECT ?st ?p ?ot WHERE {
    ?s rdf:type ?st.
    ?s ?p ?o.    
    ?o rdf:type ?ot.

    } group by  ?st ?p ?ot""")
    for x in results['results']['bindings']:
        print x['st']['value'].replace(nt,'') +"\t"+ x['p']['value'].replace(fld,'') + "\t"+ x['ot']['value'].replace(nt,'')

        #pprint.pprint( t.keys())
    
ftypes()
