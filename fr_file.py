'''
文件读写
读写文件是最常见的IO操作，
内置了读写文件的函数，用法和c是兼容的
读写文件前，必须了解一下，在磁盘上读写文件的功能都是由
操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘
所以读写文件就是请求操作系统打开一个文件对象（通常为文件描述符）
然后通过操作系统提供的接口从这个文件对象中提取数据（读文件）
或者把数据细微入这个文件对象（写文件）
'''
#读文件
#要以读文件的模式打开一个文件对象，内置的open传入文件名和标识符
f=open('E:\git/test.txt','r')
#如果文件打开成功，接下来调用read方法可以一次读取文件的全部内容
#读到内存，用一个str对象表示
print(f.read())
#文件使用完毕必须关闭，文件对象会占用操作系统资源，
#系统同一时间能打开的文件数量也是有限的
f.close()

#读写可能产生IOerror,用错误机制
try:
    f = open('E:\git/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
#每次这么写麻烦，引入with来自动调用close
with open('E:\git/test.txt','r') as f:
    print(f.read())

#为了防止文件过大一次性调用内存爆，可以反复调用read(size)
#每次读取size字节的内容
# for line in f.readline():
#     print(line.strip())#删除末尾的'\n'

'''
file-like object
像open函数返回这种还有个read方法的对象，统称为file-like object
除了file外，还可以是内存的字节流，网络流，自定义流等等
不要求特定继承类，只要写个read方法
StringIO就是在内存中创建file-like object，常用作临时缓冲
'''
#二进制文件
#前面默认的是文本文件，并且是utf-8编码的文本文件
#要读取二进制文件用'rd'模式
f=open('E:\git/test.txt','rb')
print(f.read())

#字符文件
#要读取非utf-8编码的文件，需要给open传入encoding参数
#比如读取gbk编码的文件
f=open('E:\git/test.txt','r',encoding='gbk')
print(f.read())

#写文件
#传入标识符改为'w'/wb
f=open('E:\git/test.txt','w')
print(f.write('hello'))
f.close()
