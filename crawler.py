## init
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib.request as ur

##
searchterm = 'cave' # will also be the name of the folder
# url = "https://www.bing.com/images/search?q="+searchterm+"&scope=images&form=QBLH&sp=-1&pq=cav&sc=8-3&qs=n&cvid=F226501568514A4088B6334F496838EE&first=1&cw=1338&ch=855"
url = "https://duckduckgo.com/?q="+searchterm+"&iax=images&ia=images"
# webdriver 사용하여 브라우저를 가져온다.
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)
# User-Agent를 통해 봇이 아닌 유저정보라는 것을 위해 사용
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
# 이미지 카운트 (이미지 저장할 때 사용하기 위해서)
counter = 0
succounter = 0


print(os.path)

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(500):
    # 스크롤 내려서 많은 이미지 미리 로
    browser.execute_script("window.scrollBy(0,180000)")

# counter = len(os.listdir("./cave"))
# print(counter);
counter = 756

## crawl
# div태그에서 class name이 rg_meta인 것을 찾아온다
# for x in browser.find_elements_by_class_name('imgpt'):
for x in browser.find_elements_by_class_name('tile--img__img'):
    counter = counter + 1

    try:
        # bing
        # imgurl = x.get_attribute('innerHTML').split("murl&quot;:&quot;")[1].split('&quot;',1)[0]
        # imgtype = imgurl.split('://')[1].split('/',1)[1].split('.')[1]

        # duckduckgo
        imgurl = x.get_attribute('src')
        imgtype = "jpg"

        # print("Total Count:", counter)
        # print("Succsessful Count:", succounter)
        print("URL:", imgurl)
        print(imgtype)
        img = imgurl

        req = ur.Request(img, headers={'User-Agent': header})
        raw_img = ur.urlopen(img).read()
        File = open(os.path.join(searchterm, searchterm + "_" + str(counter) + "." + imgtype), "wb")
        File.write(raw_img)
        File.close()
        succounter = succounter + 1
    except:
        print("can't get img")

print(succounter, "succesfully downloaded")
browser.close()