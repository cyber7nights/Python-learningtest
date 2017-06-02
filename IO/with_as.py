# -*- coding=utf-8 -*-

from datetime import datetime

with open("test.txt",'w') as file:
    file.write('hello world!')
with open ('test.txt','r') as file:
    s=file.read()
    print (s)
    print(file)
with open('test.txt','w') as file:
    file.write(datetime.now().strftime('%Y.%m.%d.'))
with open('test.txt','r') as file:
    s=file.read()
    print('今天是：')
    print(s)