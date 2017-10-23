import urllib.parse

import urllib.request
import json

# url = "http://192.168.1.52/getPage.php"

# #创建request对象
# mydata = {"usename" : "admin" , "pwd" : "123456"}
# req = urllib.request.Request(url , method="POST" , data = bytes(json.dumps(mydata) , encoding = "utf-8"))
# result = urllib.request.urlopen(req)

# a = result.read()
# a = a.decode('gbk')
# print(a)

starname = input("请输入")
starnameurl = urllib.parse.quote(starname)
# print(starnameurl)   歌星名字的 url编码
url = "http://mobilecdn.kugou.com/api/v3/search/song?format=jsonp&keyword=" + starnameurl + "&page=1&pagesize=10&showtype=1&callback=kgJSONP238513750"

result = urllib.request.urlopen(url)
a = result.read()
a = a.decode("utf-8")
# print(a)
b = a[a.index("(") + 1:-1]
# print(b)  b 是json串

c = json.loads(b)
# print(type(c))   转化成dict


for i in c["data"]["info"]:
    if i["songname"] == "大中国":
        # print(i["hash"])  获取歌曲的hash值
        songhash = i["hash"]
        url2 = "http://m.kugou.com/app/i/getSongInfo.php?hash=" + songhash +"&cmd=playInfo"
        result2 = urllib.request.urlopen(url2)
        a2 = result2.read()
        # print(a2)
        a2 = a2.decode("utf-8")
        # print(a2)
        a2dict = json.loads(a2)
        print(a2dict["url"])