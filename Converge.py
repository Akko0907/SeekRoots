import numpy as np

def check_err(x0,xn,err):
    """ Check error"""

    error = abs(x0-xn)
    if error>=err:
        return True
    else:
        return False

def ZeroExists(f,a,b):
    """Check existence of a zero in the function"""
    I = np.linspace(a,b,100)
    f_vec = f(I)
    
    m = np.any(f_vec<=0)
    n = np.any(f_vec>=0)

    if m and n:
        return True
    else:
        return False

def NumDiff(x_vec,f):
    """Uses finite differences to generate derivatives of f"""
    
    N = len(x_vec)
    dx = x_vec[1:]-x_vec[0:N-1]

    f_vec = f(x_vec)
    df = f_vec[1:]-f_vec[0:N-1]

    del_f = df/dx

    return del_f

def FpConv(g,a,b,pace=0.1):
    """Check convergence of fixed-point method with g function
    in the interval [a,b]"""
    x_vec = np.arange(a,b+pace,pace)
    del_g = NumDiff(x_vec,g)

    if np.all(abs(del_g)<=1):
        return True
    else:
        return False
    
