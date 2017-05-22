dict={'xiong':10,'zhang':0,"yang":-10}
print(dict['xiong'])

d={10:"xiong",0:'yang',3:'zhang'}
print(d[10])
dict['yang']=0
dict['zhang']=3
print(dict)

print('yu' in dict) #通过in判断key在不在dict里面
print(dict.get('yu'))#通过dict.get判断key在不在dict里面
print(dict.get('yu','no'))#通过dict.get判断key在不在dict里面,并返回指定值

#dict.pop('zhang')
#print(dict)#通过dict.pop删除dict中的key。


for key in dict:
    print(key,":",dict[key])

