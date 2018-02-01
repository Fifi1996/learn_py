'''
单元测试
测试驱动开发test-deivern development tdd
单元测试用来对一个模块，一个函数或者一个类来进行正确性禁言的测试工作
比如对函数abs()，可以编写集合测试用例
1 输入正数 比如1 1.2 0.99 期待返回值与输入相同
2 输入负数 比如 -1 -1.2 -0.99 期待返回值与输入相反
3 输入0 期待返回0
4 输入非数值类型 比如none [] () 期待抛出typeerror
把上面的测试用例放到一个测试模块里 就是一个完整的单元测试
'''
#如果单元测试通过，说明我们测试的这个函数能够正常工作，
#如果不通过说明有bug，
#单元测试有什么意义呢
#如果我们对abs()函数代码做了修改
#只需要再跑一遍单元测试，通过说明修改不会对函数原有的行为造成影响

#以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的用例

#编写一个dict类。这个类的行为和dict一致
#可以通过属性来访问，
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key]=value
#为了编写单元测试，需要引入模块


