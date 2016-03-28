# -*- sparql -*-
PREFIX nt: <http://introspector.xyz/gcc/node_types.owl#>
PREFIX tg: <http://introspector.xyz/projects/bash/build/eval.c.001t.tu#>
PREFIX fld: <http://introspector.xyz/gcc/field_types.owl#>
PREFIX node: <http://introspector.xyz/gcc/node_types.owl#>
PREFIX link: <http://introspector.xyz/gcc/link.owl#>

SELECT * WHERE {
  
  ?a fld:srcp 'eval.c:216'.
  ?a fld:name  [ fld:string 'parse_command'].
  ?a rdf:type nt:function_decl.

  ?a fld:body[
  rdf:type ?t.
  ?p ?t2.
  
  ]
  ###
  
}
