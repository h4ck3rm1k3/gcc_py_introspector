"""
Take a file and extract the lines that are sources
"""
from cache._00089370 import data
from subgraph import *

class SrcP :
    def __init__(self, data):
        self.data =data



def toposort(g):
    # L = Empty list that will contain the sorted elements
    L=[]
    # S = Set of all nodes with no incoming edges
    S={}
    incoming = {}

    # now collect all incoming edge count
    for n in g.nodes(): # 
        nid = n.node_id()
        idx[nid]=n.pos

        tn= n.typename()

        for f in n.fields():
            m = f.value()
            fn = f.name()

            skip = 0 
            #print "seen ",tn, nid, fn, n.pos
            if tn in ('function_decl', 'type_decl', 'var_decl', 'template_decl', 'namespace_decl', 'const_decl', 'using_decl' ) :
                if fn in  'chain' : 
                    #print "skip", tn, fn
                    skip = 1

            if fn in ( 
                    'type',
                    'scpe',  # scope creates a loop
                    'unql') : # unql also
                skip = 1

            if skip == 0 :
                if m in incoming :
                    if nid not in incoming[m]:
                        incoming[m][nid] = fn
                        #print 'incoming', fn, m, nid
                else:
                    incoming[m] = {}
                    incoming[m][nid] = fn
                    #print 'incoming', fn, m, nid

    #print "Incoming:", pprint.pformat(incoming)
    #print "Idx:", pprint.pformat(idx)

    for n in g.nodes():
        nid = n.node_id()
        if nid not in incoming:
            #print nid, "not in incoming"  # this should be only the entry points
            S[nid]=1
            # and here we remove the 
            # for f in n.fields():
            #     m = f.value()
            #     fn = f.name()
            #     #if fn == 'chan':
            #         print 'removing', m, nid
            #         del incoming[m][nid]
                
    while len(S.keys()):

        #print "Keys now",S.keys()
        #print "List now",L

        keys = S.keys()
        first = keys[0]
        del S[first]
        #remove a node n from S

        #add n to tail of L
        if first not in L :
            L.append(first)

            #  for each node m with an edge e from n to m do
            #print "Process %s " % first
            if first in idx :
                fid = idx[first]
                n = g.node(fid)

                #print "N:%s" % n.__dict__
                for m in n.fields():
                    assert(m)
                    #print "field", m.__dict__
                    v = m.value()
                    if v and v in idx:
                        mid = idx[v]
                        #print "check mid offset %s %s" % (v,mid)

                        # remove edge e from the graph
                        if v in incoming:
                            if first in incoming[v]:
                                #print "remove incoming",v,first
                                del incoming[v][first]

                                if len (incoming[v].keys()) == 0:
                                    del incoming[v]

                        #if m has no other incoming edges then
                        if v not in incoming:
                            # insert m into S
                            S[v] = 1    
                            #print "adding v to S", v 
                        else:
                            if len(incoming[v])> 0:
                                #print "v still in in incoming", v, incoming[v]
                                pass
                            else:
                                # insert m into S
                                S[v] = 1    
                                #print "adding v to S", v 
                    else:
                        #print m.__dict__
                        #print "v %s not in idx" % v
                        #S[v] = 1
                        pass
            else:
                print "first not in idx", first

    #print "Leftover",S.keys()
    
    #print "check for left overs"
    if len(incoming.keys()):
        for k in incoming.keys():
            if k :
                if len(incoming[k]) > 0 :
                    #print "Check :" , k, incoming[k]
                    raise Exception("cycle %s" % k)
        #     return error (graph has at least one cycle)
        
    return L # (a topologically sorted order)


# now print the sources in top order
seen = {} 

class Visitor :


    def _print(self, *vals):
        d = "\t" * self.indent
        print d + str(vals)

    def __init__(self):
        self.seen = {}
        self.indent = 0

    def enter(self):
        self.indent = self.indent +1

    def leave(self):
        self.indent = self.indent -1
    
    
