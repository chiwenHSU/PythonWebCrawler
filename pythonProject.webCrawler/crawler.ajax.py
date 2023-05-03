# 抓取medium.com的文章資料
import urllib.request as req
url="https://medium.com/_/api/home-feed"
#建立request附件物件
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")  #根據觀察，取得資料為JSON格式

#解析JSON格式的資料，取的每篇文章的標題
import json
data=data.replace("])}while(1);</x>"," ")
data=json.loads(data)  #把原始的 JSON資料解析成字典/列表的表示形式
#取得json資料中的文章標題
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])