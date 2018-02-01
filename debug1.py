'''
调试
程序能一次写完并正常运行的概率很小总会有各种各样的bug需要修正
有的bug简单看错误信息就知道了，有的bug复杂，要通过调试来修复
'''
#法一：打印可能有问题的变量
# def foo(s):
#     n=int(s)
#     print('>>>n=%d' %n )
#     return 10/n
# def main():
#     foo('0')
# main()

#法二 断言
#凡是用print来辅助查看的地方，都可以用assert来代替
def foo(s):
    n=int(s)
    assert n!=0,'n is zero'
    return 10/n
def main():
    foo('0')
#assert的意思是，表达式n!=0应该是true。否则程序运行的逻辑后面会出错
#如果断言失败，assert本书就会抛出错误

#法三：logging
#把print替换为loggging，
import logging
logging.basicConfig(level=logging.INFO)
a='0'
n=int(s)
logging.info('n=%d' %n)
print(10/n)

#法四 pdb