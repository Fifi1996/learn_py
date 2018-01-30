'''
面向对象高级编程
使用_slots——
正常情况下，当我们定义一个class，创建了class实例后
可以给实例绑定任何属性和方法，这就是动态语言的灵活性
'''
class Student(object):
    pass
#给实例绑定一个属性
s=Student()
s.name='Michael'#动态给实例绑定一个属性
print(s.name)
#还可以给实例绑定一个方法
def set_age(self,age):
    self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s) #给实例绑定一个方法
s.set_age(25)   #调用实例方法
print(s.age)

#但是给一个实例绑定方法，对另一个实例是不起作用的
s2=Student() #创建新的实例
#print(s2.set_age(25))#尝试调用方法

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score=score
Student.set_score=set_score
#给class绑定方法后，所有实例均可调用
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)
#通常情况下，上面的set_score方法是直接定义在class中
#但动态绑定允许程序运行时给类加功能

'''
使用_slots_
如果我们想要心智实例的属性怎么办
只允许对Student实例添加name和age属性
为了达到限制的目的，定义一个特殊的slots变量
'''
class Student(object):
    __slots__ = ('name','age')
s=Student()#创建新的实例
s.name='Michael'#绑定属性name
s.age=25 #绑定属性age
#s.score=99 #绑定属性score
#由于score没有放到__slots中，所以不能绑定score属性

#使用slots要注意，定义的属性仅对当前类实例起作用，继承的子类时不起作用的

