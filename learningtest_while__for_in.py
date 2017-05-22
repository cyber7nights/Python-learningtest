# -*- coding=utf-8 -*-
workmates=['xiong','yang','zhang','xue']
for workmate in workmates:
    print(workmate)
    #for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


#list(range(101))
#print(range(101))
#print(list(range(10,80)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
#练习

#请利用循环依次对list中的每个名字打印出Hello, xxx!
# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(x)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

#要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

#有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。

#作业练习：请试写一个死循环程序。
#n=1
#while n>0:
#    n=n+1
#    print(n)