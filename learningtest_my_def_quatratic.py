import math


def my_quatratic (a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a out of given')
    elif not isinstance(b, (int, float)):
        raise TypeError('b out of given')
    elif not isinstance(c, (int, float)):
        raise TypeError('c out of given')
    elif b**2-4*a*c<0:
        return "该方程无解"
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x=(x1,x2)
        return x
    #解二元一次方程