#!/usr/bin/python

import yaml
import body2
import types
import pprint
#print yaml.dump(deep)

def decl_expr(**kwargs):
    pass
f = {}

def rec(x,i=0):
    t = "Unknown"
    indent = i * "  "

    if 'rdf:type' in x:
        if  x['rdf:type']:
            t = x['rdf:type']
            t = t.replace('node:','')
            if t not in f: # seen
                f[t]='ntype'
        else:
            #pprint.pprint(x)
            pass
        del x['rdf:type'] # get rid of this
        
    body = t + "("
    attrs = []
    subobj = []   
    for l in x:
        n = l.replace('fld:type','ftype')
        n = n.replace('fld:','')
        v = x[l]
        if type(v) is types.DictType:
            #pass
            v2 = rec(v,i+1)
            subobj.append("\n"+ indent + "  " + n + "=" + v2 + "")
            f[n]='fld'
                        
        elif type(v) in types.StringTypes:
            if n in ('ntype','type','scpe','chain'):
                pass
            elif v =='':
                pass
            else:
                if 'link:' in v:
                    v= v.replace('link:','')
                #print n,v                
                attrs.append(n + "='" + v + "'")
                f[n]='fld'
        else:
            #print type(v)
            pass

    l = sorted(attrs)
    l.extend(sorted(subobj))
    body = body + ",".join(l)
    #body = body + ",".join()
    #pprint.pprint(attrs)
    body = body + ")"
    return body

o = open("body4.py","w")
o.write('#!/usr/bin/python' + "\n")
o.write("from body3 import *" + "\n")
o.write(rec(body2.deep))
o.close()

for x in f:
    print "def %s(**kwargs):\n                pass" % x
