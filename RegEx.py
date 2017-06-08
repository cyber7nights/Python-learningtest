# -*- coding=utf-8 -*-
import re
# test=input('please enter your home telephone number')
# if re.match(r'^\d{3,4}\-\d{3,8}$',test):
#     print('OK')
# else:
#     print('wrong')

#切分字符串(d   sa  ,,ad  a,d, ea, ,,a,ad, ,a,d ,f, ,a,d)
# a=input('please enter some words with \',\',\' \'.')
# b=re.split(r'[\s\,]+',a)#注意‘+’
# print(a)
# print(b)

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

a= re.match(r'^(\d+)(0*)$', '102300').groups()#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
b=re.match(r'^(\d+?)(0*)$', '102300').groups()#\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
print(a,b)
#编译
re_telephone=re.compile(r'^(\d{3,4})\-(\d{3,9})$')
print(re_telephone.match('010-237281').groups())

#作业
re_email=re.compile(r'([a-zA-Z0-9][a-zA-Z0-9\_]*)\@([A-Za-z0-9]*\.[a-z]*)')
name=re_email.match('tom@voyager.org').groups()
print(name[0])