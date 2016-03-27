
	SELECT  ?on  ?bn  WHERE {
	bind(replace(str(?o),'http://introspector.xyz/projects/bash/build/eval.c.001t.tu#','') as ?on)
	bind(replace(str(?b),'http://introspector.xyz/projects/bash/build/eval.c.001t.tu#','') as ?bn)

	{
	?o <http://introspector.xyz/gcc/field_types.owl#OP0> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#OP1> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#OP2> ?b.
	}

	union {
	?o <http://introspector.xyz/gcc/field_types.owl#OP3> ?b.
	}

	          }
