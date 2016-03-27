	PREFIX nt: <http://introspector.xyz/gcc/node_types.owl#>

	PREFIX tg: <http://introspector.xyz/projects/bash/build/eval.c.001t.tu#>
	PREFIX fld: <http://introspector.xyz/gcc/field_types.owl#>
	PREFIX node: <http://introspector.xyz/gcc/node_types.owl#>
	PREFIX link: <http://introspector.xyz/gcc/link.owl#>


	SELECT  *  WHERE {
	?f ?p ?a.

	?a rdf:type nt:string_cst.
	?a fld:string ?s.

	  }
