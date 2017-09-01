from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pickle
import socket
import socks
import requests
import datetime
def getHTML(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    return html
def getFragNetNAList():
    num = 1
    finalNAList = []
    url = "https://www.fragrancenet.com/fragrances?f=0!4V&page="
    NAList = getNAList(url + str(num))

    while (len(NAList) > 0):
        finalNAList.extent (NAList)
        num += 1
        NAList = getNAList(url + str(num))
    # now  = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    # path = os.path.join("NAlist",now)
    return finalNAList.sort()
def getMaxAroma(url):
    html = getHTML(url)
    bs = BeautifulSoup(html.read(), "html.parser")
    # div = bs.find("div",class_="dimensionContain")
    # div = bs.find("div", class_="variantText")
    txt = bs.find("div", class_="product").find("div", {"class": "name"}).getText()
    return txt
def getFrag(url):
    html = getHTML(url)
    bs = BeautifulSoup(html.read(), "html.parser")
    # div = bs.find("div",class_="dimensionContain")
    # div = bs.find("div", class_="variantText")
    div = bs.findAll("div", class_="pricing")
    return div
def getFragShop(url):
    html = getHTML(url)
    bs = BeautifulSoup(html.read(), "html.parser")
    div = bs.findAll("span", style="WHITE-SPACE: nowrap")
    prices = []
    for item in div:
        prices.append(item.text)
    return prices
def getFragex(url):
    ip = '167.160.114.188'  # change your proxy's ip
    port = 53576  # change your proxy's port
    temp = socket.socket
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
    socket.socket = socks.socksocket
    bs = BeautifulSoup(requests.get(url).text, "html.parser")
    socket.socket = temp
    div = bs.findAll("p", class_="new-price")
    prices = []
    for item in div:
        prices.append(item.text)
    return prices
#pickle the initial state
#arg: stringify version of the Beautiful Soup object
def dumpToSave(div):
    pickle.dump(div, open("save.p", "wb"))

def writeToFile(txt,fileName):
    file = open(fileName+'.txt',"a")
    file.write(txt+"\n")
    file.close()
def email(txt):
    return None

def getNAList(url):
    try:
        html = urlopen(url)
    except:
        return []
    bs = BeautifulSoup(html.read(), "html.parser")
    div = bs.findAll("span", itemprop="name")
    if len(div) == 0:
        return []
    result = []
    for item in div:
        result.append(item.text)
    return result
