# -*- coding= utf-8 -*-
import os,struct
from datetime import datetime

listdir=[x for x in os.listdir('.') if os.path.isfile(x) and (os.path.splitext(x)[1]=='.BMP' or os.path.splitext(x)[1]=='.bmp')]#目录下后缀为‘.BMP’和‘.bmp’的文件列表
# print(listdir)
os.remove('bmpinfo.txt')#因为open(file,'a')是在文末追加写，所以为避免每次运行重复写入，先删除之前的版本。
if len(listdir)>0:
    for image in listdir:
        with open(image,'rb') as f:
            s=f.read(30)
            info=struct.unpack('<ccIIIIIIHH',s)
        if info[0]+info[1]==b'BM':
            size=str(info[-3])+'*'+str(info[-4])
            color=info[-1]
            print(image+'-info')
            print('高宽分辨率：',size)
            print('颜色数：',color)
            with open('bmpinfo.txt','a') as t:#open()，'a'----连续追加写，'w'----覆盖写。
                t.write(datetime.now().strftime('%a,%m-%d-%Y %H:%M:%S'))
                t.write('\ninfo:'+image)
                t.write('\n高宽分辨率：'+size)
                t.write('\n颜色数：'+str(color))

        else:
            print(image,'is not BM')
else:
    print('Not find BMP')