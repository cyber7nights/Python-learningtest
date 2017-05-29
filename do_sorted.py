# -*- coding=utf-8 -*-
#假设我们用一组tuple表示学生名字和成绩：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 请用sorted()对上述列表分别按名字排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
#     return t[0]
# L2 = sorted(L, key=by_name)
# ↑方法一，方法二↓
L2=sorted(L,key=lambda x:x[0])
print(L2)

# 再按成绩从高到低排序：
# def by_score(t):
#     return t[1]
# L2 = sorted(L,key=by_score,reverse=True)
# ↑方法一，方法二↓
L2 = sorted(L,key=lambda x:x[1],reverse=True)
print(L2)

#总结，sorted高级函数，是对列表元素进行了一次映射从而通过映射来排序。