class SourceGen:
    class Base:     
        def __init__(self, node, visitor):
            self.node=node
            self.visitor = visitor

        def _print(self, *vals):
            self.visitor._print( vals)

        @classmethod
        def register(clz):
#            self._print clz.__name__
#            self._print clz.__dict__
#            self._print "reg",clz.CLASS,clz
            Node.TypeNames[clz.CLASS]=clz

        def resolve(self, f):
            v = f.resolve()                
            ns = v.specialize(self.visitor)
            self.visitor.enter()
            ns.generate()
            self.visitor.leave()


    class IntegerType (Base) :
        CLASS='integer_type'

        def generate(self):
            self._print("typedef basetype newnode")

    class IntegerCst (Base) :
        CLASS='integer_cst'

        def generate(self):
            self._print("integer const")
            for f in self.node.val_fields():
                if f.name() == 'low':
                    self._print("Value",f.name(), f.value())


    class TemplateTypeParm(Base):
        CLASS='template_type_parm'

        def generate(self):
            self._print("template type param")

    class TemplateDecl(Base):
        CLASS='template_decl'

        def generate(self):
            self._print("template decl")

    class TreeList(Base):
        CLASS='tree_list'

        def generate(self):
            #self._print("\tprocess_list", self.node.id)
            for f in self.node.fields():
             #   self._print( "\tIn List",f.name(), f.value())
                self.resolve(f)
             #   self._print ("\tStill In List")


    class FunctionDecl(Base):
        CLASS='function_decl'

        def generate(self):
            self._print ("void food()")

    class FunctionType(Base):
        CLASS='function_type'

        def generate(self):
            self._print ("void ()()")

    class BooleanType(Base):
        CLASS='boolean_type'

        def generate(self):
            self._print ("bool")

    class TypeDecl(Base):
        CLASS='type_decl'

        def generate(self):
            self._print ("type_decl")
    

    class IdentifierNode(Base):
        CLASS='identifier_node'

        def generate(self):
            for f in self.node.val_fields():
                if f.name() == 'String':
                    self._print( "Identifer",f.name(), f.value())

    class RecordType(Base):
        CLASS='record_type'

        def generate(self):
            self._print ("record_type")

    class TreeVec(Base):
        CLASS='tree_vec'

        def generate(self):
            self._print ("tree_vec")
            self.visitor.enter()
            for f in self.node.val_fields():
                self._print ("vec",f.name(), f.value())

            for f in self.node.fields():
                self._print ("vec2",f.name(), f.value())
                self.resolve(f)
            self.visitor.leave()


    class BindExpr(Base):
        CLASS='bind_expr'

        def generate(self):
            self._print ("bind_expr")

    class ReturnExpr(Base):
        CLASS='return_expr'

        def generate(self):
            self._print ("return_expr")

    class TruthNotExpr(Base):
        CLASS='truth_not_expr'

        def generate(self):
            self._print ("! truth_not_expr")

    class EqExpr(Base):
        CLASS='eq_expr'

        def generate(self):
            self._print ("== eq_expr")

    class IndirectRef(Base):
        CLASS='indirect_ref'

        def generate(self):
            self._print ("*indirect_ref")

    class ParmDecl(Base):
        CLASS='parm_decl'

        def generate(self):
            self._print ("parm_decl")

    class ReferenceType(Base):
        CLASS='reference_type'

        def generate(self):
            self._print ("reference_type")


    class VoidType(Base):
        CLASS='void_type'

        def generate(self):
            self._print ("void")

def walk_topo(g):   
    for x in toposort(g):
        #self._print x
        n = g.node(idx[x])

        ns = n.specialize()
        ns.generate()

def walk(g):   
    v = Visitor()
    for n in g.nodes():
        v._print ("Next in visit")
        ns = n.specialize(v)
        ns.generate()


from types import ClassType

for x in SourceGen.__dict__:
    v = SourceGen.__dict__[x]
    if isinstance(v, ClassType ):
        #self._print "CHeck",x, type(v),v
        if x != 'Base':
            v.register()


import pprint
g = Graph(data)

walk(g)
