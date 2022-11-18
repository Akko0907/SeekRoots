import Converge as cvg
import numpy as np

def ZerosNewton(f,a,b,error):
    """Find function zeros using Newton's secant method"""

    g = lambda xi,xj: xj-f(xj)*(xi-xj)/(f(xi)-f(xj))

    x0 = (2*a+b)/3
    x1 = (a+2*b)/3
    count = 0
    while loop:
        count += 1
        xn = g(x0,x1)
        loop = cvg.check_err(x1,xn,error)
        x1 = xn
        x0 = x1
        if count > 300:
            print("count exceeded 300 for some reason,breaking")
            return None
    return xn
