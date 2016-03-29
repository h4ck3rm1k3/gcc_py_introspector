import yaml
import body2
import types
import pprint
#print yaml.dump(deep)

def rec(x,i=0):
    t = "Unknown"
    indent = i * "  "
    if 'rdf:type' in x:
        t = x['rdf:type']
        t = t.replace('node:','')
        del x['rdf:type']

    
    t.replace('node:','')
    body = t + "("
    attrs = []
    subobj = []   
    for l in x:
        n= l.replace('fld:','')
        v = x[l]
        if type(v) is types.DictType:
            #pass
            v2 = rec(v,i+1)
            subobj.append("\n"+ indent + "  " + n + "=" + v2 + "")
            
        elif type(v) in types.StringTypes:
            if n in ('type','scpe','chain'):
                pass
            elif v =='':
                pass
            else:
                if 'link:' in v:
                    v= v.replace('link:','')
                #print n,v                
                attrs.append(n + "='" + v + "'")
                
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
    
print rec(body2.deep);
