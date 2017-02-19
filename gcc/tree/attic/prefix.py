
source = 'http://introspector.xyz/projects/bash/build/eval.c.001t.tu'
tg = source + '#'
fld = 'http://introspector.xyz/gcc/field_types.owl#'
types='http://introspector.xyz/gcc/structure.owl#'
nt   ='http://introspector.xyz/gcc/node_types.owl#'
qual = 'http://introspector.xyz/gcc/qual.owl#'
link = 'http://introspector.xyz/gcc/link.owl#'
rdf = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
art='http://introspector.xyz/gcc/artificial.owl#'
prefixes = """
    PREFIX nt: <http://introspector.xyz/gcc/node_types.owl#>
    PREFIX tg: <http://introspector.xyz/projects/bash/build/eval.c.001t.tu#>
    PREFIX fld: <http://introspector.xyz/gcc/field_types.owl#>
    PREFIX node: <http://introspector.xyz/gcc/node_types.owl#>
    PREFIX link: <http://introspector.xyz/gcc/link.owl#>
    PREFIX art:<http://introspector.xyz/gcc/artificial.owl#>
"""
def clean(x):
    return x.replace(tg,"")\
            .replace(types,"type:")\
            .replace(fld,"fld:")\
            .replace(qual,"qual:")\
            .replace(link,"link:")\
            .replace(rdf,'rdf:') \
            .replace(art,'art:') \
            .replace(source,"")\
            .replace(nt,"node:")\
            #.replace(":","_")\

            
from SPARQLWrapper import SPARQLWrapper, XML, N3, JSONLD, JSON, POST, GET, SELECT, CONSTRUCT, ASK, DESCRIBE
from SPARQLWrapper.Wrapper import _SPARQL_DEFAULT, _SPARQL_XML, _SPARQL_JSON, _SPARQL_POSSIBLE, _RDF_XML, _RDF_N3, _RDF_JSONLD, _RDF_POSSIBLE
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed

def q(q):
    sparql = SPARQLWrapper("http://localhost:8080/sparql")
    sparql.setQuery(prefixes + q)
    sparql.setReturnFormat(JSON)
    sparql.setMethod(GET)
    result = sparql.query()
    results = result.convert();
    return results
