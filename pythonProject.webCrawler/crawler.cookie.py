# 抓取ptt gossiping版原始碼
import urllib.request as req

def getData(url):
    #建立request附件物件
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #解析原始碼取得標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div", class_="title") #尋找所有class="title"的div標籤
    for title in titles:    #篩選出未被刪除的文章純文字標題
        if title.a !=None:
            print(title.a.string)
    #抓取下一頁的連結
    nextlink=root.find("a",string="‹ 上頁")   #找到內文是‹ 上頁 的 a 標籤
    return nextlink["href"]

#Main：抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html" #第一頁是固定的
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
