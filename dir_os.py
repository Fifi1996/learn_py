'''
操作文件和目录
如果我们要操作文件。目录
可以在操作系统输入dir.cp等命令
内置的os模块可以直接调用接口参数
'''
import os
print(os.name) #操作系统类型
#如果是posix，系统是liinux/mac，nt是win系统
#要获取详细的系统信息，可以调用uname()

#操作系统中定义的环境变量，全部保存在os,environ这个变量中
print(os.environ)
#要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get('PATH'))

#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，

#查看当前目录的绝对路径
print(os.path.abspath('.'))

#把两个路径合成一个时，不要直接拼字符串，通过os.path.join
#拆分split
