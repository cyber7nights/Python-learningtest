# -*- coding=utf-8 -*-
import hashlib
class User(object):
    def __init__(self,names,passwords):
        self.name=lambda names :hashlib.md5(names)
        self.password=lambda passwords :hashlib.md5(passwords)
# name=input("enter name")
# password=input('enter password')
name='dafadf'
password="fjdiaofh"
me=User(name,password)
na=hashlib.md5()
pw=hashlib.md5()
na.update(name.encode('utf-8'))#TypeError: object() takes no parameters 所以要加encode

pw.update(password.encode('utf-8'))#TypeError: object() takes no parameters所以要加encode


print(me.name,me.password)  #存在内存里
print(na.hexdigest(),pw.hexdigest())#取出md5

#练习 验证用户md5密码
# def calc_md5(password):
#     password_md5=hashlib.md5()
#     return password_md5.update(password,'utf-8')
#  db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
#注册
db={}
def register(user_name,password):
    get_md5=hashlib.md5()
    get_md5.update(password.encode('utf-8'))
    db[user_name]=get_md5

#登陆验证
def login (user_name,password):
    if db[user_name] == password:
        print('True')
    else:
        print('False')
# user='michael'
# password='fdjaiogh'
register('michael','fhdioahf')
register('Bob','fhdhf')
login('michael','fdjaiogh')
print(db)

