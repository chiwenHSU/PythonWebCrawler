# 抓取ptt baseball版原始碼
import urllib.request as req
url="https://www.ptt.cc/bbs/Baseball/index.html"
#建立request附件物件
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#解析原始碼取得標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div", class_="title") #尋找所有class="title"的div標籤
for title in titles:
    if title.a !=None:
        print(title.a.string)