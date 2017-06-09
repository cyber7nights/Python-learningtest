from datetime import datetime,timedelta,timezone
now = datetime.now()
print(now)
print(type(now))

dt=datetime(2017,6,9,11,25)
print(dt)

dt=dt.timestamp()  #epoch time是指1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
print(dt)

#timestamp 转换为datetime
t=1496978700.0
epoch=datetime.fromtimestamp(t)
print(epoch)
epoch=datetime.utcfromtimestamp(t)
print(epoch)

#str 转换为datetime
today=datetime.strptime("2017-6-9 14:12","%Y-%m-%d %H:%M")
print(today)
print(type(today))

#datetime转换为str
now=datetime.now()
now=now.strftime('%a,%m-%d-%Y %H:%M:%S')
print(now,type(now))

#datetime 加减
now=datetime.now()
print(now)
now=now+timedelta(hours=10)
print(now)

