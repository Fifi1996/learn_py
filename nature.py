'''
实例属性和类属性
由于python是u动态语言，根据类创建的实例可以任意绑定属性
给实例绑定属性的方法是通过实例变量，或者通过self变量
'''
class Student(object):
    def __init__(self,name):
        self.name=name
s=Student('Bob')
s.score=90
#如果Student类本身需要绑定一个属性呢
#可以在class中定义属性，这种属性是类属性，归Student类所有
class Student(object):
    name='Student'
#当我们定义了一个类属性后，类的所有实例都可以访问到
s=Student() #创建实例
print(s.name) #打印name属性，因为实例没有name属性，会继续查找class
print(Student.name) #打印类的name属性
s.name='Michael' #给实例绑定name属性
print(s.name) #实例属性优先级比类属性高

#在编写程序时，千万不要对实例属性和类属性使用相同的名字
#相同名称的实例属性将屏蔽掉类属性，当你删除实例属性后，在访问的就是类属性了
'''
练习
为了统计学生人数，可以给Studnet类增加一个类属性，
每创建一个实例，该属性自动增加
'''
class Student(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1
        print(self.count)
bart=Student('Bart')