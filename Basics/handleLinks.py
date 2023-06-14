import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://demo.nopcommerce.com/register/")

# 1) click on link
driver.find_element(By.LINK_TEXT, "Digital downloads").click()
driver.back()
time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()
# driver.back()
# time.sleep(3)

# find number of links in page
# links = driver.find_elements(By.TAG_NAME, "a")
# print(len(links))
links = driver.find_elements(By.XPATH, "//a")
print(len(links))

# print all the links
for link in links:
    print(link.text)
