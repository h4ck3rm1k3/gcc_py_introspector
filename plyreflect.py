# reflection for ply
import inspect
import tu
import tuparser
import pprint
import ply
import sys

class Module:
    def __init__(self, module):
        _items = [(k, getattr(module, k)) for k in dir(module)]
        self._dict = dict(_items)


tokens= {}
for l in tu.g_lex.lexre:
    (pattern,xlist) = l 
    for b in xlist :
        if (b):
            (f,t)=b
            tokens[t]=f
            # pprint.pprint({
            #     'token': t,
            #     'fun': f.__dict__,            
            # }) # the global lexer

class Lexer(Module):
    def __init__(self, module):
        Module.__init__(self,module)
        self.linfo = ply.lex.LexerReflect(self._dict)
        self.linfo.get_all()
        for n in self.linfo.tokens:
            #pprint.pprint({"t": n})
            pass
        #for x in self.linfo.stateinfo:

        for state in self.linfo.funcsym:
            pprint.pprint({ "state":state })
            for fname, f in self.linfo.funcsym[state]:
                line = f.__code__.co_firstlineno
                _file = f.__code__.co_filename
                # pprint.pprint ({
                #          'fname': fname,
                #          'state': state,
                #          'doc': f.__doc__,
                #          'fd': f.__dict__
                #  })
                
            # pprint.pprint({
            #     #"linfo": self.linfo,
            #     #"dic"  : self.linfo.__dict__
            #     lexobj.lextokens
            # })

class Parser(Module):
    def __init__(self, module):
        Module.__init__(self,module)
        self.pinfo = ply.yacc.ParserReflect(self._dict, log=sys.stdout)
        self.pinfo.get_all()
        self._file = inspect.getsourcefile(module)
        self.rules = {}

        for line, _module, name, doc in self.pinfo.pfuncs:
            parsed_g = ply.yacc.parse_grammar(doc, self._file, line)
            for g in parsed_g:
                (g_filename,g_line,g_type,g_tokens) = g
                metadata= {
                    "n": name,
                    "m": _module,
                    'fn': g_filename,
                    'ln': g_line,
                    'type': g_type,
                    'token' : g_tokens,
                    'line': line,
                    'token_meta': [],
                    "g" : g }
                #pprint.pprint(metadata)

                for t in g_tokens:
                    if t in tokens:
                        # pprint.pprint({
                        #     'name': t,
                        #     'token': tokens[t].__dict__,
                        # #'td': t.__dict__
                        # })
                        
                        metadata['token_meta'].append({
                            #'name': t,
                            'token': tokens[t],
                        })
                    else:
                        #print "Token missing %s" % t
                        # matches 
                        metadata['token_meta'].append({
                            #'name': t,
                            'token': None,
                        })
                        
                self.rules[name]=metadata                        

        #pprint({'f' : module.__dict__[name].__dict__})
        #grammar.append((name, g))
        #self.productions = lrtab.lr_productions
        #pprint.pprint({"pdict": pinfo.__dict__})

#global reflection object
lexer  = Lexer(tu)
#exit(0)

parser = Parser(tuparser)


def reflect(rule):
    #pprint.pprint({"rule": rule.__name__})
    return parser.rules[rule.__name__]
