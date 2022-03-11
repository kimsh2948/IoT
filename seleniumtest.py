from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\PyProject\chromedriver_win32\chromedriver')
driver.get('https://seantour.com/seantour_map/travel/');

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

time = driver.find_element_by_class_name('time')
time_t = time.text.replace('\n', ' ')
print(time_t)

hwajin = soup.find('div', class_= 'blinker spot28')
print(hwajin.text)
light_hwajin = ""
if "icon green" in str(hwajin):
    light_hwajin = "green"
elif "icon yellow" in str(hwajin):
    light_hwajin = "yellow"
elif "icon red" in str(hwajin):
    light_hwajin = "red"
print(light_hwajin)

songcamping = soup.find('div', class_= 'blinker spot46')
print(songcamping.text)
light_songcamping = ""
if "icon green" in str(songcamping):
    light_songcamping = "green"
elif "icon yellow" in str(songcamping):
    light_songcamping = "yellow"
elif "icon red" in str(songcamping):
    light_songcamping = "red"
print(light_songcamping)

songjiho = soup.find('div', class_= 'blinker spot26')
print(songjiho.text)
light_songiho = ""
if "icon green" in str(songjiho):
    light_songiho = "green"
elif "icon yellow" in str(songjiho):
    light_songiho = "yellow"
elif "icon red" in str(songjiho):
    light_songiho = "red"
print(light_songiho)

sampo = soup.find('div', class_= 'blinker spot31')
print(sampo.text)
light_sampo = ""
if "icon green" in str(sampo):
    light_sampo = "green"
elif "icon yellow" in str(sampo):
    light_sampo = "yellow"
elif "icon red" in str(sampo):
    light_sampo = "red"
print(light_sampo)

chunjin = soup.find('div', class_= 'blinker spot49')
print(chunjin.text)
light_chunjin = ""
if "icon green" in str(chunjin):
    light_chunjin = "green"
elif "icon yellow" in str(chunjin):
    light_chunjin = "yellow"
elif "icon red" in str(chunjin):
    light_chunjin = "red"
print(light_chunjin)

deung = soup.find('div', class_= 'blinker spot44')
print(deung.text)
light_deung = ""
if "icon green" in str(deung):
    light_deung = "green"
elif "icon yellow" in str(deung):
    light_deung = "yellow"
elif "icon red" in str(deung):
    light_deung = "red"
print(light_deung)

sokcho = soup.find('div', class_= 'blinker spot9')
print(sokcho.text)
light_sokcho = ""
if "icon green" in str(sokcho):
    light_sokcho = "green"
elif "icon yellow" in str(sokcho):
    light_sokcho = "yellow"
elif "icon red" in str(sokcho):
    light_sokcho = "red"
print(light_sokcho)

waiong = soup.find('div', class_= 'blinker spot29')
print(waiong.text)
light_waiong = ""
if "icon green" in str(waiong):
    light_waiong = "green"
elif "icon yellow" in str(waiong):
    light_waiong = "yellow"
elif "icon red" in str(waiong):
    light_waiong = "red"
print(light_waiong)

