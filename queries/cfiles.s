	SELECT  * WHERE {
	?a <http://introspector.xyz/gcc/field_types.owl#srcp> ?b.
	FILTER(REGEX(?b, ".c:", "i")).


	optional {
	?a <http://introspector.xyz/gcc/field_types.owl#name> ?n.
	?n <http://introspector.xyz/gcc/field_types.owl#string> ?st.
	FILTER(REGEX(?st, "^[a-z]", "i")).
	}


	optional {
	?a <http://introspector.xyz/gcc/field_types.owl#scpe> ?na.
	?na <http://introspector.xyz/gcc/field_types.owl#name> ?n.
	?n <http://introspector.xyz/gcc/field_types.owl#string> ?st2.

	}


	# ?a ?p ?c2.
	#      ?o <http://introspector.xyz/gcc/field_types.owl#body> ?b.
	#          ?b ?p2 ?c3.


	}
		
