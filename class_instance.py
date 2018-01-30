'''
面向对象最重要的概念就是类和实例
必须牢记类是抽象的模板，比如student类
而实例是根据类创建出来的一个个具体的对象
每个对象有相同的方法，但各自的数据不同
'''
#以student为例，定义类是通过class关键字
class Student(object):
    pass
#class后面紧接着是类名，即student，类名通常是大写开头的单词
#接着是object，表示该类是从哪个类继承下来的
#如果没有合适的类就是用object类，这是所以类最终都会继承的类

#定义好了student类，就可以根据student类创建出student的实例，
#创建实例是通过类名+（）实现的：
bart=Student()
print(bart)
print(Student)
#可以看到变量bart指向的就是一个Student的实例，后面的数字是内存地址
#每个object的地址都不一样，而student本身则是一个类
#可以自由地给一个实例变量绑定属性，比如给实例bart绑定一个name属性
bart.name='ksjgk'
print(bart.name)

#类可以起到模板的作用，因此可以在创建实例的时候，把一些我们认为必须要绑定的属性强制编写进去
#通过定义一个特殊的__init__方法，在创建实例的时候，就把name,score等属性等绑定上去
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
#注意到__init__方法的第一个参数永远是self。表示创建的实力本身
#因此在__init__方法那日不，就可以把各种属性绑定到self，因为self指向创建的实例本身

#有了__init__方法，在创建实例的时候，就不能传入空的参数了
#必须传入与方法匹配的参数，但self不需要传，解释器会把变量传进去
bart=Student('sjgh',99)
print(bart.name)
print(bart.score)
print(bart)
#和普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
#并且在调用时不用传递该参数


'''
数据封装
面向对象编程有一个重要特点就是数据封装
在上面的student中。每个实例就拥有各自的name和score这些数据
我们通过函数来访问这些数据
比如打印一个学生的成绩
'''
#def print_score(std):
 #   print('%s: %s'% (std.name,std.score))
#print(print_score(bart))
#既然student实例本身就拥有这些数据，要访问这些数据
#没必要从外面的函数去访问，可以直接在student类的内部定义访问数据的函数
#这样就把数据给封装起来了，这些封装数据的函数是和student类本身是关联起来的，我们称为类的方法
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
#要定义一个方法，除了第一个参数外，其他和普通函数一样，
#要调用译者方法。只需要在实例变量上直接调用，除self不用传递，其他参数正常传入

#这样一来，我们从外部看student类，就只需要知道，创建实例需要给出namehescore
#而如何打印都是在student内部定义的，这些数据和逻辑被封装起来了，调用很容易，不用知道内部实现细节

#封装的里一个好处是可以给student类增加新的方法，比如get_grade：
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'
lisa=Student('lisa',99)
print(lisa.name,lisa.get_grade())

'''
小结
类是创建实例的模板，而实例则是一个个具体的对象，各个实例拥有的数据相互独立
方法就是实例与绑定的函数和普通函数不同，方法可以直接访问实例的数据
通过在实例上调用方法，我们就直接操作了对象内部的数据
但不需要知道方法内部的实现细节
和静态语言不同，py允许实例变量绑定任何数据
也就是说对于两个实例变量，虽然他们都是同一个类的不同实例
但拥有的变量名称可能不同
'''
bart=Student('Bart',99)
lisa=Student('Lisa',92)
bart.age=8
print(bart.age)
