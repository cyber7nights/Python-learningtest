# -*- coding=utf-8 -*-

# 用filter求素数
def odd_iter():
    n=1
    while True:
        n=n+2
        yield n #创造一个奇数生成器
def _not_divisible(n):
    return lambda x:x % n > 0  #创造一个筛选函数，其中的n来自于iter中元素。
def func():
    yield 2
    it=odd_iter()
    while True:  #
        n=next(it)  #
        yield n  #
        it=filter(_not_divisible(n),it)

for n in func():
    if n<100:
        print(n)
    else:
        break
print(list(range(2)))

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
def is_palindrome(n):
    if n>=9:
        n=str(n)
        for i in range(len(n)):
            return int(n[i])!=int(n[len(n)-1-i])
    else :
        return True

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))