	SELECT  ?on  ?bn ?st WHERE {
	bind(replace(str(?o),'http://introspector.xyz/projects/bash/build/eval.c.001t.tu#','') as ?on)
	?o <http://introspector.xyz/gcc/field_types.owl#body> ?b.
	FILTER (?b != <http://introspector.xyz/gcc/link.owl#undefined>) .
	bind(replace(str(?b),'http://introspector.xyz/projects/bash/build/eval.c.001t.tu#','') as ?bn)


	optional {
	?o rdf:type <http://introspector.xyz/gcc/node_types.owl#function_decl>.
	?o <http://introspector.xyz/gcc/field_types.owl#name> ?n.
	?n <http://introspector.xyz/gcc/field_types.owl#string> ?st.
	bind(replace(str(?n),'http://introspector.xyz/projects/bash/build/eval.c.001t.tu#','') as ?nn)
	FILTER(REGEX(?st, "^[a-z]", "i")).
	}
	}
	
