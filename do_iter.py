#!/usr/bin/python
# -*- coding=utf-8 -*-
#迭代iteration

d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
    # 因为默认dict迭代是key，所以要迭代value要用d.values

for k,v in d.items():
    print(k,v)

from collections import Iterable
isinstance('abc',Iterable)#str是否可以迭代 ,是
isinstance([1,2,3],Iterable)#list是否可以迭代 ，是
isinstance(123,Iterable)#整数是否可以迭代 ，否

for i,value in enumerate(d):#enumerate 实现将list变成索引-元素对。
    print(i,value)


a = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
b = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
#方法1 通过外部列表迭代，以及余数来进行表达。
# for i in list(range(0,60)):
#     print(a[i%10]+b[i%12])
#方法2 通过enumerate内部函数将list变成索引-元素的方式来进行列表生成器的判断表达。
c=[m+n for x,m in enumerate(a) for y,n in enumerate(b) if (x% 2 == 0 and y% 2 == 0) or (x% 2 != 0 and y% 2 != 0) ]
print(c)
# for s in c:
#     print(s)


L=[]
for x in range(1,11):
    L.append(x*x)
print(L)

print([x*x for x in range(1,11)])

#方法1 通过外部函数来筛选出str元素
L1 = ['Hello', 'World', 18, 'Apple', None]
l=[]
for x in L1:
    if isinstance(x,str):
        l.append(x)
    else:
        pass
L2=[s.lower() for s in l]
print(L2)
#方法2 通过列表表达式条件判断筛选出str元素
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

L=(x*x for x in range(1,11))
print(L)
for l in L:
    print(l)