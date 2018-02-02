'''
多进程
要让py程序事先多进程，要先了解操作系统的相关知识
linux提供了一个fork()系统调用，
普通函数调用一次返回一次
fork调用一次返回两次
因为操作系统把当前进程（父进程）复制了一份（子进程）
然后在父进程和子进程内返回

子进程永远返回0，而父进程返回子进程的id，
一个父进程可以fork出很多歌子进程，
父进程要记下每个子进程的id,而子进程只需要调用getpid就可以拿到父进程的id

'''
#py的os模块封装了常见的系统调用，其中包括fork，可以在py中轻松创建子进程
#import os
#print('process(%s) start ...'% os.getpgid())
#win系统没有fork

#py提供muliprocessing模块提供了一个process来代表一个进程对象
#下面例子演示了启动一个子进程并等待其结束

from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print('run child %s (%s)' % (name,os.getpid()))
if __name__=='__main__':
    print('parent process %s' % os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child end')
#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个process实例
#用start方法启动，这样创建进程比fork还简单
#join可以等待子进程结束后再继续往下运行，通常用于进程间的同步

#Pool
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程

