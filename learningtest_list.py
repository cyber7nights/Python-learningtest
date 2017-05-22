# -*- coding=utf-8 -*-
workmates=['xiong','yang','zhang','xue']
workmates_managers=['wu','sun','chen','yu']
workmates.append(workmates_managers) #添加元素
print(len(workmates))  #结果为5
print(workmates) #结果为['xiong','yang','zhang','xu'，['wu','sun','chen','yu']]
workmates.pop()#删除list末尾的元素
workmates.insert(3,workmates_managers)#指定位置插入
print(workmates)#显示结果['xiong', 'yang', 'zhang', ['wu', 'sun', 'chen', 'yu'], 'xu']
workmates[4]='xu'#替换指定位置元素
print(workmates)
#要拿到workmates_managers中的‘yu’
#方法一
print(workmates_managers[3])
#方法二
print(workmates[3][3])
#获取第一个和最后一个元素
print(workmates[0],workmates[-1])

other_co=['ZJN','XKY']
co=('PZ','XY','ST',other_co)#tuple有序集合(元组)。
print(co)
other_co.insert(1,'TX')
print(co)
other_co[1]='BD'
print(co)
#元组内的列表元素，可以被替换。
#小结

#list和tuple是Python内置的有序集合，一个可变(列表)，一个不可变（元组）。根据需要来选择使用它们。

