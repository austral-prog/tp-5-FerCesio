import math
def roots(a, b, c):
    if (b**2-4*a*c)>=0:
        root1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        root2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        if root1 != root2:
            return f"({root1}, {root2})"
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
    if a != 0 and b != 0 and c != 0:
        y = f"f(x) = {a} * X^2 + {b} * X + {c}"
        return y
    elif b == 0 and c != 0 and a != 0:
        s = f"f(x) = {a} * X^2 + {c}"
        return s
    elif c == 0 and b != 0 and a != 0:
        j = f"f(x) = {a} * X^2 + {b} * X"
        return j
    elif a == 0 and c != 0 and b != 0:
        t = f"f(x) = {b} * X + {c}"
        return t 
    elif a != 0 and b == 0 and c == 0:
        l = f"f(x) = {a} * X^2"
        return l 
    elif a == 0 and b != 0 and c == 0:
        p = f"f(x) = {b} * X"
        return p
    elif a == 0 and b == 0 and c != 0:
        u = f"f(x) = {c}"
        return u 
    else:
        return "f(x) = 0"
to_string(-2,0,1)

def derivation(a,b,c):
    if 2*a == 0:
        y = f"f'(x) = {b}"
        return y
    else:
        if b != 0:
            d = f"f'(x) = {2*a} * X + {b}"
            return d
        else:
            g = f"f'(x) = {2*a} * X"
            return g
derivation(2, -3, 1)
