url = "https://www.fragrancenet.com/fragrances?f=0!4V&page=11"
html = urlopen(url)
bs = BeautifulSoup(html.read(), "html.parser")
div = bs.findAll("span", itemprop="name")
div[0].text