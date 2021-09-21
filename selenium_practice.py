from selenium import webdriver
from selenium.webdriver.common import keys

drv = webdriver.Chrome('chromedriver.exe')
drv.get('http://google.com/ncr')
drv.close()
