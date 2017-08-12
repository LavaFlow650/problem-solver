from sympy import *
import numbers

# To import: import quadratic

class Quadratic:
    """ This class is a quadratic that evaluates exactly. """
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self,x,_latex=False):
        """ Returns the value of the quadratic at x """
        
        return self.evaluate(x,_latex=_latex)

    def evaluate(self,x,_latex=False):
        """ Returns the value of the quadratic at x """

        if (_latex):
            return latex(self.a*x*x + self.b*x + self.c)
        else:
            return sympify(self.a*x*x + self.b*x + self.c)

    def sympy(self,x='x'):
        """ Returns self in sympified form """

        return sympify("%s*%s**2 + %s*%s + %s" % (self.a,x,self.b,x,self.c))

    def latex(self,x='x'):
        """ Returns self in latex form """

        return latex(expand(self.sympy(x)))

    def vertex(self):
        """ Returns coordinates of vertex as an tuple """

        xpos = self.symmetry_x()

        if (_latex):
            return (latex(xpos), latex(self(xpos)))
        else:
            return (xpos, self(xpos))

    def discriminant(self,_latex=False):
        """ Returns the discriminant of the quadratic """

        if (_latex):
            return latex(sympify(self.b**2-4*self.a*self.c))
        else:
            return sympify(self.b**2-4*self.a*self.c)

    def roots(self,_latex=False,simplified=True):
        """ Returns the roots of the quadratic """

        x = symbols('x')

        if (_latex):
            return [latex(root) for root in solve(Eq(self.sympy('x'),0))]
        else:
            return solve(Eq(self.sympy('x'),0))

    def symmetry_x(self,_latex=False):
        """ Returns the x position of the axis symmetry of the quadratic """

        if (_latex):
            return latex(sympify(-0.5 * self.b/float(self.a)))
        else:
            return sympify(-0.5 * self.b/float(self.a))

    def symmetry_line(self,_latex=False,x='x'):
        """ Returns the axis of symmetry of the quadratic """

        return "%s = %s" % (x, str(self.symmetry_x(_latex=_latex)))

    def derivative(self,_latex=True,evaluated=True,x='x'):
        """ Returns the derivative of the quadratic, evaluates it if evaluated == true """

        k = symbols('k')

        if (evaluated):
            if (_latex):
                return latex(diff(self.sympy('k'),k)).replace('k',x)
            else:
                return str(diff(self.sympy('k'),k)).replace('k',x)
        else:
            if (_latex):
                return "\\frac{d}{d%s}\\left(%s\\right)" % (x,self.latex(x=x))
            else:
                return None

    def antiderivative(self,_latex=True,evaluated=True,x='x'):
        """ Returns the derivative of the quadratic, evaluates it if evaluated == true """

        k = symbols('k')

        if (evaluated):
            if (_latex):
                return latex(integrate(self.sympy('k'), k)).replace('k', x)
            else:
                return str(integrate(self.sympy('k'), k)).replace('k', x)
        else:
            if (_latex):
                return "\\int %s \\text{ }d%s" % (self.latex(x=x), x)
            else:
                return None

