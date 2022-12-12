import numpy as np


#========================================================================
#========================================================================


def check_err(x0: float,xn: float,err: float) -> bool:
    """ Check error"""

    error = abs(x0-xn)
    if np.any(error>=err):
        return True
    else:
        return False


#========================================================================
#========================================================================


def check_err2(f: function,xn: float,err: float) -> bool:
    """ Check error"""

    error = abs(f(xn))
    if np.any(error>=err):
        return True
    else:
        return False


#========================================================================
#========================================================================


def ZeroExists(f: function,a: float,b: float) -> bool:
    """Check existence of a zero in the function"""
    I = np.linspace(a,b,100)
    f_vec = f(I)
    
    m = np.any(f_vec<=0)
    n = np.any(f_vec>=0)

    if m and n:
        return True
    else:
        return False


#========================================================================
#========================================================================


def Diff(x_vec: np.ndarray,f: function) -> np.ndarray:
    """Uses finite differences to generate a derivatives table of f"""
    
    N = len(x_vec)
    dx = x_vec[1:]-x_vec[0:N-1]

    f_vec = f(x_vec)
    df = f_vec[1:]-f_vec[0:N-1]

    del_f = df/dx

    return del_f


#========================================================================
#========================================================================


def FpConv(g: function,a: float,b: float,pace: float=0.1) -> bool:
    """Check convergence of fixed-point method with g function
    in the interval [a,b]"""
    
    x_vec = np.arange(a,b+pace,pace)
    del_g = Diff(x_vec,g)

    if np.all(abs(del_g)<=1):
        return True
    else:
        return False
    
