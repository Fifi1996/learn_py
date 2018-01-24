'''
高阶函数Higher-order function
变量可以指向函数
'''
#调用函数
print(abs(-10))
#只写函数
print(abs)
#函数本身可以赋值给变量，变量可以指向函数
f=abs
print(f(-10))  #变量指向了一个函数，可通过变量来调用这个函数

#传入参数
#既然变量可以指向参数，函数的参数也可以接收变量，
#那么一个函数就可以接收另一个函数作为参数，这种函数称为高阶函数
def add(x,y,f):
    return f(x)+f(y)
print(add(-5,6,abs))
#编写高阶函数，就是让函数的参数能够接收别的参数
#把函数作为参数传入，这样的函数称为高阶函数，函数式变成就是
#指这种高度抽象的编程范式
'''
python内建了map()和reduce()函数
map()函数接收两个参数，一个是函数，一个是Interable
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Interable返回
'''
#举例说明，比如我们有一个函数f(x)=x2，
#要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6])
print(list(r))
'''
map()传入的第一个参数是f。即函数对象本身，由于结果r是一个人Interable
是一个惰性序列，因此通过list()含糊是让它把整个序列都计算出来并返回一个list
'''
#不需要map()函数，写一个循环，也可以计算出结果
L=[]
for n in [1,2,3,4,5,6,7]:
    L.append(f(n))
print(L)
#的确可以，但是从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list吗？
#map()作为高阶函数，事实上他把运算规则抽象了，因此我们不但可以
#计算简单的f(x)=x^2,还可以计算任意复杂的函数，
#比如把这个list的所有数字转化为字符串
print(list(map(str,[1,2,3,4,5,6])))
'''
reduce把一个函数作用在一个序列[x1,x2,x3...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的
下一个元素做累积计算reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
#求和运算可以直接用内建函数sum()
#但是要把序列[1,3,5,7,9]变成整数13579，reduce就可以派上用场
from functools import reduce
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))
#考虑到字符串str也是一个序列，
#可以将str转换为int的函数
from functools import reduce
def fn(x,y):
    return x*10+y
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn,map(char2num,'13579')))
#整理成一个str2int的函数是：

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
#还可以用lambda函数进一步简化
from functools import reduce
DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x,y: x*10+y,map(char2num,s))
#也就是说，假设没有提供int()函数，完全可以自己写一个把字符串转换为整数的函数
''' 
练习
利用map()函数，八用户输入的不规范的英文名字，变为首字母大写
其他小写的规范名字，输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(name):
    return name.capitalize()
L1=['adam','LISA','barI']
L2=list(map(normalize,L1))
print(L2)
'''
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
def prod(L):
    return reduce(lambda x,y:x*y,L)
print(prod([3,5,7,9]))
'''
利用map和reduce编写一个str2float函数
把字符串'123.456‘转化为浮点数123,456
'''
from functools import reduce
def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)
print('\'123.4567\'=',str2float('123.4567'))

'''
内建的filter()函数用于过滤序列
和map()类似，filter也接收一个函数和一个序列，
不同的是，filter把传入的函数依次作用于每个元素，
然后根据返回值true/flase决定保留还是丢弃该元素
'''
#例如在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,3,4,6,7,9])))

#把一个序列中空的字符串删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['S','','G',None,'  '])))
#filter函数返回的是一个Iterator,也就是一个惰性序列
#要强迫完成计算结果，需要用list获得所有结果并返回list
'''
用filter求素数
计算素数的一个方法是埃氏筛法
首先列出从2开始的所有自然数，构造一个序列：
2，3，4，5，6，7，8，9，10
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3,5,7,9
取新序列的第一个数3，她一定是素数，然后用3把序列的3的倍数筛掉：
5，7：
取新序列第一个数5，有5把序列的5的倍数筛掉：
7
不断筛出得到所有的素数
'''
#先构造一个从3开始的奇数序列
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#这是一个生成器，并且是一个无限序列
#然后定义一个筛选函数
def _not_divisible(n):
    return lambda x: x%n>0
#最后定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it=_odd_iter() #初始序列
    while True:
        n=next(it) #返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it) #构造新序列
#这个生成器先返回第一个素数2，然后利用filter不断产生筛选后的新序列
#由于primes也是一个无限序列，所以调用时需要设置一个退出循环的条件
for n in primes(): #打印100以内的素数
    if n<100:
        print(n)
    else:
        break
#注意到Iterator是惰性计算的序列
#所以我们可以用py表示‘全体自然数’‘全体素数’这样的序列，代码简洁
'''
练习
回数是指从左向右读和从右向左读都是一样的数，例如12321，989
请利用filter筛选出回数：
'''
def is_palindrome(n):
    nn=str(n)
    return nn==nn[::-1]
print(list(filter(is_palindrome,range(1,100))))

'''
排序算法
排序是程序中经常用到的算法，无论是冒泡排序还是快速排序，
排序的核心是比较两个元素的大小，如果是数字就直接比较
如果是字符串过着两个dict呢？
因此比较的过程必须通过函数抽象出来
'''
#内置的sorted()可以对list进行排序
print(sorted([5,7,2,8,8]))
#此外sorted也是高阶函数，还可以接收一个key函数来实现自定义排序
#例如按照绝对值大小排序
print(sorted([3,-6,65,4],key=abs))
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
#对比原始的list和经过key=abs处理过的list:
list=[3,-6,65,4]
keys=[3, 6,65,4]
#然后sorted函数按照keys进行排序


#字符串排序的例子
print(sorted(['bab','about','Zoo']))
#默认情况下，对字符串排序是按照ASCII大小比较的，
'''
现在，我们提出排序应该忽略大小写，按照字母序排序。
要实现这个算法，不必对现有代码大加改动，
只要我们能用一个key函数把字符串映射为忽略大小写排序即可。
忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
'''
#我们给sorted传入key函数，可实现忽略大小写的排序
print(sorted(['bab','about','Zoo'],key=str.lower))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True:
print(sorted(['bab','about','Zoo'],key=str.lower,reverse=True))
#从上述例子可以看出，高阶函数的抽象能力很强大，核心代码可以保持u简介
#小结，sorted是一个高阶函数，排序的关键在实现一个映射函数
'''
练习
假设我们呢用一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''

def by_name(t):
    return t[0].lower()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1=sorted(L,key=by_name)
print(L1)
#再按成绩从高到低排序：
def by_sort(t):
    return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2=sorted(L,key=by_sort,reverse=True)
print(L2)
