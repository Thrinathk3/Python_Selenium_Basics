import time
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.nopcommerce.com/")

# get cookies and print
cookies = driver.get_cookies()
print("size of cookies", len(cookies))

# print cookies
# for c in cookies:
#     # print(c)
#     print(c.get("name"), ":", c.get("value"))

# add new cookies
driver.add_cookie({"name":"Mycookie", "value":"123456"})
cookies = driver.get_cookies()
print("size of cookies after adding a new cookie", len(cookies))

# delete specific cookie from webbrowser
driver.delete_cookie("Mycookie")
cookies = driver.get_cookies()
print("size of cookies after deleting specific cookie", len(cookies))

# delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("size of cookies after delete all cookies", len(cookies))