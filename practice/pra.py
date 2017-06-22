# -*- coding=utf-8 -*-
import os
#089这三个数，组成的四个数的组合有哪些。
num=[0,8,9]
z=[]
try:
    os.remove('resu.txt')
except:
    pass
finally:
    for i in num:
        for j in num:
            for k in num:
                for l in num:

                    x=str(i)+str(j)+str(k)+str(l)
                    z.append(x)

    print (z)
    print('数量：',len(z))
    with open('resu.txt','a') as q:
        q.write('数量：'+str(len(z))+'\n')
        for i in z:
            q.write(i+'    ')
            q.write('\n')

    #0789四个数，组成的四位数组合且有两个数可以重复的有哪些。
    num=['0','7','8','9']
    y=[]
    for i in num:
        for j in num:
            for k in num:
                for l in num:
                    # if i!=j!=k!=l and ((i!=j!=k)or(j!=k!=l)or(k!=l!=i)or(l!=i!=j)):
                    if i!=j!=k!=l:
                        x=i+j+k+l
                        for n in range(len(x)):
                            if x[n-4]!=x[n-3]!=x[n-2]:
                                m=x  #如果直接用append 会导致同一个数字被写入4次
                        y.append(m)
    print (y)
    print('数量：',len(y))
    with open ('resu.txt','a') as q:
        q.write('\nQ2:\n'+'数量：'+str(len(y))+'\n')
        for i in y:
            q.write(i+'\n')
