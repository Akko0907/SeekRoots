import FuncRoots.Converge as cvg

#=================================================================================================================
#=================================================================================================================


def Bissec(f: function, a0: float, b0: float,
            x0: float=None, error: float=0.01) -> float:
    """ The function to be analized is 'f', 'a' and 'b' are the interval's
    start and finish. Function must be well behaved! """
    
    if x0==None:
        x0 = (b0+a0)/2
    a_new = a0
    b_new = b0

    loop = cvg.ZeroExists(f,a0,b0)
    count = 0
    while loop:    
        count += 1
        if f(x0)*f(b_new)<0:
            a_new = x0
            xn = a_new+(b_new-a_new)/2
            loop = cvg.check_err(x0,xn,error)
        else:
            b_new = x0
            xn = a_new+(b_new-a_new)/2
            loop = cvg.check_err(x0,xn,error)
        x0 = xn

    if count>0:
        print(f"zero founded at x={xn} in the interval [{a0},{b0}] within error < {error} in {count} iterations")
        return xn
    else:
        print(f"No zero founded at the interval [{a0},{b0}]")
        return None

#=================================================================================================================
#=================================================================================================================


def FixedP(g: function, a: float, b: float,
           x0: float=None, error: float=0.01,
           loop: bool=False, max_count: int=300) -> float:
    """ Receives a function g(x), transformed from f(x)=0 into x=g(x) """

    if loop==False:
        loop = cvg.FpConv(g,a,b)

    if x0==None:
        x0 = (b+a)/2
        
    count = 0
    while loop:
        count += 1
        xn = g(x0)
        loop = cvg.check_err(x0,xn,error)
        x0 = xn
        if count > max_count:
            print(f"count exceeded {max_count} for some reason,breaking (did you check its convergence?)")
            return None

    if count==0:
        print(f"Convergence not guarantee")
        return None
    
    else: 
        print(f"zero founded at x={xn} in the interval [{a},{b}] within error < {error} in {count} iterations")
        return xn

#=================================================================================================================
#=================================================================================================================


def ZerosNewton(f: function,a: float,b: float,
                error: float=0.01, kicks: list=None,
                max_count: int=300) -> float:
                
    """Find function zeros using Newton's secant method"""

    g = lambda xi,xj: xj-f(xj)*(xi-xj)/(f(xi)-f(xj))

    if kicks==None:
        x0 = (2*a+b)/3
        x1 = (a+2*b)/3
    else:
        x0 = kicks[0]
        x1 = kicks[1]

    count = 0
    loop = True
    while loop:
        count += 1
        xn = g(x0,x1)
        loop = cvg.check_err2(f,xn,error)
        x0 = x1
        x1 = xn
        if count > max_count:
            print(f'count exceeded {max_count} for some reason,breaking...')
            return None
    print(f'Zero found in x = {xn} within error = {error}')
    return xn