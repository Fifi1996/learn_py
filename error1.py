'''
错误处理
在程序运行过程中，如果发生了错误，可以事先约定返回一个错误代码
这样能知道为什么出错以及错误原因
错误码十分常见，比如打开文件open()
成功时返回描述符一个整数，出错时返回-1
用错误码来表示是否出错十分不便，
因为函数本身应该返回的正常结果和错误码混在一起，
造成调用者必须用大量的代码来判断是否出错
高级语言通常都内置一套tey..except,,finally的错误处理机制
'''
#举例看try机制
try:
    print('try...')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally..')
print('END')

#py的错误也是class，所有的错误累心都继承自BaseException
#在使用except时需注意，它不但捕获该类型的错误，还把其子类也一网打尽
try:
    foo()
except ValueError as e:
    print('Vaule error')
except UnicodeError as e:
    print('Unicodeerror')
#第二个except永远也捕获不到，因为unicode时vaule的子类

#使用捕捉错误还有好处是可以跨越多层调用
#比如函数main调用foo。foo调用bar。结果bar出错了，
#只要main捕获到了就可以处理
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        print('error:',e)
    finally:
        print('finally...')
#也就是说不需要在每隔可能出错的地方取捕捉错误
#较少了写错误机制的麻烦

#调用栈
#如果错误没有被捕获，他就会一直往上抛，最终被解释器捕获
#打印一个错误信息，然后程序退出


#记录错误
#如果捕获错误，自然是打印出错堆栈，但是程序也被结束了
#内置的logging模块可以很容易的记录错误信息
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
#通过配置，logging还可以把错误记录到日志文件里，方便事后排查

#抛出错误
#因为错误是class，捕获一个错误就是捕获到该class的一个实例
#要抛出错误，根据需要，先定义一个错误的class，
#选择继承关系，用raise语句抛出一个错误实例
class FooError(ValueError):
    pass
def foo(s):
    n=int(s)
    if n==0
        raise FooError('invalid vaule: %s' %s)
    return 10/n
foo('0')