from functools import wraps
from gcc.tree.pprint2 import *
import ply.lex as lex
from gcc.tree.nodes import attrs, declare, reference
from gcc.tree.debug import debug, debug2, debug4
from gcc.tree.tnode import TNode

#funcs = {}
import pprint

def get_value(x):
    #pprint.pprint({"get value":x})
    if 'value' in x.__dict__:        
        return x.value
    else:
        return None
        

def parser_rule(f):
    """
    parser rule
    """
    doc = f.__doc__
    #debug(pprint2.pformat( dir(f)))
    #debug(pprint2.pformat( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):

        #if len(psr_val.stack) ==  1:
        debug( 'Parser f', f, doc)
        #funcs[f]=1
        debug2(pformat2({ 'slice' :psr_val.slice,
                        'stack' : psr_val.stack}))
        debug2(pformat2(psr_val.__dict__))
        #rpprint(dir(psr_val))
        i = 0

        debug2( psr_val)

        for x in psr_val.slice[1:] :
            #pprint.pprint(x)
            debug2( "\t\t\tITEM:",i,":", pformat2(x),"Value:",pformat2(get_value(x)))
            #attrs(get_value(x))
            
            i = i +1
        #         #, pformat(dir(x))
        r= f(psr_val)
        x =psr_val.slice[0]
        debug2( "\t\t\tresult:",i,":", pformat2(x),"Value:",pformat2(get_value(x)))
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
    #debug( 'Parser f', f, doc)
    #debug(pformat( dir(f)))
    #debug(pformat( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):

        debug2( 'Parser node f', f)
        
        anode_type= psr_val.slice[2].value

        debug(pformat2({ 'slice' :psr_val.slice,
                                               'stack' : psr_val.stack}))
        debug(pformat2(psr_val.__dict__))
        #debug(pformat(dir(psr_val)))
        i = 0
        for x in psr_val.slice :
            debug2(
                "\t\t\tSLICE ITEM:",
                i,
                ":",
                pformat2(x),
                "Value:",
                pformat2(get_value(x)))
            i = i +1
            #pformat(dir(x))
            
        node_id= declare(psr_val.slice[1])
        debug( 'Parser node f', node_id, anode_type)

        r= f(psr_val)
        if anode_type in registry  :
            debug( "going to create ", anode_type)
            cls = registry[anode_type]
            obj = cls(node_id, anode_type, psr_val)
            psr_val[0] = obj
        else:
            debug(pformat2(registry))
            debug( "going to create default", anode_type, node_id)
            if anode_type not in types:
                types[anode_type]=1
            else:

                types[anode_type]=types[anode_type]+1
            psr_val[0] = {
                'node_decl': node_id,
                'type': anode_type ,
                #'body': psr_val
            }

        
        debug(pformat2(psr_val[0]))
        
    wrapper.doc = doc
    return wrapper

def token_rule(f):
    """
    token rule
    """
    doc = f.__doc__

    # debug(pformat({
    #     'token decl function f': f,
    #     'doc': doc,
    #     'dict' : f.__dict__
    #     }))

    @wraps(f)
    def wrapper(tok):
        debug(pformat({
            'call function f': f,
            'doc': doc,
            'tok':tok,
            'lexpos' :tok.lexpos,
            'lineno' :tok.lineno,
            'type' :tok.type,
            'value' :tok.value,
            'dict' : tok.__dict__
        }))
        #debug(pformat2())
        #debug(pformat(dir(tok)))
        r= f(tok)
        if r is None :
            debug4(pformat({
                'none returned f': f,
                'doc': doc,
                'dict' : f.__dict__
            }))
            #raise Exception("None")
        debug({"ret:": r})
        return r
    
    wrapper.doc = doc
    return wrapper

def register(name, theclass):
    registry[name]  =  theclass

# def node_type(name):

#     debug(pprint.pformat({
#         'decl node type function f': name,
#         'name' : name
#         }))
#         def __init__(self, theclass):
#             debug( {
#                 "init": self,
#                 "class": theclass,
#                 'name': name,
#                 })
#             registry[name]  =  theclass
#             #debug( "Created",self, theclass, name)
#         #     self.id_name= name
#         #     self.theclass = theclass
#         #     #node_type, node_id, psr_val
#         #     #self.obj = theclass()    
#         #the_name = name
#     global  registry
#     # save this class
#     return SomeType

def report():
    debug( 'report')
    debug(pformat2( types))
    #debug(pformat2( funcs))

def parser_simple_rule(f):
    """
    parser simple rule
    """
    doc = f.__doc__
    #debug(pformat( dir(f)))
    #debug(pformat( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):
        debug( 'Parser f', f, doc)
        field_name = psr_val.slice[1]
        field_value = psr_val.slice[2]
        debug( 'Parser rule f', field_name, field_value)
        debug(pformat2({ 'slice' :psr_val.slice,
                               'stack' : psr_val.stack}))
        debug(pformat2(psr_val.__dict__))
        
        #debug(pformat(dir(psr_val)))
        #i = 0
        #for x in psr_val.slice :
        #    debug( "\t\t\tITEM:",i,":", pformat(x),"Value:",pformat(get_value(x)))
        #    i = i +1

        r= f(psr_val)
        # if node_type in registry  :
        #     debug( "going to create ", node_type)
        #     cls = registry[node_type]
        #     obj = cls(node_id, node_type, psr_val)
        #     debug( obj)
        #     psr_val[0] = obj
        # else:
        #     debug(pformat(registry))
        #     debug( "going to create default", node_type)
        #     if node_type not in types:
        #         types[node_type]=1
        #     else:
        #         types[node_type]=types[node_type]+1

        psr_val[0] = {
            #'node_type' : f.__name__,
            field_name.value : field_value.value
        }
        debug( " attr %s" % pformat2( psr_val[0]))

    wrapper.doc = doc
    return wrapper

def parser_simple_rule_node(f):
    """
    parser simple rule
    """
    doc = f.__doc__
    #debug(pformat2( dir(f)))
    #debug(pformat2( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):
        debug( 'Parser f', f, doc)
        field_name = psr_val.slice[1]
        field_value = reference(psr_val.slice[2].value,field_name)
        debug( 'Parser rule f', field_name, field_value)
        debug(pformat2({ 'slice' :psr_val.slice,
                               'stack' : psr_val.stack}))
        debug(pformat2(psr_val.__dict__))
        #debug(pformat2(dir(psr_val)))
        #i = 0
        #for x in psr_val.slice :
        #    debug( "\t\t\tITEM:",i,":", pformat2(x),"Value:",pformat2(get_value(x)))
        #    i = i +1

        r= f(psr_val)
        # if node_type in registry  :
        #     debug( "going to create ", node_type))
        #     cls = registry[node_type]
        #     obj = cls(node_id, node_type, psr_val)
        #     debug( obj))
        #     psr_val[0] = obj
        # else:
        #     debug(pformat2(registry)))
        #     debug( "going to create default", node_type))
        #     if node_type not in types:
        #         types[node_type]=1
        #     else:
        #         types[node_type]=types[node_type]+1

        psr_val[0] = { #'node_type' : f.__name__,
            field_name.value : field_value

        }

        #field_value.ref(psr_val[0])

        debug( " attr %s" % pformat2( psr_val[0]))

    wrapper.doc = doc
    return wrapper
