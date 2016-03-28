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
  rdf:	type ?t			;
  fld:	body[
  rdf:	type ?t2		;
  ?p3 ?o4 ;
  ] ;
  ].
  {
    ?o4 fld:OP0 ?p4.
  }
  UNION {
    ?o4 fld:OP1 ?p4.
  }
  UNION {
    ?o4 fld:expr ?p4.
  }


  optional {
    ?p4 rdf:type nt:var_decl.
    ?p4 fld:name  ?o5.
    ?o5 fld:string ?varname.
    #[  ].
  }


  #FILTER regex(?p3, ".*","i")
  FILTER(REGEX(str(?p3), "E[0-9]", "i")).

}
