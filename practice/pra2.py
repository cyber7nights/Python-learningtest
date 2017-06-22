# -*- coding=utf-8 -*-
import os
#0-9,六位数密码
num=list(range(10))
z=[]
try:
    os.remove('result2.txt')
except:
    pass
finally:
    for a in num:
        for b in num:
            for c in num:
                for d in num:
                    for e in num:
                        for f in num:
                            x=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                            z.append(x)
    with open ('result2.txt','w') as q:
        for i in z:
            q.write(i+'\n')