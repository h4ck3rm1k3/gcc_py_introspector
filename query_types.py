from graphviz import Digraph

import prefix

import json
import pprint

# print out what field types occur
def ftypes():
    t = {}
    results = prefix.q( """  

    SELECT ?st ?p ?ot (count(?o) as ?count) (min(?o) as ?firsto) (min(?s) as ?firsts)
WHERE {
    ?s rdf:type ?st.
    ?s ?p ?o.
    ?o rdf:type ?ot.                                                                                                                                            } group by  ?st ?p ?ot

""")
    print("\t".join(
        [
            'count',
            'firsto',
            'firsts',
            'st',
            'p',
            'ot']))
    d1 = {}
    d2 = {}
    for x in results['results']['bindings']:
        s=prefix.clean(x['st']['value'])
        o=prefix.clean(x['ot']['value'])
        p=prefix.clean(x['p']['value'])
        print("\t".join(
            [
                x['count']['value'],
                prefix.clean(x['firsto']['value']),
                prefix.clean(x['firsts']['value']),
                prefix.clean(x['st']['value']),
                prefix.clean(x['p']['value']),
                prefix.clean(x['ot']['value'])
            ]))
            

        atype =False
        if o.endswith('type'):
            atype=True
        if s.endswith('type'):
            atype=True
        if p in ('type','domn','elts',
                     'size','unql',
                     'chain',
                     'scpe',
                     'min',
                     'max',
                     'csts',
                     'bpos',
                     'retn',
                     'argt',
                     'ptd',
                     'flds',
                     'refd'
             ):
            atype=True


        if not atype:
            d = d1
            if s not in d:
                d[s] = {}
            if p not in d[s]:
                d[s][p] = {}

            if o not in d[s][p]:
                d[s][p][o]  =x['count']['value']
            else:
                d[s][p][o]= d[s][p][o] + x['count']['value']            
        else:
            d = d2
            if s not in d:
                d[s] = {}
            if p not in d[s]:
                d[s][p] = {}

            if o not in d[s][p]:
                d[s][p][o]  =x['count']['value']
            else:
                d[s][p][o]= d[s][p][o] + x['count']['value']            


    pprint.pprint( { 'exprs' :d1 ,
                     'types' :d2
                 })
    
ftypes()


