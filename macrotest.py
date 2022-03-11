#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

WAITTIME = 1000
SLEEPSEC = 5
LOOP = 3 # -1 for infinite

HOMEPAGE = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang.com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252F"
ITEMURL = "https://www.coupang.com/vp/products/71343011?itemId=238087169&vendorItemId=3584992631&q=kf94+%EB%8C%80%ED%98%95&itemsCount=36&searchId=f321d072847744a9b69b8031aef1de52&rank=3&isAddedCart="

id = 'kimsh2948'
pw = 'rlatjdgns123'

def login(driver):
    driver.find_element_by_id('login-email-input').send_keys('kimsh2948@naver.com')
    time.sleep(0.5);
    driver.find_element_by_id('login-password-input').send_keys('rlatjdgns12k')
    time.sleep(0.5);
    driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[5]/button').click()

def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

def checkStock(driver, i):
    print '재고 확인 함수'
    mktotal = driver.find_element_by_xpath("//strong[@id='MK_p_total']")
    totalPrice = mktotal.get_attribute("innerHTML")
    if (totalPrice == "0"):
        print('[%d]%s' % (i, 'out of stock'))
        return True
    else:
        print
        "Go! Checkout~"
        return False

def checkout(driver):
    print '구매하기 누르는 함수'

def order(driver):
    print '주문서 작성 함수'


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 2)

    driver.get(HOMEPAGE)
    # copy_input('//*[@id="id"]', id)
    # copy_input('//*[@id="pw"]', pw)
    login(driver)
    driver.get(ITEMURL)
    element = driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/div[3]/div[12]/div/table/tbody/tr[1]/td[1]/span")
    driver.execute_script("arguments[0].click();", element)

    i = 1
    while(checkStock(driver, i)):
        i += 1
        time.sleep(SLEEPSEC)
        if (i > LOOP and LOOP != -1):
            break
        driver.get(ITEMURL)

    checkout(driver)

    order(driver)
