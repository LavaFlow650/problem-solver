from sympy import *
import polynomial

def factor_quadratic(q,x='x',_latex=True):
    """ Factors the quadratic """
    k = symbols('k')

    if (_latex):
        return latex(factor(q.sympy('k'),extension=[I])).replace('k',x)
    else:
        return str(factor(q.sympy('k'),extension=[I])).replace('k',x)
