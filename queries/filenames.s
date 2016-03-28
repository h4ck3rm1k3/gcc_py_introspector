	SELECT ?filen
	WHERE {

	?f <http://introspector.xyz/gcc/field_types.owl#srcp> ?s.


	bind(strafter(str(?s),':') as ?linen)
	bind(STRBEFORE(str(?s),':') as ?filen)

	}
	group by ?filen
