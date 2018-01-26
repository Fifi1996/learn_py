'''
模块
在程序开发过程中，随着代码越来愈多一个文件里的代码就会越来越长
为了编写可维护的代码，我们把很多函数分组分别放到不同的文件里
许多编程语言都采用这种组织代码的方式
在python中，一个.py文件就称之为一个模块
'''
#在编写程序时，经常引用其他模块包括内置和第三方模块
#使用模块可以避免函数名和变量名冲突
#若模块名冲突时可以引入包package
#按照目录存放模块xx,模块名变为packsge.xx
'''
每个包目录下会有一个_init_.py文件
必须存在才能把他当作一个包，可以是空文件也可以有代码
'''
#创建自己的模块时要注意：
'''
模块名要遵循python变量命名规范，不使用中文，特殊字符
模块名不要和系统模块名冲突，最好弦查看系统是否已经存在
检查方法是在交互环境下执行import abc若成功则说明系统存在此模块
'''

'''
使用模块
python 内置很多有用的模块，只要安装完毕，这些模块就立刻可以使用

'''
#以内奸的sys模块为例，编写一个hello模块：
#!/user/bin/env python3
# -*- coding:utf-8 -*-
'a test module'
_author_ ='Michael Liao'
import sys
#导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量可以访问该模块的所有功能
def test():
    args=sys.argv
#sys模块有一个argv变量，用list存储了命令行的所有参数
#argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args)==1:
         print('hello,world')
    elif len(args)==2:
         print('hello,%s'% args[1])
    else:
         print('too many arguments')
if __name__=='_main_':
    test()
'''
例如：
运行python3 hello.py获得的sys.argv就是['hello.py']；
运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
'''

'''
当我们在命令行运行hello模块文件时，解释器把一个特殊变量
_name_置为_main_，而如果在其他地方导入该hello模块时
if判断将失败。因此这种if测试可以让一个模块通过命令行运行时
执行一些额外的代码，最常见的就是运行测试
'''

'''
作用域
在一个模块中，我们可能会定义许多函数和变量，但有的函数和变量我们希望给
别人使用，有的函数我们仅仅在模块内部使用。在py中，是通过_前缀来实现的
'''
#正常的函数和变量名时公开的public可以直接被引用，比如abc,pi
#类似_xx_这样的变量时特殊变量，可以直接被引用但有特殊用途
#比如上面的_author_,_name_就是特殊变量,hello模块定义的文档注释也可以用
#特殊变量_doc_访问，自己的变量一般不要用这种变量名
#类似_xx这样的函数或变量就是非公开的private，不应该直接被使用
#private函数或变量不应该被别人引用，那他有什么用呢？
def _private_1(name):
    return 'hello, %s' % name
def _private_2(name):
    return 'hi,%s' % name
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
#我们在模块里公开greeting函数，而把内部逻辑用private函数隐藏了
#这样调用greeting函数不用关心内部的private函数细节
#也是一种非常有用的代码封装和抽象的方法即：
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

'''
安装第三方模块
在python中，安装第三方模块，是通过包管理工具pip完成的
假如我们呢要安装一个第三方库，-python imaging libary
这是非常强大的处理图像的工具库
因此基于PIL的Pillow项目开发非常活跃
'''
#一般来说，第三方库都会在官方的https://pypi.python.org/pypi网站注册
#要安装一个第三方库必须先知道库名
#方法一:pip install Pillow

'''
我们经常使用用到很多第三方库，例如Pillow,Mysql,web框架Flask、
用pip一个一个安装费时费力还要考虑兼容性
推荐直接使用Anaconda，是一个基于py的数据处理和科学计算平台
已经内置了许多的三方库，简单易用
'''
#模块搜索路径
#当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件
# 如果找不到，就会报错：ImportError: No module named mymodule
#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，
# 搜索路径存放在sys模块的path变量中：
#如果我们要添加自己的搜索目录，有两种方法:

#一是直接修改sys.path，添加要搜索的目录:
#import sys
#sys.path.append('/user/michael')
#这种方法是在运行时修改，运行结束后失效。

#第二种方法是设置环境变量PYTHONPATH
#该环境变量的内容会被自动添加到模块搜索路径中，
#设置方式与设置path环境变量类似，
#注意只需要添加你自己的搜索路径
