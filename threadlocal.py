'''
ThreadLocal
在多线程环境下，每个线程都有自己的数据，
一个线程使用自己的局部变量比使用全局变量好
因为局部变量不会影响其他线程
而全局变量修改必须加锁
但是局部变量在函数调用时传递起来很麻烦

'''
def process_student(name):
    std=Student(name)
    #std是局部变量，但是每个函数都要用它，必须传递
    do_task1(std)
    do_task2(std)
def do_task1(std):
    do_subtask1(std)
    do_subtask2(std)
def do_task2(std):
    do_subtask2(std)
    do_subtask2(std)
#如果函数每层都要传很复杂

#ThreadLocal不用查找dict
import threading
#创建全局的threadlocal对象
local_school=threading.local()

def process_student():
    #获取当前线程关联的studnet
    std=local_school.student
    print('hello%s(in %s)'% (std,threading.current_thread().name))
def process_thread(name):
    #绑定threadlocal的student
    local_school.student=name
    process_student()
t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
#全局变量local_school就是一个threadlocal对象，每个thread对它都可以读写student属性
#但互不影响，可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量
#可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量

#最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，
#这样一个线程所有调用到的处理函数都可以方便的访问这些资源

#小结
#一个threadlocal变量虽然是全局变量，但每个线程都只能读写自己的线程的独立副本
#解决了参数在一个线程中各个函数之间互相传递的问题