from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import sys
def getHTML(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    return html

def getNews(html):
    bs = BeautifulSoup(html.read(), "html.parser")
    news = {}
    # get the text
    blockquote = bs.blockquote
    text = blockquote.get_text()
    news['txt'] = text.replace("\u200b","")
    #get the img src and title
    news['src'] = blockquote.img['src']
    news['title'] = bs.h1.get_text()
    return news
def strimString(str):
    j = 0
    for i in range (0, len(str)):
        if str[i]!= '\n' and str[i] != '\t' and str[i] != ' ':
            j = i
            break
    str = str[j:]
    return str
def writeToFile(content, file):
    f = open(file, 'w')
    f.write(content)  # python will convert \n to os.linesep
    f.close()  # you can omit in most cases as the destructor will call it
html = getHTML("https://www.otosaigon.com/threads/ford-hua-hen-ra-mat-13-mau-xe-ev-vao-nam-2020.8756955/")
if html == None:
    print("Canoot retrieve html")
    sys.exit(0)
news = getNews(html)
print (news['txt'])
print (strimString(news['txt']))
# writeToFile(blockquote.get_text(),"/Users/Nhan/test/a.html")
html = getHTML("http://www.fragrancenet.com/perfume/narciso-rodriguez/narciso-rodriguez-narciso-poudree/eau-de-parfum#286401")
bs = BeautifulSoup(html.read(), "html.parser")