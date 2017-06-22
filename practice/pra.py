# -*- coding=utf-8 -*-
#089这三个数，组成的四个数的组合有哪些。
num=[0,8,9]
z=[]
for i in num:
    for j in num:
        for k in num:
            for l in num:
                if i!= 0:
                    x=str(i)+str(j)+str(k)+str(l)
                    z.append(x)

print (z)
print('数量：',len(z))

#0789四个数，组成的四位数组合且有两个数可以重复的有哪些。
num=['0','7','8','9']
y=[]
for i in num:
    for j in num:
        for k in num:
            for l in num:
                if i!= '0' and i!=j!=k!=l and ((i!=j!=k)or(j!=k!=l)or(k!=l!=i)or(l!=i!=j)):
                    x=i+j+k+l

                    y.append(x)
print (y)
print('数量：',len(y))