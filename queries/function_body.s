	SELECT ?o ?s ?b  WHERE {
	#?o <http://introspector.xyz/gcc/field_types.owl#tag> ?tag.
	?o rdf:type <http://introspector.xyz/gcc/node_types.owl#function_decl>.
	?o rdf:type ?type.
	?o <http://introspector.xyz/gcc/field_types.owl#name> ?n.
	?n <http://introspector.xyz/gcc/field_types.owl#string> ?s.

	#?f <http://introspector.xyz/gcc/field_types.owl#scpe> ?o.
	#?f <http://introspector.xyz/gcc/field_types.owl#name> ?fn.
	#?fn <http://introspector.xyz/gcc/field_types.owl#string> ?fs.
	?o <http://introspector.xyz/gcc/field_types.owl#body> ?b.

	FILTER (?b != <http://introspector.xyz/gcc/link.owl#undefined>)

	 }
