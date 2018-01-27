'''
面向对象编程-obiect oriented programming
oop把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数

面向过程的程序设计把计算机程序视为一系列的命令集合，
即一组函数的顺序执行，为了简化程序设计，面向过程把函数继续切分为子函数
即把大块函数通过切割成小块函数来降低系统的复杂度

面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象可以饥饿收其他对象发来的信息
并处理这些信息，计算机程序的执行就是一系列消息在各个对象之间传递

在py中，所有数据类型都可以视为对象，当然可以自定义对象
自定义对象数据类型就是面向对象中的类（class）的概念
'''
#以一个例子来说明面向过程和面向对象在程序流程的不同之处
#假如我们要处理学生成绩表。为了表示一个学生的成绩，面向过程程序用一个dict表示
std1={'name':'Michael','score':98}
std2={'name':'Bob','score':90}
#而处理学生成绩可以通过函数实现，比如打印学生的成绩
def print_score(std):
    print('%s:%s'% (std['name'],std['score']))
print(print_score(std1))

#如果采用面向对象的程序设计思想，我们首先思考的不是程序的执行流程
#而是student这种数据类型应该被视为一个对象
#这个对象拥有name和score这两个属性(property)
#如果要打印一个学生的成绩，首先必须创建处这个学生对应的对象
#然后给对象发一个print_score消息，这让对象自己把自己的数据打印出来
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
#给对象发消息实际上就是调用对象对应的关联函数，
#称为对象的方法（method）。面向对象的程序写出来就像这样：
hart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
hart.print_score()
lisa.print_score()
'''
面向对象设计思想是从自然界中来，因为自然界中类和实例的概念很自然
class是一种抽象概念，比如我们们定义的class-student。是指学生这个概念
而实例则是一个具体的student，比如Bart Simpson,Lisa Simpson
所以面向对象的程序设计思想是抽象处class，根据clsss创建instance
面向对象的抽象程度又比函数高，因为一个class既包含数据，又包含操作数据的方法

'''
#数据封装，继承，多台是面向对象的三大特点