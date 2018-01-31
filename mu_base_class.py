'''
多重继承
继承时面向对象编程的一个重要的方式，通过继承，子类可以扩展父类的功能

回忆一下Animal类层次的设计，假如实现以下四种动物
Dog - 狗狗；
Bat - 蝙蝠；
Parrot - 鹦鹉；
Ostrich - 鸵鸟。
按照哺乳类华和鸟类归类
按照能跑，能飞归类
把上面两种包含进来可以设计更多
哺乳类：能跑的哺乳类，能飞的哺乳类；
鸟类：能跑的鸟类，能飞的鸟类。

如果再增加，类的数量会呈指数增长，这样设计时不行的

'''
#正确的做法是采用多重继承，首先主要的类层次仍按照哺乳类和鸟类设计
class Aniaml(object):
    pass
#大类
class Mammal(Aniaml):
    pass
class Bird(Aniaml):
    pass
#各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrish(Bird):
    pass

#给动物加上Runnanle和Flyable的功能，需要先定义类
class Runnable(object):
    def run(self):
        print('run...')
class Flyable(object):
    def fly(self):
        print('fly...')

#对于需要Run功能的动物，就多继承一个Runnable,例如Dog
class Dog(Mammal,Runnable):
    pass
#通过多重继承，一个子类可以同时获得多个父类的所有功能

'''
MixIn
在设计类的继承关系时，通常，主线都是单一继承下来的
例如，Ostrich继承自Bird。
但是，如果需要“混入”额外的功能，
通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，
再同时继承Runnable。这种设计通常称之为MixIn。

为了更好地看出继承关系，
我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，
让某个动物同时拥有好几个MixIn：
'''
#目的就是给一个类增加多个功能，这样设计时优先考虑通过多重继承来组合
#多个MixIn的功能，而不是设计多层次的复杂继承关系

#自带的很多库也使用了MixIn,例如TCPServer.UDPServer
#这两类网络服务，要同时服务多个用户使用多进程或多线程模块
#两种模型由ForkingMixIn和ThreadingMinxIn提供
#通过组合，可以创造除合适的服务来


#编写一个多进程模式的Tcp服务：
class MyTCPServer(MyTCPServer,ForkingMixIn):
    pass
#编写一个多线程模式的udp服务：
class MyUDPServer(UDPServer,ThreadingMixIn):
    pass

#小结
#python允许使用多重继承，MixIn是一种常见的设计
#只允许单一继承的语言（java），不能使用