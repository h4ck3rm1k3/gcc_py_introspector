	SELECT

	?t
	(count(?f) as ?count)
	(min(?f) as ?first)
	(max(?f) as ?last)

	WHERE {

	?f <http://introspector.xyz/gcc/field_types.owl#srcp> 'true'.
	?f rdf:type ?t.


	}
	group by ?t
