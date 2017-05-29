# -*- coding=utf-8 -*-

def calc_sum(*arge):
    ax=0
    for i in arge:
        ax=i+ax
    return ax
print(calc_sum(1,3,5))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f=lazy_sum(1,2,3,4)
print('>>>>',f)
print(lazy_sum(1,2,3,4))#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
print(f(),'<<<<')#调用函数f时，才真正计算求和的结果：

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
print(list(count()))
f1,f2,f3=count()
print(f1,f2,f3)
print(f1(),f2(),f3())
#注意三者print变化

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i 的当前值被传入f()
    return fs

# 一个函数可以返回一个计算结果，也可以返回一个函数。
#
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

def now():
    print('2017-5-29')
now