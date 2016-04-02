# reflection for ply
import inspect
import tu
import tuparser
import pprint
import ply
import sys
module = tuparser
_items = [(k, getattr(module, k)) for k in dir(module)]
pdict = dict(_items)
pinfo = ply.yacc.ParserReflect(pdict, log=sys.stdout)
pinfo.get_all()
_file = inspect.getsourcefile(module)

rules = {}

for line, _module, name, doc in pinfo.pfuncs:
    parsed_g = ply.yacc.parse_grammar(doc, _file, line)
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
            "g" : g }
        #pprint.pprint(metadata)
        rules[name]=metadata

        #pprint({'f' : module.__dict__[name].__dict__})
        #grammar.append((name, g))
        
#self.productions = lrtab.lr_productions

#pprint.pprint({"pdict": pinfo.__dict__})

def reflect(rule):
    #pprint.pprint({"rule": rule.__name__})
    return rules[rule.__name__]
