'''
继承和多态
在oop程序中，当我们定义了一个class时，可以从某个现有的class继承
新的class称为子类(subclass)，而被继承的类称为基类，父类或超类
base class/super class
'''
#比如我们呢已经编写了一个名为animal的class，有一个run()方法可以直接打印
class Animal(object):
    def run(self):
        print('Animal is run..')
#当我们需要编写Dog和Cat类时，就可以直接从Animal类中继承：
class Dog(Animal):
    pass
#对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类

#继承有什么好处？
#子类获得父类的全部功能
dog=Dog()
print(dog.run())
#子类中可以增加方法
class Dog(Animal):
    def run(self):
        print('Animal is run..')
    def eat(self):
        print('eat...')
#当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()
#在代码运行时总会调用子类的run(),这样我们就获得了集成的另一个好处，多态

'''
要理解什么时多态，首先要对数据类型做说明，
当我们定义一个class时，实际上就定义了一种数据类型，
判断一个变量是否是某个类型可以用isinstance判断
'''
a=list()
b=Animal()
c=Dog()
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
#尝试一下
print(isinstance(c,Animal))
#看来c不仅是Dog,还是Animal

#因为Dog是从Animal继承下来的，当我们创建了一个Dog实例c时
#发现c类型是Dog,但是同时Dog本来就是Animal的一种
#所以在继承关系中，如果一个实例的数据类型时某个子类，那他的数据类型也可以被看做是父类
#反之不行
print(isinstance(b,Dog))

#要理解多态的好处，还需要编写一个函数，这个函数接受一个Animal类型的变量
def run_twice(animal):
    animal.run()
    animal.run()
#当我们传入Animal的实例时，
print(run_twice(Animal()))
# 打印出 Animal is running...
#       Animal is running...
#但我们传入Dog实例时，run_twice
print(run_twice(Dog()))
#打印出 Dog is running...
#      Dog is running...

#如果在定义一个Tortoise类型，也从Animal派生
class TorToise(Animal):
    def run(self):
        print('Tortoise is run..')
#当我们调用run_teice时，传入Tortoise的实例
print(run_twice(TorToise()))
#打印出 Tortoise is running
#      Tortoise is running

#发现新增一个Animal的子类，不必对run_teice()做任何修改，

'''
多态的好处就是，我们需要传入Dog,Tortoise时，只需要接收Animal类型就可以了
然后按照Animal类型进行操作即可，
由于Animal类型会有run方法，因此传入的任意类型只要是Animal类或者子类
就会自动调用实际类型run方法，这就是多态的意思

'''
#对于一个变量，只需要知道它是Animal类型，无需确切知道它的子类型，
#可以放心调用RUN方法
#而具体调用的run方法是作用在Animal,Dog对象上，
#由运行时该对象的确切类型决定，这就是多态真正的威力
#调用方只管调用，不管细节，而我们新增一种Animal子类时，只要确保run方法编写正确
#这就是著名的开闭原则

#对扩展开放：允许新增Animal子类
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数

#继承还可以一级级继承下来，最终都可以追溯到根类object

'''
静态语言VS动态语言
对于静态语言例如Java来说，如果要传入Animal类型
则传入的对象必须是Animal类型或者它子类，否则无法调用run()方法

对于python这种动态语言来说，则不一定传入Animal类型
只需要传入的对象有一个run()方法就可以了

'''
class Timer(object):
    def run(self):
        print('sgagag')
#这就是动态语言的‘鸭子’类型，不要求严格的继承体系，
#一个对象只要看起来像鸭子，走路像鸭子，那就可以看作鸭子

#python的'file-like-object'就是一种鸭子类型，对真正的文件对象
#他有一种read方法，返回其内容，但是很多对象只要有read方法，都被视为file-like-object

#小结
#继承可以把父类的所有功能都直接拿过来，这样不必从零做起
#子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写

#动态语言的鸭子类型决定了继承不像静态语言那样是必须的