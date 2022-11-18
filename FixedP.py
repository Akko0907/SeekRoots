import Converge as cvg
import numpy as np

def FixedP(g,a,b,error,loop=False):
    """ Receives a function g(x), transformed from f(x)=0 into x=g(x) """

    if loop==False:
        loop = cvg.FpConv(g,a,b)
    else:
        loop = True

    x0 = (b+a)/2
    count = 0
    while loop:
        count += 1
        xn = g(x0)
        loop = cvg.check_err(x0,xn,error)
        x0 = xn
        if count > 300:
            print("count exceeded 300 for some reason,breaking (did you check its convergence?)")
            return None

    if count==0:
        print(f"Convergence not guarantee")
        return None
    
    else: 
        print(f"zero founded at x={xn} in the interval [{a},{b}] within error < {error} in {count} iterations")
        return xn


