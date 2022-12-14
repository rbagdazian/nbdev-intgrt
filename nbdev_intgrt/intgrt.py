# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_intgrt.ipynb.

# %% auto 0
__all__ = ['intgrt']

# %% ../00_intgrt.ipynb 3
def intgrt(func, # function or method representing the curve being integrated
           lbnd:float, # lower bound of integration
           ubnd:float, # upper bound of integration
           intvl:float): # value to be used for 'dx'
    """This function performs a numeric integration using a simple summation approach"""
    sumx =0
    lside=lbnd
    rside=lbnd+intvl
    while(rside<ubnd):
        avgval = (func(lside) + func(rside))/2
        dx = (rside-lside)
        sumx = sumx + (dx*avgval)
        lside = lside + intvl
        rside = rside + intvl
        #print(rside,ubnd)
    return sumx
