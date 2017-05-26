#!/usr/bin/python
# -*- coding=utf-8 -*-
#切片

r=list(range(0,10))
print(r)

r=[]
n=10
for i in range(n):
    r.append(i)
print(r)

print(r[:])
print(r[0:6:2])#从第一个数开始，到第六个数，步长为2
