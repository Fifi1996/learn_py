'''
文档测试
如果经常阅读官方文档，看恶意看到很多文档都用实例代码
比如re模块就带了很多实例代码

'''
import re
m=re.search('(?<=abc)def','abcdef')
print(m.group(0))
#这些代码与其他说明可以卸载注释中。然后有一些工作自动生成文档
#可以自动执行写在注释里的这些代码
def abs(n):
    '''
    Function to get absolute value of number
    Example:
    >>> abs(1)
    1
    >>>abs(-1)
    1
    >>>abs(0)
    0
    '''
    return n if n>=0 else (-n)
#明确的告诉调用者该函数的期望输入和输出

#doctest很有用，不但可以用来测试，还可以直接作为示例代码
#通过某些文档生成工具，就可以自动把包含doctest的注释提取出来