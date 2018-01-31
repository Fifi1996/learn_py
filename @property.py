'''
使用@property
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单
但是没办法检查参数，导致可以把成绩随便改

'''
#s=Student()
#s.score=9999
#显然不合逻辑，为了限制score的范围，可以通过一个set_score方法来设置成绩
#通过get_score方法来获取成绩，这样在方法中可以检查参数
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be int!')
        if value <0 or value >100:
            raise ValueError('score must be 0-100')
        self._score=value

#现在对任意实例进行操作，就不能随便设置score了
s=Student()
s.set_score(69)
print(s.get_score())

#s.set_score(999)  超过100报错

'''
但是上面调用方法又略复杂，没有直接调用属性这么简单
装饰器（decorator）可以给函数动态加上功能，对于类的方法
装饰器一样起作用，内置的@peoperty就是负责把一个方法变成属性调用的
'''
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be int!')
        if value <0 or value >100:
            raise ValueError('score must be 0-100')
        self._score=value
#@property实现比较复杂，先考虑如何使用
#把一个getter方法变成属性，只需要加上@property
#此时@property本身又创建了另一个装饰器@score.setter
#负责把一个setter方法变成属性赋值
#于是就有了一个可控的属性操作
s=Student()
s.score=60 #实际转换为s.set_score(69)
print(s.score)

#注意到这个神奇的@property，我们在对实例属性操作时
#就知道该属性很可能不是直接暴露的，而是通过getter和setter实现

#还可以定义只读属性，只定义getter方法，不定义setter方法就是只读属性
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value
    @property
    def age(self):
        return 2018-self._birth
#上面的birth就是可读写属性，而age就是只读属性

#小结
#@property广泛应用在类的定义中，可让调用者写出简短的代码
#同时保证对参数进行必要的检查

'''
练习
请利用@property给一个Screen对象加上width和height属性，
以及一个只读属性resolution：
'''
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,wide):
            self._width=wide
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, high):
        self._height = high
    @property
    def resolution(self):
        return self._width*self._height
x=Screen()
x.width=100
x.height=100
print(x.resolution)