class NQuadratic:
    """ This class is a quadratic that evaluates numerically, not exactly. """
    def __init__(self,a,b,c):

        assert all([isinstance(k,numbers.Number) for k in [a,b,c]])
        self.a = a
        self.b = b
        self.c = c

    def __call__(self,x):
        """ Returns the value of the quadratic at x """

        return self.evaluate(x)

    def evaluate(self,x):
        """ Returns the value of the quadratic at x """

        return self.a*x*x + self.b*x + self.c

    def sympy(self,x='x'):
        """ Returns self in sympified form """

        return sympify("%s*%s**2 + %s*%s + %s" % (self.a,x,self.b,x,self.c))

    def latex(self,x='x'):
        """ Returns self in latex form """

        return latex(simplify(self.sympy(x)))

    def vertex(self):
        """ Returns coordinates of vertex as an tuple """

        xpos = self.symmetry_x()

        if (_latex):
            return (latex(xpos), latex(self(xpos)))
        else:
            return (xpos, self(xpos))

    def discriminant(self,_latex=False):
        """ Returns the discriminant of the quadratic """

        if (_latex):
            return latex(sympify(self.b**2-4*self.a*self.c))
        else:
            return self.b**2-4*self.a*self.c

    def roots(self,_latex=False,simplified=True):
        """ Returns the roots of the quadratic """

        x = symbols('x')

        if (_latex):
            return [latex(root) for root in solve(Eq(self.sympy('x'),0))]
        else:
            roots = []
            for root in solve(Eq(self.sympy('x'),0)):
                try:
                    roots.append(float(root))
                except TypeError:
                    roots.append(complex(root))
            return roots

    def symmetry_x(self,_latex=False):
        """ Returns the x position of the axis symmetry of the quadratic """

        if (_latex):
            return latex(sympify(-0.5 * self.b/float(self.a)))
        else:
            return -0.5 * self.b/float(self.a)

    def symmetry_line(self,_latex=False,x='x'):
        """ Returns the axis of symmetry of the quadratic """

        return "%s = %s" % (x, str(self.symmetry_x(_latex=_latex)))

    def derivative(self,_latex=True,evaluated=True,x='x'):
        """ Returns the derivative of the quadratic, evaluates it if evaluated == true """

        k = symbols('k')

        if (evaluated):
            if (_latex):
                return latex(diff(self.sympy('k'),k)).replace('k',x)
            else:
                return str(diff(self.sympy('k'),k)).replace('k',x)
        else:
            if (_latex):
                return "\\frac{d}{d%s}\\left(%s\\right)" % (x,self.latex(x=x))
            else:
                return None

    def antiderivative(self,_latex=True,evaluated=True,x='x'):
        """ Returns the derivative of the quadratic, evaluates it if evaluated == true """

        k = symbols('k')

        if (evaluated):
            if (_latex):
                return latex(integrate(self.sympy('k'), k)).replace('k', x)
            else:
                return str(integrate(self.sympy('k'), k)).replace('k', x)
        else:
            if (_latex):
                return "\\int %s \\text{ }d%s" % (self.latex(x=x), x)
            else:
                return None

def factor_quadratic(q,x='x',_latex=True):
    """ Factors the quadratic """
    k = symbols('k')

    if (_latex):
        return latex(factor(q.sympy('k'),extension=[I])).replace('k',x)
    else:
        return str(factor(q.sympy('k'),extension=[I])).replace('k',x)

from sympy import *
import numbers

class Cubic:
    """ This class is a cubic that evaluates exactly. """
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __call__(self,x,_latex=False):
        """ Returns the value of the cubic at x """

        return self.evaluate(x,_latex=_latex)

    def evaluate(self,x,_latex=False):
        """ Returns the value of the cubic at x """

        if (_latex):
            return latex(self.a*x*x*x + self.b*x*x + self.c*x + self.d)
        else:
            return sympify(self.a*x*x*x + self.b*x*x + self.c*x + self.d)

    def sympy(self,x='x'):
        """ Returns self in sympified form """

        return sympify("(%s)*%s**3 + (%s)*%s**2 + (%s)*%s + %s" % (self.a,x,self.b,x,self.c,x,self.d))

    def latex(self,x='x'):
        """ Returns self in latex form """

        return latex(simplify(self.sympy(x)))

    def inflection_point(self,_latex=False):
        """ Returns coordinates of inflection point as an tuple """

        xpos = self.inflection_x()

        if (_latex):
            return (latex(xpos), latex(self(xpos)))
        else:
            return (xpos, self(xpos))

    def discriminant(self,_latex=False):
        """ Returns the discriminant of the cubic """

        a = self.a
        b = self.b
        c = self.c
        d = self.d

        if (_latex):
            return latex(sympify(b*b*c*c-4*a*c*c*c-4*b*b*b*d-27*a*a*d*d+18*a*b*c*d))
        else:
            return sympify(b*b*c*c-4*a*c*c*c-4*b*b*b*d-27*a*a*d*d+18*a*b*c*d)

    def roots(self,_latex=False,simplified=True):
        """ Returns the roots of the cubic """

        x = symbols('x')

        if (_latex):
            return [latex(root) for root in solve(Eq(self.sympy('x'),0))]
        else:
            return solve(Eq(self.sympy('x'),0))

    def inflection_x(self,_latex=False):
        """ Returns the x position of the inflection point of the cubic """

        if (_latex):
            return latex(sympify(-self.b/(3*self.a)))
        else:
            return sympify(-self.b/(3*self.a))

    def derivative(self,_latex=True,evaluated=True,x='x'):
        """ Returns the derivative of the cubic, evaluates it if evaluated == true """

        k = symbols('k')

        if (evaluated):
            if (_latex):
                return latex(diff(self.sympy('k'),k)).replace('k',x)
            else:
                return str(diff(self.sympy('k'),k)).replace('k',x)
        else:
            if (_latex):
                return "\\frac{d}{d%s}\\left(%s\\right)" % (x,self.latex(x=x))
            else:
                return None

    def antiderivative(self,_latex=True,evaluated=True,x='x'):
        """ Returns the derivative of the cubic, evaluates it if evaluated == true """

        k = symbols('k')

        if (evaluated):
            if (_latex):
                return latex(integrate(self.sympy('k'), k)).replace('k', x)
            else:
                return str(integrate(self.sympy('k'), k)).replace('k', x)
        else:
            if (_latex):
                return "\\int %s \\text{ }d%s" % (self.latex(x=x), x)
            else:
                return None

