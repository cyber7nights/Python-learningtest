# -*- coding=utf-8 -*-
from learningtest_my_def_quatratic import my_quatratic

print(my_quatratic(2,3,1))

print('默认参数的bug')
def nextyear_age(age=[]):
    age.append(1)
    return age
print(nextyear_age())
print(nextyear_age())
print(nextyear_age())
print(nextyear_age())
print(nextyear_age([0]))  #默认参数必须指向不变参数

print('可变参数的内外部list组装问题')
def calc(nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
print(calc((1,2,3)))#可变参数，在函数外部组装成为list或者tuple。

def calc(*nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
print(calc(1,2,3))#可变参数，在函数内部通过*组装成为list或者tuple

def calc(nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
sum2=(1,2,3,4,5)
print(calc(sum2))#已经有list或者tuple，可变参数，在函数内部可变参数应该与函数外部参数相同。

def calc(*nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
sum2=(1,2,3,4,5)
print(calc(*sum2))#已经有list或者tuple，可变参数，在函数内部可变参数应该与函数外部参数相同。

print('关键字参数')
