from functools import wraps
import pprint2
import ply.lex as lex
import nodes
funcs = {}
def debug(*args,**kvargs):
    #pprint2.pprint({'args':args,'kvargs':kvargs})
    pass

class TNode :
    def __init__(self, node_id, node_type, o):
        self.node_id=node_id
        self.node_type=node_type
        self.o=o
    def nid(self):
        return self.node_id.n

    def pstack(self):
        r = ""
        debug( "Stack:%s" % pprint2.pformat(self.o.stack))
        #debug(pprint2.pformat(dir(self.o)))
        #debug(pprint2.pformat(self.o.__dict__))
        for s in self.o.stack:
            if s.type == '$end':
                pass
            else:
                s1= "pstack[type:%s t2:%s value:%s]," % (s.type, type(s.value), s.value.node_id)
                r = r + s1
                debug( "Stack",s,pprint2.pformat(s))
                #debug( "Stack",s,pprint2.pformat(dir(s)))
                debug( "Stack",s,pprint2.pformat(s.__dict__))
        return r
            
    def __repr__(self):
        return "!TNode:id='%s',type:'%s',obj:'%s'!" % (
            self.node_id.n,
            self.node_type,
            'pstack'
            #self.pstack()
            #pprint2.pformat(self.o.__dict__)
        )

def get_value(x):
    if 'value' in x.__dict__:
        return x.value
    else:
        return None
        #return pprint2.pformat(x)

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
        funcs[f]=1
        debug(pprint2.pformat2({ 'slice' :psr_val.slice,
                        'stack' : psr_val.stack}))
        debug(pprint2.pformat2(psr_val.__dict__))
        #rpprint2.pprint(dir(psr_val))
        i = 0

        # if isinstance(psr_val,lex.LexToken):
        debug( psr_val)
        #     pass
        # else:

        for x in psr_val.slice[1:] :
            debug( "\t\t\tITEM:",i,":", pprint2.pformat2(x),"Value:",pprint2.pformat2(get_value(x)))
            nodes.attrs(get_value(x))
            
            i = i +1
        #         #, pprint2.pformat(dir(x))
        r= f(psr_val)
        x =psr_val.slice[0]
        debug( "\t\t\tresult:",i,":", pprint2.pformat2(x),"Value:",pprint2.pformat2(get_value(x)))
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
    #debug(pprint2.pformat( dir(f)))
    #("['__call__',\n '__class__',\n '__closure__',\n '__code__',\n '__defaults__',\n '__delattr__',\n '__dict__',\n '__doc__',\n '__format__',\n '__get__',\n '__getattribute__',\n '__globals__',\n '__hash__',\n '__init__',\n '__module__',\n '__name__',\n '__new__',\n '__reduce__',\n '__reduce_ex__',\n '__repr__',\n '__setattr__',\n '__sizeof__',\n '__str__',\n '__subclasshook__',\n 'func_closure',\n 'func_code',\n 'func_defaults',\n 'func_dict',\n 'func_doc',\n 'func_globals',\n 'func_name']",)
    #debug(pprint2.pformat( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):

        node_id= nodes.declare(psr_val.slice[1])
        anode_type= psr_val.slice[2].value

        debug( 'Parser node f', node_id, node_type)
        debug(pprint2.pformat2({ 'slice' :psr_val.slice,
                                               'stack' : psr_val.stack}))
        debug(pprint2.pformat2(psr_val.__dict__))
        #debug(pprint2.pformat(dir(psr_val)))
        i = 0
        #for x in psr_val.slice :
        #    debug( "\t\t\tITEM:",i,":", pprint2.pformat(x),"Value:",pprint2.pformat(get_value(x)))
        #    i = i +1
            #, pprint2.pformat(dir(x))

        r= f(psr_val)
        if anode_type in registry  :
            debug( "going to create ", node_type)
            cls = registry[anode_type]
            obj = cls(node_id, anode_type, psr_val)
            debug( obj)
            psr_val[0] = obj
        else:
            debug(pprint2.pformat2(registry))
            debug( "going to create default", node_type, node_id)
            if anode_type not in types:
                types[anode_type]=1
            else:
                types[anode_type]=types[anode_type]+1

            psr_val[0] = TNode(node_id, anode_type , psr_val)

        debug(pprint2.pformat2(psr_val[0]))

    wrapper.doc = doc
    return wrapper

