import math
def roots(a, b, c):
    if (b**2-4*a*c)>=0:
        root1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        root2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        if root1 != root2:
            return f"({root1},{root2})"
        else:
            return f"({root1})"
    else:
        return "( )"
roots(1,-8,16)

def value_y(a, b, c, x):
    y = a*(x**2)+b*x+c
    return y
value_y(1,-3,2,-1)

def to_string(a, b, c):
    y = f"f(x) = {a} * X^2 + {b} * X + {c}"
    return y 
to_string(2,-3,1)

def derivation(a,b,c):
    if 2*a == 0:
        y = f"f'(x) = {b}"
        return y
    else:
        d = f"f'(x) = {2*a}x + {b}"
        return d
derivation(2, -3, 1)
