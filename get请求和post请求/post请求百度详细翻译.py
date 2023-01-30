
import urllib
import urllib.parse
import urllib.request

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Cookie':'BAIDUID=70E56D9ADCC84D6931EF902FF6E988CC:FG=1; BIDUPSID=70E56D9ADCC84D695D67B9D604E8A579; PSTM=1665722434; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=00810h0h0l2h0k8ha4a425bk1hsd9f41k; ZFY=W3iljNGmjTs4waMtqbTN:B:AqobHjvDB:ATGCLNEUfeNLE:C; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDRCVFR[Fc9oatPmwxn]=aeXf-1x8UdYcs; delPer=0; PSINO=1; H_PS_PSSID='
}



data = {
    "from": "en",
    "to": "zh",
    "query": "love",
    "transtype": "enter",
    "simple_means_flag": "3",
    "sign": "198772.518981",
    "token": "89a4cacc153b88c14be86e7147923780",
    "domain": "common",

}

# post请求的参数，必须进行编码并且调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers, data=data)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')


import json

obj = json.loads(content)
print(obj)