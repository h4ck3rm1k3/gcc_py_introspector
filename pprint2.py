import pprint as orig

def pprint (*argv,**kvargs):
    raise Exception('')

def pformat (*argv,**kvargs):
    raise Exception('')

def pformat2 (*argv,**kvargs):
    return orig.pformat([argv,kvargs])

def dprint (*argv,**kvargs):
    pass
