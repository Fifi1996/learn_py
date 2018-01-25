'''
装饰器
'''
#由于函数也是一个对象，而且函数对象可以赋值给变量，
#所以通过变量也能调用该函数
def now():
    print('2018-1-25')
f=now
print(f())
#函数对象有一个_name_属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)
'''
假设我们要增强now函数的功能，比如再函数调用前后自动打印日志
但又不希望修改函数定义，这种代码运行期间动态增加功能的方式称之为
装饰器 decorator
'''
#本质上，装饰器就是一个返回函数的高阶函数，
#所以我们要定义一个能打印日志的装饰器：
def log(func):
    def wrapper(*args,**kw):
        print('call %s()'% func.__name__)
        return func(*args,**kw)
    return wrapper
#观察上面的log，因为她是一个decorator，所以接受一个函数作为参数
#并返回一个函数，我们要借助@语法，把decorator置于函数的定义处：
@log
def now():
    print('2018-1-25')
#调用now函数，不仅会运行now函数本身，还会运行函数前打印一行日志
print(now())

#把@log放到now()函数的定义处，相当于执行了：
now=log(now)
'''
由于log是一个装饰器，返回一个函数，所以原来的now函数仍然存在，
只是现在同名的now变量指向了新的函数，于是调用now执行新函数
即在log函数中返回wrapper
wrapper函数的参数定义是(*args,**kw)
因此wrapper函数可以接受任意参数的调用
在wrapper函数内，首先打印日志，紧接着调用原始函数
'''
#如果decorator本身需要传入参数，那就要编写一个返回decorator的
#高阶函数，写出来会更复杂
#比如要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
#这个三层嵌套的decorator用法如下：
@log('execute')
def now():
    print('2018-1-25')
print(now())
#和两层嵌套的decorator相比，三层的效果：
now=log('execute')(now)
'''
我们来剖析上面的语句，首先执行log('execute'),返回的是装饰器函数
在调用返回的函数，参数是now函数，返回值最终是wrapper函数
以上两种decorator的定义都没有问题。但是还差最后一步，
因为我们讲了函数也是对象，他有_name_等属性，但你去看经过装饰器装饰过的函数
他们的_name_已经从原来的'now'变成了'wrapper'
'''
print(now.__name__)
'''
因为返回的那个wrapper函数名就是'wrapper',
所以西药把原始函数的_name_等属性复制到wrapper函数中，
否则有些依赖函数签名的代码执行就会出错
'''
#不需要编写wrapper._name_=func._name_这样的代码
#内置的funtools.wrapper就是干这个的，一个完整的decorator写法如下：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args，**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
#或者针对带参数的decorator：
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
#inmprt functools是导入functools模块，
'''
练习
请设计一个decorator，他可以作用在任何函数上，并打印该函数的执行时间

'''
import time,functools
def metric(fn):
    print('%s executed in %s ms' % fn.__name__,10.24))



