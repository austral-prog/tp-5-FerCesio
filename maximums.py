def max_of_two (x, y):
    if x>y:
        return x 
    else:
        return y
max_of_two(2, 1)


def max_of_three (x, y, z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
max_of_three(1,-1,3)
