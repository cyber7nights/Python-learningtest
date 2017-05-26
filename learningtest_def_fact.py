# -*- coding=utf-8 -*-
def fact(n):
    if n == 1 :
        return 1
    return n*fact(n-1)
print(fact(10))

def fact(n):
    return dev_fact(n,1)
def dev_fact(num,product):
    if num==1:
        return product
    return dev_fact(num-1,product*num)
print(fact(10))