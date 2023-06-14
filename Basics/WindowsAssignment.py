import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("selenium")
driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']").click()
time.sleep(5)
searchlinks = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']/a")
print(len(searchlinks))
for link in searchlinks:
 link.click()

 time.sleep(10)

windowIds = driver.window_handles
for winid in windowIds:
    driver.switch_to.window(winid)
    print(driver.title)

# driver.quit()
