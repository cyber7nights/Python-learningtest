# -*- coding=utf-8 -*-

def my_abs(x):
    if not isinstance(x,(int,float)):
        return 'TypeErro:out of given'
    if x>=0:
        return x
    else:
        return -x

def enroll(name,age,gender,city='beijing'):#城市默认值为北京
    print('name:',name)