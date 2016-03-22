	SELECT ?s ?fs WHERE {
	?o <http://introspector.xyz/gcc/field_types.owl#tag> ?tag.
	#?o rdf:type <http://introspector.xyz/gcc/node_types.owl#record_type>.
	?o rdf:type ?type.
	?o <http://introspector.xyz/gcc/field_types.owl#name> ?n.
	?n <http://introspector.xyz/gcc/field_types.owl#string> ?s.

	?f <http://introspector.xyz/gcc/field_types.owl#scpe> ?o.
	?f <http://introspector.xyz/gcc/field_types.owl#name> ?fn.
	?fn <http://introspector.xyz/gcc/field_types.owl#string> ?fs.

	 }
