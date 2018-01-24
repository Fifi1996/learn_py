#切片
L=['Michael','Sarah','Tracy','Bob','Jack']
#取前三个元素
print(L[0],L[1],L[2])#笨方法，若是拓展为N不适用

r=[]
n=3
for i in range(n):
    r.append(L[i])
print(r)
'''
对于这种经常取指定索引范围的操作，用循环十份繁琐
因此提供了切片slice 操作符，能简化这种操作
'''
print(L[0:3])
#表示从索引0开始取，直到3为止，但不包括3
#若第一个索引是0还可以省略
L[:3]
'''
倒数切片
倒数第一个元素的索引是-1
切片可以取任意元素
'''
M=list(range(100))
print(M[0:10])
print(M[20:30])
print(M[0:10:2])
#tuple也是一种list，唯一区别是tuple不变
#tuple也可以用切片操作
print((1,2,3,4,5)[:3])

#字符串'XXX'也可以看成是一种list，每个元素就是一个字符
#操作完仍是字符串
print('AFMSBHDJG'[3:6])
#练习
'''
利用切片操作，实现一个trim函数，
去除字符串首尾的空格，注意不要调用strip()方法
'''
def trim(s):
    if(len(s) == 0 or (s[0] != ' ' and s[-1] != ' ')):
        return s
    elif s[0] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])
if __name__ == '__main__':
    if trim('hello ') != 'hello':
        test = trim('hello ')
        print(test,'a')
        print('测试失败!')
    elif trim(' hello') != 'hello':
        test = trim(' hello')
        print(test,'b')
    elif trim(' hello ') != 'hello':
        test = trim(' hello ')
        print('测试失败!')
    elif trim('') != '':
        test = trim('')
        print(test,'d')
        print('测试失败!')
    elif trim(' ') != '':
        test = trim(' ')
        print(test,'e')
        print('测试失败!')
    else:
        print('测试成功!')
    pass
#迭代
'''
如果给定一个list/tuple,我们可以通过for循环来遍历这个list/tuple
这种遍历称为迭代Iteration
'''
#迭代是通过for ..in 来完成的，而很多语言迭代是通过下标完成的
'''
可以看出python循环抽象程度是高于c的for循环的，
因为python的for循环不禁可以用在list/tuple上
还可以作用在其他可迭代的对象上
list这种数据类型虽然有下标，但是很多数据类型师妹下标的
但是只要是可迭代对象，无论有没有下标都可以迭代
比如dict
'''
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
'''
    默认情况下，dict迭代的是key。
    如果要迭代value，可以用for value in d.values()，
    如果要同时迭代key和value，
    可以用for k, v in d.items()。
'''
#如何判断一个对象是可迭代对象，
# 用过collection模块的Iterable类型
from collections import Iterable
print(isinstance('abc',Iterable))
#如果要对list实现类似java那样下标循环怎么办
#py内置的enumerate函数可以把list变成索引-元素对
#这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
    print(i,value)

'''
练习
请使用迭代查找一个list中最小和最大值，
并返回一个tuple：
'''

def findMinMax(l):
   l.sort()
   min=l[0]
   max=l[-1]
   return min,max
print(findMinMax([1,2,3]))
'''
列表生成式 List Comprehensions
内置的来创建list的生成式

'''
print(list(range(1,11)))
print([x*x for x in range(1,11)])
#for循环厚民还可以加上if判断
print([x*x for x in range(1,11) if x%2==0])
import os
print([d for d in os.listdir('.')])

'''
列表生成器 generator
不必创建完整的list节省控件、
一边循环一边计算
'''
#法一 把【】 改为{}
g=(x*x for x in range(10))
print(next(g))
#generator 保存的是算法，每次调用next(g),
#直到没有更多元素，抛出StopIteration

#由于next(g)也是可迭代对象可以使用for循环
for n in g:
    print(n)
#斐波拉契数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(6))
#法二 print(b)换成yield b

#杨辉三角
def triangles():
    L=[1]
    yield L
    while True:
        L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1]
        yield L
n=0
for L in triangles():
    print(L)
    n=n+1
    if n==10:
        break
'''
可以被next()函数调用并不断返回下一个值的对象
称为迭代器：Iterator
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型
'''