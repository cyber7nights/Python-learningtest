# -*- coding=utf-8 -*-
from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('start %s %s'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('spend %s %s'%(name,end-start))
if __name__=='__main__':
    print('parent process %s'%os.getpid())
    p=Pool(4)
    # 方法一：
    # for i in range(5):
    #     # p.apply_async(long_time_task,args=(i,))

    # 方法二：
    i=list(range(5))
    p.map(long_time_task,i)

    print('Waiting for all subprocesses done...')
    p.close()#关闭进池，无法继续添加新的进程
    p.join()#阻塞主进程，避免子进程还没结束就结束。
    print('All subprocesses done.')