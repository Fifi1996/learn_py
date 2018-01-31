'''
使用枚举类
当我们需要定义常量时，一个办法使用大写变量通过整数来定义。例如月份
JAN=1
FEB=2
好处就是简单，缺点是类型是int，并且仍然是变量
更好的方法是为这样的枚举类型定义一个class类型
每个常量都是class的唯一实例
内置的enum类来实现这个功能
'''
from enum import Enum
Month=Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#这样就获得了Month类型的枚举类，可以直接使用Month.Jan来引用常量
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
#value属性则是自动赋给成员的int常量，默认从1开始计数

#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
from enum import Enum,unique
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
#@unique装饰器可以帮我们检查保证没有重复值

#访问这些枚举类型可以有若干种方法
day1=Weekday.Mon
print(day1)

'''
练习
把student的gender改造为枚举类型，可以避免使用字符串

'''
from enum import Enum,unique
@unique
class Gender(Enum):
    Male=0
    Female=1
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
#小结
#Enum可以把一组相关常量定义在一个class中，且class不变
#成员可以直接比较

