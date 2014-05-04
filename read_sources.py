"""
Take a file and extract the lines that are sources
"""
from cache._00089370 import data
from subgraph import *

class SrcP :
    def __init__(self, data):
        self.data =data


# now print the sources in top order
seen = {} 

class Visitor :

    def _print(self, *vals):
        d = "  " * self.indent
        if isinstance(vals, str):
            print d + vals
        elif isinstance(vals[0], tuple):
            #print type(vals)
            print d + ",".join(*vals)
        elif isinstance(vals[0], str):
            print d + vals[0]
        else:
            print type(vals)
            print d + pprint.pformat(*vals)

    def __init__(self):
        self._seen = {}
        self.indent = 0
        

    def enter(self):
        self.indent = self.indent +1

    def leave(self):
        self.indent = self.indent -1

    def seen(self, node):
        nid = node.node.node_id()
        if nid not in self._seen:
            #self._print ("not seen %s" % nid)
            self._seen[nid]=1
            return False
        else:
            #self._print("dup seen %s" % nid)
            return True

class SourceGen:

    class Base:     
        def __init__(self, node, visitor):
            self.node=node
            self.visitor = visitor
            #visitor._print("Node %s %s" % (self.node.node_id(),self.node.typename()) )
            
        def _print(self, *vals):
            self.visitor._print( vals)

        def visit_scalars(self):
            self.visitor.enter()
            for f in self.node.val_fields():
                self._print("%s=%s" % (f.name(), f.value()))
            self.visitor.leave()

        def reference(self):
            self.visitor._print("Reference to Node: %s %s" % (self.node.node_id(),self.node.typename(),))
            self.emit_reference()
            #self.visit_scalars()

        def visit_attrs(self):
            self.visitor.enter()
            self.visit_scalars()

            for f in self.node.fields():
                fn = f.name()

                if fn not in ("scpe","chain"):
                    self._print ("base_ref: %s %s" % (f.name(), f.value()))
                    self.visitor.enter()
                    # recurse into the field
                    self.resolve(f)
                    self.visitor.leave()
                else:
                    #self._print ("Skip",f.name(), f.value())
                    pass
                    
            self.visitor.leave()

        def visit_attrs_simple(self):
            self.visitor.enter()

            for f in self.node.fields():
                fn = f.name()

                if fn not in ("scpe","chain"):
                    self._print ("base_ref %s %s" % (f.name(), f.value()))
                else:
                    self._print ("Skip",f.name(), f.value())
                    
            self.visitor.leave()

        def visit_chain(self):
            self.visitor.enter()
            for f in self.node.fields():
                fn = f.name()
                if fn in ("chain"):
                    self._print ("chain",f.name(), f.value())
                    self.visitor.enter()
                    self.resolve(f)

                    self.visitor.leave()
            self.visitor.leave()

        @classmethod
        def register(clz):
