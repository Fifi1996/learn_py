'''
访问限制
在class内部，可以有属性和方法，而外部的代码可以通过直接调用实例变量的方法来操作数据
这样就隐藏了内部的复杂逻辑
但是从前面的student类的定义来看，外部代码还是可以自由的修改一个实例的name,score属性
'''
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__.
#在python中，实例的变量名如果以__开头，就变成私有变量
#只有内部可以访问，外部不能访问，
#所以把student改一改
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))
#改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量了

#bart=Student('Bart',90)
#print(bart.__name)

#这样就确保了外部代码不能随意修改对象内部的状态，通过访问限制的保护，代码恒健壮
#但是如果外部代码要获取name和score怎么办?
#可以给student增加get_name和get_score这样的方法
def get_name(self):
    return self.__name
def get_score(self):
    return self.__score
#如果又要允许修改怎么办》
#可以在增加set_score方法
def set_score(self,score):
    self.__score=score
#虽然这样大费周章，但是方法中可以对参数做检查，避免传入无效的参数
#__xx__是特殊变量，可以直接访问，__xx是私有变量
'''
练习
请把下面的student对象的gendet字段对外部隐藏起来，用get_gender（）
和set_gender代替。并检查参数的有效性
'''
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender.__str__()=='male' or gender.__str__=='female':
            self.__gender=gender
        else:
            raise ValueError('no')
bart=Student('Bart','male')
print(bart.get_gender())
