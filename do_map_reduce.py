def f(x):
    return x*x
r=map(f,list(range(1,10)))
print(r)
print(list(r))

def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce

def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    s1=[]
    for n in s:
        s1.append(n)
    n=s1.index('.')
    s1.pop(n)
    def x(x):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x]
    def xy(x,y):
        return x*10+y
    return reduce(xy,list(map(x,s1)))/(10**n)
print('str2float(\'123.456\') =', str2float('123.456'))