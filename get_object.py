'''
获取对象信息
当我们拿到一个对象的引用时，如何知道这个对象是什么类型

'''
#使用type()
#我们来判断对象类型，使用type()函数
#基本类型都可以用type判断
print(type(123))
print(type('str'))
print(type(None))
#如果一个变量指向函数或类也可以
print(type(abs))

#type()函数返回的是什么类型，返回的是class类型
#如果要在if语句中判断，就需要比较两个变量的type类型是否相同
print(type(123)==type(456))

#判断基本类型可以直接写int,str等，但如果要判断一个对象是否时函数怎么办？
#可以使用types模块中定义的常量
import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(lambda x:x)==types.LambdaType)

#使用isinstance

#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数
#它返回一个包含字符串的list
print(dir('ABC'))
#打印： ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']

#类似__xxx__的属性和方法在py中都是有特殊用途的，比如__len__返回长度
#如果你调用len()函数去获取一个对象的长度，实际上在内部自动去调用该对象__len__()方法
#下面代码是等价的
print(len('ABC'))
print('ABC'.__len__())

#我们自己写的类，如果也想用len(MyObj)的话，就自己写一个__len__方法
class MyDog(object):
    def __len__(self):
        return 100
dog=MyDog()
print(len(dog))

#剩下的都是普通属性或方法，比如lower（）返回小写的字符串
print('ABC'.lower())


#仅仅把属性和方法列出来是不够的，配合getatttr（），setatttr（）
#以及hasattr，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x=0
    def power(self):
        return self.x*self.x
obj=MyObject()
print(hasattr(obj,'x')) #有属性x吗
print(obj.x)

'''
小结
通过内置的一系列函数，我们可以对任意一个对象进行剖析
拿到其内部数据，注意：只有在不知道对象信息的时候，我们才会去获取对象的信息
'''
#如果可以直接写：
sum=obj.x+obj.y
#就不要写
sum=getattr(obj.'x')+getattr(obj.'y')

#一个正确的用法的例子
def readImage(fp):
    if hasattr(fp,'read'):
        return readData(fp)
    return None
#我们希望从文件流fp中读取图像，首先要判断该fp对象是否存在read方法
#如果存在，则该对象是一个流，如果不存在，则无法读取,hasattr（）就爬上用场了
