'''
序列化pickling
其他语言的serialization/marshaling/flattening
在程序运行中，所有的变量都是在内存中，
比如定义一个dict
'''
d=dict(name='Bob',age=20,score=90)
#可以随时修改变量，把name改为n，
#但是一旦程序结束，变量所占的内存就被操作系统全部回收
#如果没有把修改后的n存到磁盘，下次运行还是name

#我们把变量从内存中编程可存储或传输的过程称为序列化
#序列化之后可以把序列化的内容写入磁盘，或者通过网络传输到别的机器
#反过来，把变量内容从序列化的对象重新读到内存里称为反序列化

#尝试把一个对象许可i恶化写入文件
import pickle
d=dict(name='Bob',age=20,score=90)
print(pickle.dumps(d))
#pickle.dumps方法把任意对象序列化成一个bytes
#然后把这个vytes写入文件，或者用另i一个方法把对象序列化写入一个file-like object
f=open('dum[.txt','wb')
pickle.dump(d,f)
f.close()

#如果要在不痛编程语言之间传递对象，就必须把对对象序列化为标准格式
#比如XML，更好的是JSON
