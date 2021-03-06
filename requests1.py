'''
requests
内置的urllib模块。用于访问网络资源，但用起来麻烦，缺少功能
requests处理URL资源特别方便

'''
#通过get访问一个页面
import requests
r = requests.get('https://www.douban.com/')
# 豆瓣首页
print(r.status_code)
#print(r.text)

#对于带参数的url，传入一个dict作为params参数
r=requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
print(r.url)
#requests自动检测编码，可以使徒encoding属性
print(r.encoding)

#无论相应文本还是二进制文件，都可以用content属性获得bytes对象
print(r.content)

#requests方便还在于对特定类型的响应，例如json，可以直接获取
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())
#需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/',headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

#要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
#默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON

#上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)