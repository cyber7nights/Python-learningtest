# -*- coding=utf-8 -*-
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

Point=namedtuple('point',['x','y'])#namedtuple函数定义一个含有（'名称'，['属性']）的类。Point是一个tuple的子类，point是这个子类的名称。
p=Point(1,2)#p是Point类的实例
print(p.x)
print(dir(p))

q=deque(['x','y','z'])#deque创建一个list队列。
q.append('a')
q.appendleft('b')#deque支持appendleft和popleft
print(q)

dd=defaultdict(lambda : 'N/A')#defaultdict 是在dict中存放一个函数，当不存在key时返回某一特定值。
print(type(dd))
dd['key1']='ok'
print(type(dd))
print(dd['key1'])
print(dd['key2'])

d={'a':1,'b':2,'c':3}
d=OrderedDict(d)
di=([1,'a'],[2,'b'],[3,'c'])
di=dict(di)
print(di)
di=OrderedDict(di)
print(di)
print(d)

#计数
#方法1
s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()
c=Counter(s)
te='高端会疯掉发呆东方花地哦啊发我更方便vzjcviuehfdahs掉哈啊'
t=Counter(te)
print(c)
print(t)
#方法2
c=Counter()
for ch in s:
    c[ch]=c[ch]+1
print(c)