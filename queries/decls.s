	SELECT  ?a ?b ?st ?tn WHERE {
	?a <http://introspector.xyz/gcc/field_types.owl#srcp> ?b.
	FILTER(REGEX(?b, ".c:", "i")).

	?a rdf:type ?t.

	bind(replace(str(?t),'http://introspector.xyz/gcc/node_types.owl#','') as ?tn).


	optional {
	?a <http://introspector.xyz/gcc/field_types.owl#name> ?n.
	?n <http://introspector.xyz/gcc/field_types.owl#string> ?st.
	FILTER(REGEX(?st, "^[a-z]", "i")).
	}


	optional {
	?a <http://introspector.xyz/gcc/field_types.owl#scpe> ?na.
	?na <http://introspector.xyz/gcc/field_types.owl#name> ?n.
	?n <http://introspector.xyz/gcc/field_types.owl#string> ?st.

	}


	# ?a ?p ?c2.
	#      ?o <http://introspector.xyz/gcc/field_types.owl#body> ?b.
	#          ?b ?p2 ?c3.


	}
		
