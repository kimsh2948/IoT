from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time



html = urlopen("https://seantour.com/seantour_map/travel/")
bsObject = BeautifulSoup(html, "html.parser")

time = bsObject.find('div', class_= 'time')
print(time.text())

#강원도
light_sok = bsObject.find('div', class_= 'blinker spot46')
print(light_sok.get_text())
test = light_sok.select('div a')
print(test)
sok = str(test)
if "icon green" in sok:
     print("green light")
elif "icon yellow" in sok:
     print("yellow light")
elif "icon red" in sok:
     print("red light")

light_nak = bsObject.find('div', class_= 'blinker spot8')
print(light_nak.get_text())
light_gyug = bsObject.find('div', class_= 'blinker spot6')
print(light_gyug.get_text())
light_sam = bsObject.find('div', class_= 'blinker spot10')
print(light_sam.get_text())

#부산
light = bsObject.find('div', class_= 'blinker spot7')
light = bsObject.find('div', class_= 'blinker spot1')
light = bsObject.find('div', class_= 'blinker spot2')
light = bsObject.find('div', class_= 'blinker spot3')
light = bsObject.find('div', class_= 'blinker spot5')

#대천
light = bsObject.find('div', class_= 'blinker spot4')

# print (bsObject.head.find("span")