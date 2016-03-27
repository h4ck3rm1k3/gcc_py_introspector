
	SELECT ?on  ?bn ?st  ?tn WHERE {
	bind(replace(str(?o),'http://introspector.xyz/projects/bash/build/eval.c.001t.tu#','') as ?on)
	bind(replace(str(?b),'http://introspector.xyz/projects/bash/build/eval.c.001t.tu#','') as ?bn)


	#          ?o rdf:type <http://introspector.xyz/gcc/node_types.owl#function_decl>.
	?o rdf:type ?type.
	bind(replace(str(?type),'http://introspector.xyz/gcc/node_types.owl#','') as ?tn)



	{
	?o <http://introspector.xyz/gcc/field_types.owl#OP0> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#OP1> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#E0> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#expr> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#fn> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#OP2> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#OP3> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#body> ?b.
	}

	optional {
	?b <http://introspector.xyz/gcc/field_types.owl#name> ?c.
	?c <http://introspector.xyz/gcc/field_types.owl#string> ?st.
	}



	FILTER (?b != <http://introspector.xyz/gcc/link.owl#undefined>)

	          }
