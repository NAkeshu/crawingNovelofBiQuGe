# 网站：笔趣阁 http://www.biquge.com.tw/
# 测试文章：飞剑问道 http://www.biquge.com.tw/18_18820/
# 使用前将main()中BookId的00_00000替换成小说代码(例：飞剑问道代码 18_18820)


from bs4 import BeautifulSoup
import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def findAllTags(html, url):
    list = []
    bsObj = BeautifulSoup(html, "html.parser")
    for a in bsObj.findAll("dd"):
        for tag in a.children:
            pat = re.compile(r'\/\d{2}\_\d{5}')
            newUrl = pat.sub("", url)   # http://www.biquge.com.tw
            list.append(newUrl + tag.attrs["href"])
    return list

def getchapText(chapUrl):
    chapList = []
    chapHtml = getHTMLText(chapUrl)
    chapObj = BeautifulSoup(chapHtml, "html.parser")
    chapName = chapObj.find("h1")
    # print (chapName.get_text())
    chapList.append(chapName.get_text())
    chapText = chapObj.find(id="content")
    # print (chapText.get_text())
    chapList.append(chapText.get_text())
    return chapList

def saveinaFile(chapList):
    FileName = chapList.pop(0) + ".txt"
    try:
        with open(FileName, "w", encoding='utf-8') as f:
            chaptext = chapList.pop()
            f.write(chaptext)
        print(FileName + "保存成功")
    except OSError as e:
        print(FileName + "保存失败")





def main():
    TempUrl = "http://www.biquge.com.tw/"
    BookId = "00_00000"
    url = TempUrl + BookId
    # url = "http://www.biquge.com.tw/16_16209"
    html = getHTMLText(url)

    chapList = findAllTags(html, url)
    for aChap in chapList:
        oneChap = getchapText(aChap)
        saveinaFile(oneChap)
    print("小说保存结束")

# for u in findAllTags(html):
#     print (u)

if __name__ == "__main__":
    main()
