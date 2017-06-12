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

#作业
# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    #dt=re.match(r'^(1[0-9]{3}|200[0-9]|[201[0-7]|[0-9]{1,4})[: -\/_](0[1-9]|1[0-2]|[1-9])[:-\_](0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])[\:-|\s](0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])',dt_str)
    tz_utc_5=timezone(timedelta(hours=5))
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    dt=dt.replace(tzinfo=tz_utc_5)
    tz=re.match(r'(UTC)([+|-]0[0-9]|[+|-]1[0-9]|[+|-]2[0-3]|[+|-][0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])',tz_str).groups()
    tz=int(tz[1])
    print(tz)
    print( dt.astimezone(timezone(timedelta(hours=tz))).timestamp())
    return dt.astimezone(timezone(timedelta(hours=tz))).timestamp()

# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
# assert t1 == 1433121030.0, t1
#
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t2)
# assert t2 == 1433121030.0, t2
#
# print('Pass')