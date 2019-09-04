# 向新浪发起请求，并得到相应的内容
# 导入模块
import urllib.request

# 向网站发请求，得到响应对象
response=urllib.request.urlopen('https://www.sina.com.cn/',timeout=1)
# response=urllib.request.urlopen('https://www.taobao.com/')
# 获取响应对象内容(html源码)
html=response.read().decode('utf-8')
# print(html)

print(response.geturl())
print(response.getcode())

# encode()：string 转 bytes
# decode(): bytes  转 string

