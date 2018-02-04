'''
正则表达式
re模块
有了准备知识，就可以在py中使用了，re模块
包含所有正则表达式的功能，由于字符串本身也用\转义
要特别注意
'''
s='ABC\\-001' #py的字符串
#对应的正则为'ABC\-001'
#先看看如何判断正则表达式是否匹配
import re
print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
#如果匹配成功返回一个match对象，否则none
#常见的判断方法
test='用户输入的字符串'
if re.match(r'正则表达式',test):
    print('ok')
else:
    print('fail')
'''
练习
请尝试写一个验证Email地址的正则表达式。
版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
'''
import re
def fun1(email):
    print(re.match((r'(\w*)|\.|(\w*)@(\w*).(\com)'),email))

fun1('someone@gmail.com')
fun1('bill.gates@microsoft.com')