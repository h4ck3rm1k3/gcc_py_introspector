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
    PREFIX nt: <http://introspector.xyz/gcc/node_types.owl#>
    PREFIX tg: <http://introspector.xyz/projects/bash/build/eval.c.001t.tu#>
    PREFIX fld: <http://introspector.xyz/gcc/field_types.owl#>
    PREFIX node: <http://introspector.xyz/gcc/node_types.owl#>
    PREFIX link: <http://introspector.xyz/gcc/link.owl#>
"""


import json
import pprint

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

    SELECT ?st ?p ?ot (count(?o) as ?count) (min(?o) as ?firsto) (min(?s) as ?firsts)
WHERE {
    ?s rdf:type ?st.
    ?s ?p ?o.
    ?o rdf:type ?ot.                                                                                                                                            } group by  ?st ?p ?ot

""")
    for x in results['results']['bindings']:
        print "\t".join(
            [
                x['count']['value'],
                x['firsto']['value'].replace(tg,''),
                x['firsts']['value'].replace(tg,''),
                x['st']['value'].replace(nt,''),
                x['p']['value'].replace(fld,''),
                x['ot']['value'].replace(nt,'')
            ]
        )

        #pprint.pprint( t.keys())
    
ftypes()
