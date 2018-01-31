'''
定制类
看到类似__slots__这种形如__xx__的变量或者函数名要注意
是有特殊用途的，帮助我们定制类

'''
#__str__
#先定义一个类，打印一个实例
class Student(object):
    def __init__(self,name):
        self.name=name
print(Student('Michael'))
#打印出一堆 <__main__.Student object at 0x109afb190>，不好看。

#要打印好看，定义好__str__方法，返回一个好看的字符串
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student('Michael'))

#直接敲变量不用print打印出来还是不好看
s=Student('skhgj')
print(s)
#__str__返回用户看到的的字符串


#__iter__
#如果一个类想被用于for,,in循环，类似list
#必须实现一个__iter__方法，返回一个迭代对象
#for循环会调用迭代对象的next（）拿到循环的下一个值
#直到遇到StopIteration错误时退出循环

#以斐波那契数列为例，写一个Fib类，作用于for循环
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 #初始化两个计数器a,b
    def __iter__(self):
        return self #实例本身就是迭代对象，返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b #计算下一个值
        if self.a>100000:
            raise StopIteration
        return self.a #返回下一个值
    #把Fib实例作用于for循环
for n in Fib():
    print(n)


#__getitem__
#Fib实例虽然能做用于for循环，看起来和list有点像，但是当成list使用不行
#比如取第5个元素
#Fib()[5]

#TypeError: 'Fib' object does not support indexing

#要像list那样按照下标取出元素，要实现__getitem__方法
class Fib(object):
    def __getitem__(self, n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
#现在可以按照下标访问数列的任意一项了
f=Fib()
print(f[0])

#但是list有个神奇的切片方法
print(list(range(100)[5:10]))

#对于Fib却报错。原因是__getitem__传入的参数可能是一个int
#也可能是一个切片对象slice。所以要判断
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int): #n是索引
            a,b,=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice): #n是切片
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >=start:
                    L.append(a)
                a,b=b,a+b
            return L
#现在试试对Fib切片
f=Fib()
print(f[0:5])

#但是没有对step参数做处理,也没有对负数做处理，还有很多工作要做
#如果把对象看作dict,__getitem__的参数也可能是一个可以做key的object，例如str

#对应的是__setitem__，吧对象作为list/dict来对集合赋值
#__delitem__用于删除某个元素

#通过上面的方法，自己定义的类表现的和list tuple dict没什么区别
#归功于动态语言的‘鸭子类型’不需要强制继承某个接口


#__getattr__
#正常情况下，调用类的方法或者属性时，如果不存在就会报错
class Student(object):
    def __init__(self):
        self.name='Michael'
#调用name属性，没问题，但是不逊在的score就报错

#要避免这个错误，除了可以加上一个score属性外，还可以写一个__getattr__方法
#动态返回一个属性，修改：
class Student(object):
    def __init__(self):
        self.name='Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
#只有在没有找到属性的情况下，才调用__getattr__已有的属性
#比如name不会在__getattr__中查找

'''
举例
现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

http://api.server/user/friends
http://api.server/user/timeline/list
如果要写SDK，给每个URL对应的API都写一个方法，那得累死，
而且，API一旦改动，SDK也要改。
'''
#利用完全动态的__getattr__可以写出一个链式调用
class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__=__str__
print(Chain().status.user.timeline.list)

#__call__
#一个对象实例可以有自己的属性和方法，调用实例方法时
#用instance.method来调用、
#任何类只需要定义一个__call__方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s.' %self.name)
#调用方式
s=Student('SH')
print(s())
#__call__还可以定义参数
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象