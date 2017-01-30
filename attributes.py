from functools import wraps
import pprint
import ply.lex as lex

class TNode :
    def __init__(x, v, z, o):
        pass

def get_value(x):
    if 'value' in x.__dict__:
        return x.value
    else:
        return pprint.pformat(x)

funcs = {}

def parser_rule(f):
    """ 
    parser rule
    """
    doc = f.__doc__
    #pprint.pprint( dir(f))
    #pprint.pprint( f.__dict__)
    @wraps(f)
    def wrapper(psr_val):
        
        #if len(psr_val.stack) ==  1:
        #print 'Parser f', f, doc
        funcs[f]=1
        #pprint.pprint({ 'slice' :psr_val.slice,
        #                'stack' : psr_val.stack})
        #pprint.pprint(psr_val.__dict__)
        #rpprint.pprint(dir(psr_val))
        i = 0

        # if isinstance(psr_val,lex.LexToken):
        #     #print psr_val
        #     pass
        # else:
            
             # for x in psr_val.slice[1:] :
             #     print "\t\t\tITEM:",i,":", pprint.pformat(x),"Value:",pprint.pformat(get_value(x))
             #     i = i +1
        #         #, pprint.pformat(dir(x))            
        r= f(psr_val)
        x =psr_val.slice[0]
        #print "\t\t\tresult:",i,":", pprint.pformat(x),"Value:",pprint.pformat(get_value(x))

        
        return r
    

    
    wrapper.doc = doc
    return wrapper

registry = {}
types = {}
def parser_node_rule(f):
    """ 
    parser node rule
    """
    doc = f.__doc__
    #pprint.pprint( dir(f))
    #pprint.pprint( f.__dict__)
    @wraps(f)
    def wrapper(psr_val):

        node_id= psr_val.slice[1]
        anode_type= psr_val.slice[2].value
        
        #print 'Parser node f', node_id.value, node_type.value
        #pprint.pprint({ 'slice' :psr_val.slice,
        #                'stack' : psr_val.stack})
        #pprint.pprint(psr_val.__dict__)
        #pprint.pprint(dir(psr_val))
        i = 0 
        #for x in psr_val.slice :
        #    print "\t\t\tITEM:",i,":", pprint.pformat(x),"Value:",pprint.pformat(get_value(x))
        #    i = i +1
            #, pprint.pformat(dir(x))
            
        r= f(psr_val)
        if anode_type in registry  :
            #print "going to create ", node_type
            cls = registry[anode_type]
            obj = cls(node_id, anode_type, psr_val)
            #print obj
            psr_val[0] = obj
        else:
            #pprint.pprint(registry)
            #print "going to create default", node_type, node_id
            if anode_type not in types:
                types[anode_type]=1
            else:
                types[anode_type]=types[anode_type]+1
            
            psr_val[0] = TNode(node_id, anode_type , psr_val)
        
    wrapper.doc = doc
    return wrapper

def token_rule(f):
    """ 
    token rule
    """
    doc = f.__doc__
    #pprint.pprint( dir(f))
    #pprint.pprint( f.__dict__)
    @wraps(f)
    def wrapper(tok):
        # print 'token function f', f, doc, tok
        # pprint.pprint({ 'lexpos' :tok.lexpos,
        #                 'lineno' :tok.lineno,
        #                 'type' :tok.type,
        #                 'value' :tok.value,
        #                 })

        #pprint.pprint(tok.__dict__)
        #pprint.pprint(dir(tok))
        return f(tok)
    wrapper.doc = doc
    return wrapper

def node_type(name):
    #pprint.pprint(cls)
    #pprint.pprint(name)
    #return cls
    
    class SomeType:
        #the_class =  theclass
        #the_name =  name
        #@classmethod
        # def create( self, tid, node_type, val):
        #     print "Self",self
        #     print "Self.name",self.the_name            
        #     return self.the_class(tid,val)
            
        def __init__(self, theclass):
            #print "init", self
            #print "init", theclass
            #self.the_class = theclass
            registry[name]  =  theclass
    
        #     self.id_name= name
        #     self.theclass = theclass
        #     #node_type, node_id, psr_val
        #     #self.obj = theclass()
        #     #print "Created",self, theclass, name            
        #the_name = name
        
    global  registry   
    # save this class

    
    return SomeType
def report():
    #pprint.pprint( types)
    pprint.pprint( funcs)





def parser_simple_rule(f):
    """ 
    parser simple rule
    """
    doc = f.__doc__
    #pprint.pprint( dir(f))
    #pprint.pprint( f.__dict__)
    @wraps(f)
    def wrapper(psr_val):

        field_name = psr_val.slice[1]
        field_value = psr_val.slice[2]        
        #print 'Parser rule f', field_name, field_value
        #pprint.pprint({ 'slice' :psr_val.slice,
        #                'stack' : psr_val.stack})
        #pprint.pprint(psr_val.__dict__)
        #pprint.pprint(dir(psr_val))
        #i = 0 
        #for x in psr_val.slice :
        #    print "\t\t\tITEM:",i,":", pprint.pformat(x),"Value:",pprint.pformat(get_value(x))
        #    i = i +1
            
        r= f(psr_val)
        # if node_type in registry  :
        #     #print "going to create ", node_type
        #     cls = registry[node_type]
        #     obj = cls(node_id, node_type, psr_val)
        #     #print obj
        #     psr_val[0] = obj
        # else:
        #     #pprint.pprint(registry)
        #     #print "going to create default", node_type
        #     if node_type not in types:
        #         types[node_type]=1
        #     else:
        #         types[node_type]=types[node_type]+1
            
        psr_val[0] = { 'node_type' : f.__name__, 'val' :field_value.value, 'name': field_name.value }
        #print " attr %s" % pprint.pformat( psr_val[0])
        
    wrapper.doc = doc
    return wrapper
