import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get("http://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)