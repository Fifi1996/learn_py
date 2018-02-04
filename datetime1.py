'''
datetime
处理日期和时间的标准库

'''
from datetime import datetime
now=datetime.now()
print(now)

#str转换为datetime
#很多时候用户输入的日期和时间是字符串
from datetime import datetime,timedelta
cday=datetime.strptime('2018-2-4 12:05:59', '%Y-%m-%d %H:%M:%S')
print(cday)
#datetime转化为str
from datetime import datetime
now=datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
#加减时间要导入timedelta类
print(now+timedelta(hours=10))
