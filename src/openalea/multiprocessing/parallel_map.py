from types import FunctionType

def parallel_map(function, seq):
    '''    
    '''
    from ipyparallel import Client
    rc = Client() # remote client

    dview = rc[:]
    #lview.block = True

    if function and seq:
        return ( dview.map_sync(function, seq), )
    else:
        return ( [], )