#            self._print clz.__name__
#            self._print clz.__dict__
#            self._print "reg",clz.CLASS,clz
            Node.TypeNames[clz.CLASS]=clz

        def resolve(self, f):
            v = f.resolve()                
            #TODO check if not seen already, only resolve onces
            if (v):
                ns = v.specialize(self.visitor)

                self.visitor.enter()

                if not self.visitor.seen(ns):
                    # if not seen generate the full object
                    ns.generate()
                else:
                    # otherwise reference the existing object
                    ns.reference()

                self.visitor.leave()


    class IntegerType (Base) :
        CLASS='integer_type'

        def generate(self):
            self._print("typedef basetype newnode")
            self.visit_scalars()

    class IntegerCst (Base) :
        CLASS='integer_cst'

        def generate(self):
            self._print("integer const")
            for f in self.node.val_fields():
                if f.name() == 'low':
                    self._print("Value",f.name(), f.value())

        def emit_reference(self):
            self._print("integer const")
            for f in self.node.val_fields():
                if f.name() == 'low':
                    self._print("Value",f.name(), f.value())


    class TemplateTypeParm(Base):
        CLASS='template_type_parm'

        def generate(self):
            self._print("template type param")
            self.visit_attrs()

    class TemplateDecl(Base):
        CLASS='template_decl'

        def generate(self):
            self._print("template decl")
            self.visit_attrs()

    class TreeList(Base):
        CLASS='tree_list'

        def generate(self):
            #self._print("\tprocess_list", self.node.id)
            for f in self.node.fields():
                self._print( "\tIn List",f.name(), f.value())
                self.resolve(f)
             #   self._print ("\tStill In List")


    class FunctionDecl(Base):
        CLASS='function_decl'

        def generate(self):
            self._print ("void food()")
            self.visit_attrs()

    class FunctionType(Base):
        CLASS='function_type'

        def generate(self):
            self._print ("functiontype")
            self.visit_attrs()

        def emit_reference(self):
            for f in self.node.fields():
                if f.name() == 'name':
                    nr = f.resolve()
                    ns =nr.specialize(self.visitor)
                    ns.emit_reference()
                else:
                    self._print( "skip", f.name())


    class BooleanType(Base):
        CLASS='boolean_type'

        def generate(self):
            self._print ("bool")
            self.visit_scalars()

    class TypeDecl(Base):
        CLASS='type_decl'

        def generate(self):
            self._print ("type_decl")
            self.visit_attrs() 
            #self.visit_scalars()
            #self.visit_attrs_simple()

        def emit_reference(self):
            for f in self.node.fields():
                if f.name() == 'name':
                    nr = f.resolve()
                    ns =nr.specialize(self.visitor)
                    ns.emit_reference()
            
    class IdentifierNode(Base):
        CLASS='identifier_node'

        def generate(self):
            self.visit_attrs()

            for f in self.node.val_fields():
                if f.name() == 'String':
                    self._print( "Identifier",f.name(), f.value())

        def emit_reference(self):
            for f in self.node.val_fields():
                if f.name() == 'String':
                    self._print( "Identifer Ref: %s" % f.value())
            

    class RecordType(Base):
        """
        class for structs, classes and unions 
        """
        CLASS='record_type'

        def generate(self):
            self._print ("record_type")
            self.visit_attrs()
            self.visit_attrs_simple()

        def emit_reference(self):
            for f in self.node.fields():
                if f.name() == 'name':
                    nr = f.resolve()
                    ns =nr.specialize(self.visitor)
                    ns.emit_reference()

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
            self.visit_attrs()

    class ReturnExpr(Base):
        CLASS='return_expr'

        def generate(self):
            self._print ("return_expr")
            self.visit_attrs()

    class TruthNotExpr(Base):
        CLASS='truth_not_expr'

        def generate(self):
            self._print ("! truth_not_expr")
            self.visit_attrs()

    class EqExpr(Base):
        CLASS='eq_expr'

        def generate(self):
            self._print ("== eq_expr")
            self.visit_attrs()

    class IndirectRef(Base):
        CLASS='indirect_ref'

        def generate(self):
            self._print ("*indirect_ref")
            #self.visit_attrs()
            self.visit_scalars()
            self.visit_attrs_simple()
            
    class ParmDecl(Base):
        CLASS='parm_decl'

        def generate(self):
            self._print ("parm_decl")
            self.visit_attrs()
            self.visit_chain()

    class ReferenceType(Base):
        CLASS='reference_type'

        def generate(self):
            self._print ("reference_type")
            self.visit_attrs()

        def emit_reference(self):
            for f in self.node.fields():
                if f.name() == 'name':
                    nr = f.resolve()
                    ns =nr.specialize(self.visitor)
                    ns.emit_reference()
                else:
                    self._print( "skip", f.name())

    class VoidType(Base):
        CLASS='void_type'

        def generate(self):
            self._print ("void")
            self.visit_scalars()

        def emit_reference(self):
            self.generate()

from types import ClassType

# register all the class
for x in SourceGen.__dict__:
    v = SourceGen.__dict__[x]
    if isinstance(v, ClassType ):
        #self._print "CHeck",x, type(v),v
        if x != 'Base':
            v.register()


import pprint
g = Graph(data)
n = g.node(0)
v = Visitor()
v._print("Start Visit %s" % n.node_id())
ns = n.specialize(v)
ns.generate()
