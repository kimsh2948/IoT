from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://seantour.com/seantour_map/travel/")

bsObject = BeautifulSoup(html, "html.parser")


print(bsObject)
