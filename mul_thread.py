'''
多线程
多任务可以由多进程完成，也可以由一个进程内的多线程完成
标准库提供了两个模块
_thread低级模块
threading，高级模块
'''
#启动一个线程就是把一个函数传入并创建thread实例，然后调用start开始执行
import time,threading
#新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s end' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
#由于任何进程默认就会启动一个线程，把该线程称为主线程
#主线程又可以启动新线程

#Lock
#多进程和多线程最大的不同在于，多进程中同一个变量，各自由一份拷贝在于每个进程中互不影响
#多线程中所有变量都由所有线程共享
#所以任何一个变量都可以被任何一个线程修改，危险在于共享数据之间容易把内容改乱了

