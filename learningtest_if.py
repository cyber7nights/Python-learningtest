# -*- coding=utf-8 -*-
age=input('please write your age')
if int(age) >= 18:
    print('your age is',age,":"'adult')
elif int(age) >= 6:
    print('your age is',age,":"'teenager')
else:
    print('your age is',age,":"'kid')

#作业：小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
height = float(input('请输入您的身高（cm）：'))
weight = float(input('请输入您的体重（kg）：'))
bmi = (weight/height)**2
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')