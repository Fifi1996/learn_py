'''
调用函数须知道函数名称和参数
#python官网查看文档
#http://docs.python.org/3/library/functions.html#abs
'''

#求绝对值的函数abs
print(abs(100))
print(abs(100))
print(abs(-1))
#max函数可以接收任意多个参数，返回最大的那个
print(max(1,100,2))

'''
数据类型转化
pyhton内置的常用函数还包括数据类型转换函数
int()函数可以把其他数据类型转化为整数
'''
int('123')
int(12.34)
print(float(12.34))
#函数名其实就是指向一个函数对象的引用，函数名赋给一个变量相当于给函数起了一个别名
a=abs #变量a指向abs函数
print(a(-1))#所以可以通过a调用abs函数
#练习
#hex()函数把一个整数转换成十六进制表示的字符串
n1=255
n2=1000
print(hex(n1))
print(hex(n2))

'''
定义函数
定义函数使用def语句，依次写出函数名，括号，参数和冒号
然后缩进块中编写函数体，函数的返回值用return语句返回
'''
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-99))
'''
如果将定义的颚函数保存为xx.py文件，那么可以在该文件的当前
目录下启动python解释器，用from xx import my_abs
来导入my_abs函数
'''
#空函数
#什么事也不做的空函数，可以用pass语句
def nop():
    pass
#pass可以用来做占位符，比如现在还没想好怎么写函数里面的代码
#pass还可以用在其他语句中
#if age>=18:
#    pass
'''
参数检查
当传入不恰当的参数时，内置函数会检查出参数错误，而我们定义的
my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样
所以这个函数定义不够完善
'''
#修改下函数定义，对参数类型做检查，只允许整数和浮点数类型
#数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('had operand type')
    if x>=0:
        return x
    else:
        return -x
#print(my_abs(g))

'''
返回多个值
比如在游戏中经常需要从一个点移动到另一个店，给出坐标
位移和角度，就可以计算新的坐标
'''
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
#导入math包，并允许后续代码引用math包里的sin,cos函数
x,y=move(100,100,60,math.pi/6)
print(x,y)
#但其实这只是一种假象，函数返回仍然是单一值
#返回时tuple
#语法上tuple可以省略括号，而多个变量可以同时接收一个tuple
#按位置赋给对应的值
#按位置赋给对应的值

#练习
#定义一个函数quadratic(a,b,c)可以接收3个参数，返回一元二次方程
#a^2+bx+c=0的两个解
import math
def quadratic(a,b,c):
    n=b*b-4*a*c
    if math.sqrt(n)>0:
        x1=(-b + math.sqrt(n)) / 2 / a
        x2=(-b-math.sqrt(n))/2/a
        return x1,x2
print(quadratic(2,3,1))
'''
python的函数定义很简单，但是灵活度却很大
除正常定义的必选参数外，还可以使用默认参数，可变参数和关键字参数
使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码
'''
#位置参数
def power(x):
    return x*x
#对于power(x)函数，参数x就是一个位置参数
#当调用power函数时，必选传入有且仅有的一个参数
#power(5)
#如果计算x^3,4,5,6,次方不能定义无数个函数
#可以把power(x),改为power(x,n)
def power1(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power1(5,2))
'''
默认参数降低了函数调用的难度
有多个默认参数时，调用的时候既可以按顺序提供默认参数
enroll('Bob','M',7)意思是除了name,gender这两个参数外
最后一个参数用在age上，
我们可以把年龄和城市设为默认参数：
'''
def enroll(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city',city)
print(enroll('Sarah','F'))
#定义默认参数时要牢记一点，默认参数必须指向不变对象
'''
重点
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
'''
#可变参数
'''
在函数中，还可以定义可变函数，就是传入的参数是可变的
可以是0-任意
以数学题为例子，给出一组数字a,b,c,,,,计算a^2+b^2+c^2+++
要定义出这个函数，必须确定输入的函数，由于参数个数不确定
可以把参数作为一个list或者tuple传进来
'''
def calc(number):
    sum=0
    for n in number:
        sum=sum+n*n
    return sum\
#但是调用时需要先组装出一个list或tuple
print(calc([1,2,3]))

#接下来把函数的参数变成可变参数
def calc1(*num):
    sum=0
    for n in number:
        sum=sum+n*n
    return sum
print(calc1(1,2))
'''
定义可变参数和list/tuple参数相比，仅仅在参数前面加了*
在函数内部，参数number接收到的时一个tuple，因此函数代码完全不变
但是调用函数时，可以传入任意个参数，包括0
'''
#如果已经有一个list/tuple要调用可变参数
#num=[1,2,3]
#print(calc(*num))
#*num表示把num这个list中所有元素作为可变参数传进去
'''
关键字参数
可变参数允许你传入任意个参数，在函数调用时自动组装为tuple
而关键字允许你传入人一个含参数名的参数
这些关键字参数在函数内部自动组装成一个dict
'''
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
#函数person除了必选参数name和age外，还接受关键字参数kw
#调用该函数时，可以只传入必选参数
print(person('Micah',30))
'''
关键字参数有什么用？它可以扩展函数的功能
比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，
利用关键字参数来定义这个函数就能满足注册的需求。
和可变参数类似，也可以先组装出一个dict
然后，把该dict转换为关键字参数传进去：
'''
#参数组合
#五种参数：必选，默认，可变，关键字，命名关键字
'''
递归函数
在函数内部，可以调用其他函数
'''
#计算阶乘
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
'''
递归函数的优点是定义简单，逻辑清晰
循环方式不如递归清晰
要防止栈溢出可以使用尾递归
'''
#练习
'''
汉诺塔的移动可以用递归函数非常简单地实现。
请编写move(n, a, b, c)函数，
它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
然后打印出把所有盘子从A借助B移动到C的方法，
'''
def  move(n,a,b,c):
    if n==1:
        print(a,'-->',c)

