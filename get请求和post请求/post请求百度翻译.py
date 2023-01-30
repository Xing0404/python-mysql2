# post请求

from urllib import request
import urllib.parse
import json

url = "https://fanyi.baidu.com/sug"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
}

data = {
    'kw': 'spider'
}

# post请求的参数，必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数是不会拼接在url后面的，而是需要放在请求对象定制的参数中
request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)
print(obj)