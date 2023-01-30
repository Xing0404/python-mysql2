
# urlencode应用场景: 多个参数的时候

# https://www.baidu.com/s?wd=周杰伦&sex=男

# import urllib.parse
#
# data = {
#     'wd': '周杰伦',
#     'sex': '男',
#     'location': '中国台湾省'
# }
#
# a = urllib.parse.urlencode(data)    # 将中文转化为unicode编码，需要传入一个字典，会自动将字典中一个个键值对用&连接


import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url + new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode('utf-8')

print(content)