from bs4 import BeautifulSoup
from urllib import request
pageContent = str(request.urlopen("https://www.euronews.com/2019/10/17/bulgarian-police-arrest-six-after-racist-abuse-hurled-at-england-players-during-euro-2020").read())
pageContent = BeautifulSoup(pageContent,"html.parser")
for item in pageContent.select("p"):
    print(item.get_text())