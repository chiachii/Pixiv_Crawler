#引入套件
from bs4 import BeautifulSoup
import urllib.request as req
import requests
import time

def PixivItem_URL():
    #偽裝使用者資料
    headers = {
        "user-agent" : "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2825.67 Safari/537.36",
        "cookie" : "customLocale=zh_TW"
    }

    #目標網址
    url = "https://www.pixiv.net/ranking.php?mode=daily"

    #取得網頁原始碼+解碼
    request = req.Request(url, headers=headers)
    with req.urlopen(request) as response:
        url_data = response.read().decode('utf-8')  
    pixiv_data = BeautifulSoup(url_data,'html.parser')

    #抓取圖片區資料
    img_predata = pixiv_data.find_all("section", class_="ranking-item")

    #抓第(?)名圖片資料(目前預設為第一名)
    img_data = img_predata[0] #此處的索引表示抓第(?+1)名的圖片

    #抓取圖片網址
    img_url_data = img_predata[0].find_all("img", class_="_thumbnail ui-scroll-view")
    img_url_data = str(img_url_data[0]).split(" ")

    #擷取欲回傳的部分+修飾
    img_url = img_url_data[7].replace("data-src=\"","")
    img_url = img_url.replace("\"","")
    img_url = img_url.replace("i.pximg.net","i.pixiv.cat") #反向代理：將 i.pximg.net 修改為 i.pixiv.cat
    img_url = img_url.replace("240x480","1200x1200") #改為大圖

    return(img_url)