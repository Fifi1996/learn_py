'''
匿名函数
当我们再传入函数时，有些时候不需要显示的定义函数
直接传入匿名函数更方便
'''
#以map为例，计算f(x)=x^2除了定义一个f(x)函数外，还可以直接传入匿名函数
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7])))
#通过对比可以看出，匿名函数lambda x:x*x实际是：
def f(x):
    return x*x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数
'''
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该结果
好处是在没有函数名，不必担心函数名冲突，此外匿名函数也是函数对象
可以把匿名函数赋值给一个变量，再利用变量来调用该函数
'''
f=lambda x:x*x
print(f)
print(f(5))
#同样也可以把匿名函数作为返回值返回
def build(x,y):
    return lambda: x*x+y*y
'''
练习
请用匿名函数改造下面的代码
def is_odd(n):
    return n%2==1
L=list(filter(is_odd,range(1,20)))
'''
print(list(filter(lambda n:n%2==1,range(1,20))))