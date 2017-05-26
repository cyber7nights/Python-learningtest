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
print(calc((1,2,3)))#可变参数，在函数外部,参数赋值內组装成为tuple&list。

def calc(*nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
print(calc(1,2,3))#可变参数，在函数内部通过*组装成为tuple&list

def calc(nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
sum2=(1,2,3,4,5)
print(calc(sum2))#已经有tuple&list，可变参数，在函数内部可变参数应该与函数外部参数相同。

def calc(*nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
sum2=(1,2,3,4,5)
print(calc(*sum2))#已经有tuple或者list，可变参数，在函数内部可变参数应该与函数外部参数相同。

print('关键字参数,dict类型参数的内外部组装问题')
def person(num,name, age, **kw):
    print('num:',num,'name:', name, 'age:', age, 'other:', kw)
person(1,'iong',24)
person(2,'iong',24,city='CD')
#1,2函数内组装dict

extra={'job':"engineer",'city':'CD'}
def person(num,name, age, **kw):
    print('num:',num,'''
    age:''',age,'''
    name:''',name,'''
    other:''',kw)
person(3,'iong',24,job=extra['job'],city=extra['city'])
#3函数外部组装dict,参数赋值内组装。本质上与上一条没有任何区别。

extra={'job':"engineer",'city':'CD'}
def person(num,name, age, kw):
    print('num:', num, '''
    age:''', age, '''
    name:''', name, '''
    other:''', kw)
person(4,'iong',24,extra)
#4完全在函数外，参数赋值外组装dict。

extra={'job':"engineer",'city':'CD'}
def person(num,name, age, **kw):
    print('num:', num, '''
    age:''', age, '''
    name:''', name, '''
    other:''', kw)
person(5,'iong',24,**extra)
#5函数外，参数赋值外组装dict

def person(num,name, age, kw):
    print('num:', num, '''
    age:''', age, '''
    name:''', name, '''
    other:''', kw)
person(6,'iong',24,{'job':"engineer",'city':'CD'})
#6函数外，参数赋值內组装dict，同前两条。

#总结可变参数和关键字参数
print('''
总结：tuple&list类型的参数属于可变参数，可以在函数内组装，也可以在函数外组装。同时也能在参数赋值前提前组装。''','''
dict类型的关键字参数同样和可变参数一样''','''
最后：在这两种类型的参数中，不光要考虑函数内的组装，也要考虑参数赋值时的组装，同时还有元组、字典中的元素问题。''','''
    可变参数实际接收的是一个tuple''')

#