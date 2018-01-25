'''
py的functools模块提供了许多游泳的功能，
其中一个就是偏函数，partial function
与数学上的意义不同
在函数参数时讲到，通过设定参数的默认值，可以降低函数调用的难度
偏函数也可以做到这一点
'''
#int函数可以把字符串转化为整数，当仅传入字符串时，int()默认十进制转换
print(int('12345'))
#int还提供额外的ebase参数，默认值为10，如果传入base参数，可以做N进制转换
print(int('12345',base=8))
print(int('12345',16))
#假如要转换大量的二进制字符串，每次都传入int(x,base=2)很麻烦
#于是我们想到，卡哇伊定义一个int2()函数，默认把base=2传进去
def int2(x,base=2):
    return int(x,base)
#这样转换二进制就方便了
print(int2('1000'))

#functools.partial帮助我们创建一个偏函数，不需要我们呢定义
import functools
int2=functools.partial(int,base=2)
print(int2('1000'))
#简单来说functools.partial的作用就是把一个函数的某些参数固定
#也就是设置默认值，返回一个新的函数，调用这个新函数会更简单
#创建偏函数时，实际上可以接收函数对象，*args和**kw这3个参数
int2=functools.partial(int,base=2)
#实际上固定了int函数的关键字参数base
int2('10010')
#相当于
kw={'base':2}
int('10010',**kw)
#当传入
max2=functools.partial(max,10)
#实际上会把10作为args的一部分自动加到左边,也就是
max2(5,6,7)
#相当于
args=(10,5,6,7)
max(*args)
'''
当函数的参数太多，需要简化时，使用functools.partial可以创建一个新的函数，
这个新函数可以固定原函数的部分参数，而在调用时更简单
'''

