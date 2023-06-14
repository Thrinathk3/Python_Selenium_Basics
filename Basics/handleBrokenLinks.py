import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("http://www.deadlinkcity.com/")

alllinks = driver.find_elements(By.TAG_NAME, "a")
count = 0
for link in alllinks:
    url = link.get_attribute("href")
    try:
       res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is Broken Link")
        count += 1

    else:
        print(url, " is Valid Link")

print("total number of broken links :", count)
