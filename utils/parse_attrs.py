# parse the attrs
import re
import pprint
f =open ('attrs.txt')

types = {}

for x in f:
    x = re.sub(r' attrs attrs '," ATTRLIST ",x)
    x = re.sub(r' ATTRLIST attrs '," ATTRLIST ",x)
    x = re.sub(r' ATTRLIST ATTRLIST '," ATTRLIST ",x)
    parts = x.split(" . ")  
    stack = parts[0].split(" ")
    last = parts[1]
    #m = re.match("LexToken\((\w+),",last)
    #if m:
    #    stack.append(m.group(1))
        
    btype = stack[2]
    if btype not in types:
        types[btype] = {}
    t = types[btype]
    #print stack
    for s in stack[3:]:
        if s not in t:
            t[s]={}
        t = t[s]
    #print btype, stack[3:], parts[1]
#pprint.pprint( types)
def r(t):
    rt =[]
    #pprint.pprint( t)
    for k in t:
        m = re.match(r'\w+_ATTR',k)
        if m :
            #print "\tKey:%s" % k,"->", ",".join(rt)
            if len(rt) > 0:
                last = rt[-1]
                if k != last:
                    rt.append(k)
            else:
                rt.append(k)
                
        kd = t[k]

        ret = r(kd)
        if len(rt) >0 :
            for x in ret:
                last = rt[-1]
                if x != last:
                    rt.append(x)
        else:
            rt = ret
            
    return rt

ttypes = {}

for t in types:
    #print "T:%s" % t
    td = types[t]
    d = r(td)
    d2 = list(x for x in reversed(d))
    k = ",".join(d2)

    if k not in ttypes:
        ttypes[k] = [t]
    else:
        last = ttypes[k][-1]
        if t != last :
            #print t,last
            ttypes[k].append(t)

#pprint.pprint(ttypes)
for s in ttypes:
    #print s
    for x in ttypes[s]:
        #print x, s
        t = s.replace(","," ")
        print """def p_%s_node(psr_val):\n    'node : NODE %s %s attr_list'""" % (x,x,t)