class NCubic:
    """ This class is a cubic which evaluates numerically. """
    def __init__(self,a,b,c,d):

        assert all([isinstance(k, numbers.Number) for k in [a, b, c]])
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __call__(self,x,_latex=False):
        """ Returns the value of the cubic at x """

        return self.evaluate(x,_latex=_latex)

    def evaluate(self,x,_latex=False):
        """ Returns the value of the cubic at x """

        if (_latex):
            return latex(self.a*x*x*x + self.b*x*x + self.c*x + self.d)
        else:
            return self.a*x*x*x + self.b*x*x + self.c*x + self.d

    def sympy(self,x='x'):
        """ Returns self in sympified form """

        return sympify("(%s)*%s**3 + (%s)*%s**2 + (%s)*%s + %s" % (self.a,x,self.b,x,self.c,x,self.d))

    def latex(self,x='x'):
        """ Returns self in latex form """

        return latex(simplify(self.sympy(x)))

    def inflection_point(self,_latex=False):
        """ Returns coordinates of inflection point as an tuple """

        xpos = self.inflection_x()

        if (_latex):
            return (latex(xpos), latex(self(xpos)))
        else:
            return (xpos, self(xpos))

    def discriminant(self,_latex=False):
        """ Returns the discriminant of the cubic """

        a = self.a
        b = self.b
        c = self.c
        d = self.d

        if (_latex):
            return latex(sympify(b*b*c*c-4*a*c*c*c-4*b*b*b*d-27*a*a*d*d+18*a*b*c*d))
        else:
            return b*b*c*c-4*a*c*c*c-4*b*b*b*d-27*a*a*d*d+18*a*b*c*d

    def roots(self,_latex=False,simplified=True):
        """ Returns the roots of the cubic """

        x = symbols('x')

        if (_latex):
            return [latex(root) for root in solve(Eq(self.sympy('x'),0))]
        else:
            roots = []

            for root in solve(Eq(self.sympy('x'),0)):
                try:
                    roots.append(float(root))
                except TypeError:
                    roots.append(complex(root))

            return roots

    def inflection_x(self,_latex=False):
        """ Returns the x position of the inflection point of the cubic """

        if (_latex):
            return latex(sympify(-self.b/(3*self.a)))
        else:
            return -self.b/(3*self.a)

    def derivative(self,_latex=True,evaluated=True,x='x'):
        """ Returns the derivative of the cubic, evaluates it if evaluated == true """

        k = symbols('k')

        if (evaluated):
            if (_latex):
                return latex(diff(self.sympy('k'),k)).replace('k',x)
            else:
                return str(diff(self.sympy('k'),k)).replace('k',x)
        else:
            if (_latex):
                return "\\frac{d}{d%s}\\left(%s\\right)" % (x,self.latex(x=x))
            else:
                return None

    def antiderivative(self,_latex=True,evaluated=True,x='x'):
        """ Returns the derivative of the cubic, evaluates it if evaluated == true """

        k = symbols('k')

        if (evaluated):
            if (_latex):
                return latex(integrate(self.sympy('k'), k)).replace('k', x)
            else:
                return str(integrate(self.sympy('k'), k)).replace('k', x)
        else:
            if (_latex):
                return "\\int %s \\text{ }d%s" % (self.latex(x=x), x)
            else:
                return None
