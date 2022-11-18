import Converge as cvg

def Bissec(f,a,b,error):
    """ The function to be analized is 'f', 'a' and 'b' are the interval's
    start and finish"""
    
    x0 = (b+a)/2
    loop = cvg.ZeroExists(f,a,b)
    count = 0
    while loop:    
        count += 1
        if f(x0)*f(x0)<0:
            b = x0
            xn = a+(b-a)/2
            loop = cvg.check_err(x0,xn,error)
        else:
            a = x0
            xn = a+(b-a)/2
            loop = cvg.check_err(x0,xn,error)
        x0 = xn

    if count>0:
        print(f"zero founded at x={xn} in the interval [{a},{b}] within error < {error} in {count} iterations")
        return xn
    else:
        print(f"No zero founded at the interval [{a},{b}]")
        return None

    
