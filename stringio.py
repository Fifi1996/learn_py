'''
StringIO和BytesIO
很多时候数据读写不一定是文件，也可以在内存中读写
StringIO是在内存中读写str

'''
from io import StringIO
f=StringIO()
print(f.write('hello world'))
print(f.getvalue())
#getvaule方法用于获取写入后的str

#BytesIO用例操作为进制数据
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