def token_rule(f):
    """
    token rule
    """
    doc = f.__doc__
    #debug(pprint2.pformat( dir(f)))
    #debug(pprint2.pformat( f.__dict__))
    @wraps(f)
    def wrapper(tok):
        # debug( 'token function f', f, doc, tok)
        # debug(pprint2.pformat({ 'lexpos' :tok.lexpos,
        #                 'lineno' :tok.lineno,
        #                 'type' :tok.type,
        #                 'value' :tok.value,
        #                 }))

        debug(pprint2.pformat2(tok.__dict__))
        #debug(pprint2.pformat(dir(tok)))
        return f(tok)
    wrapper.doc = doc
    return wrapper

def node_type(name):
    #debug(pprint2.pformat(cls))
    #debug(pprint2.pformat(name))
    #return cls

    class SomeType:
        #the_class =  theclass
        #the_name =  name
        #@classmethod
        # def create( self, tid, node_type, val):
        #     debug( "Self",self)
        #     debug( "Self.name",self.the_name)
        #     return self.the_class(tid,val)

        def __init__(self, theclass):
            debug( "init", self)
            debug( "init", theclass)
            #self.the_class = theclass
            registry[name]  =  theclass
            debug( "Created",self, theclass, name)
        #     self.id_name= name
        #     self.theclass = theclass
        #     #node_type, node_id, psr_val
        #     #self.obj = theclass()
    
        #the_name = name
    global  registry
    # save this class
    return SomeType

def report():
    debug( 'report')
    debug(pprint2.pformat2( types))
    debug(pprint2.pformat2( funcs))

def parser_simple_rule(f):
    """
    parser simple rule
    """
    doc = f.__doc__
    #debug(pprint2.pformat( dir(f)))
    #debug(pprint2.pformat( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):

        field_name = psr_val.slice[1]
        field_value = psr_val.slice[2]
        debug( 'Parser rule f', field_name, field_value)
        debug(pprint2.pformat2({ 'slice' :psr_val.slice,
                               'stack' : psr_val.stack}))
        debug(pprint2.pformat2(psr_val.__dict__))
        #debug(pprint2.pformat(dir(psr_val)))
        #i = 0
        #for x in psr_val.slice :
        #    debug( "\t\t\tITEM:",i,":", pprint2.pformat(x),"Value:",pprint2.pformat(get_value(x)))
        #    i = i +1

        r= f(psr_val)
        # if node_type in registry  :
        #     debug( "going to create ", node_type)
        #     cls = registry[node_type]
        #     obj = cls(node_id, node_type, psr_val)
        #     debug( obj)
        #     psr_val[0] = obj
        # else:
        #     debug(pprint2.pformat(registry))
        #     debug( "going to create default", node_type)
        #     if node_type not in types:
        #         types[node_type]=1
        #     else:
        #         types[node_type]=types[node_type]+1

        psr_val[0] = { 'node_type' : f.__name__, 'val' :field_value.value, 'name': field_name.value }
        debug( " attr %s" % pprint2.pformat2( psr_val[0]))

    wrapper.doc = doc
    return wrapper

def parser_simple_rule_node(f):
    """
    parser simple rule
    """
    doc = f.__doc__
    #debug(pprint2.pformat2( dir(f)))
    #debug(pprint2.pformat2( f.__dict__))
    @wraps(f)
    def wrapper(psr_val):

        field_name = psr_val.slice[1]
        field_value = nodes.reference(psr_val.slice[2].value,field_name)
        debug( 'Parser rule f', field_name, field_value)
        debug(pprint2.pformat2({ 'slice' :psr_val.slice,
                               'stack' : psr_val.stack}))
        debug(pprint2.pformat2(psr_val.__dict__))
        #debug(pprint2.pformat2(dir(psr_val)))
        #i = 0
        #for x in psr_val.slice :
        #    debug( "\t\t\tITEM:",i,":", pprint2.pformat2(x),"Value:",pprint2.pformat2(get_value(x)))
        #    i = i +1

        r= f(psr_val)
        # if node_type in registry  :
        #     debug( "going to create ", node_type))
        #     cls = registry[node_type]
        #     obj = cls(node_id, node_type, psr_val)
        #     debug( obj))
        #     psr_val[0] = obj
        # else:
        #     debug(pprint2.pformat2(registry)))
        #     debug( "going to create default", node_type))
        #     if node_type not in types:
        #         types[node_type]=1
        #     else:
        #         types[node_type]=types[node_type]+1

        psr_val[0] = { 'node_type' : f.__name__, 'val' :field_value, 'name': field_name.value }

        #field_value.ref(psr_val[0])

        debug( " attr %s" % pprint2.pformat2( psr_val[0]))

    wrapper.doc = doc
    return wrapper
