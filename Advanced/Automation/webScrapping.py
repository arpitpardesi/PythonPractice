from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
con = html.read()
bsObj = BeautifulSoup(con, "html.parser")

print(bsObj.prettify())
for i in bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")}):
    print(i["src"])