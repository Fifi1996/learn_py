'''
返回函数
函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以将函数作为结果值返回
'''
#实现一个可变参数的求和，通常是这样定义的
def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax
#如果不需要立刻求和，而是在后面的代码中根据需要再计算怎么办？
#可以不返回求和的结果，返回求和的函数
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
#当我们调用lazy_sum时，返回的是求和函数
f=lazy_sum(1,2,3,5)
print(f)
print(f())
'''
在这个例子中。我们在函数lazy_sum中有定义了函数sum，
并且内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时
相关的参数和变量都保存在返回的函数中，这种称为”闭包“的程序有极大的威力
'''
#再注意一点，当我们调用lazy_sum时，每次调用都会返回一个新的函数
#即使传入相同的参数
f1=lazy_sum(1,2,3,5)
print(f1==f)
'''
闭包
注意到返回的函数在其定义内部引用了局部变量args，
所以当一个函数返回了一个函数后，其内部的局部变量还被新的函数引用，
所以闭包用起来简单实现起来不容易
还有的问题是，返回的函数没有立刻执行，
而是调用到了f()才执行
'''
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
#在上面的例子中，每次循环都创建了一个新函数，然后把创建的桑函数都返回了
print(f1())
print(f2())
print(f3())
#结果并不是1，4，9
#而是全部都是9.原因在于返回的函数引用了变量i，但它并非立刻执行
#等到3个函数都返回时，他们所引用的变量i已经变成了3.因此最终9

#!!!返回闭包时牢记一点，返回函数不要引用任何循环变量，或者后续会发生变化的变量

'''
如果一定要引用循环变量怎么办，方法是再创建一个函数，
用该函数的参数绑定循环变量当前的值，无论后续如何改变，
已经绑到函数参数的值不变
'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
'''
练习
利用闭包返回一个计数器函数，每次调用它返回递增整数：

'''
def createCounter():
    def f():
        n=0
        while True:
            n=n+1
            yield n
    sum=f()
    def counter():
        return next(sum)
    return counter()
