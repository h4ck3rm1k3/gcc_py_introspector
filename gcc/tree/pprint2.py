import pprint as orig

def pprint (*argv,**kvargs):
    #raise Exception('')
    return orig.pprint([argv,kvargs])

def pformat (*argv,**kvargs):
    #raise Exception('')
    return orig.pformat([argv,kvargs])
    
def pformat2 (*argv,**kvargs):
    return orig.pformat([argv,kvargs])

def dprint (*argv,**kvargs):
    pass
