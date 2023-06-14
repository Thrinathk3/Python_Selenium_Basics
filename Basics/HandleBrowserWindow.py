import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://opensource-demo.orangehrmlive.com/")
time.sleep(5)

# windowid = driver.current_window_handle
# print(windowid)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)
windowIds = driver.window_handles

# Approach1
# parentwindowid = windowIds[0]
# childwindowid = windowIds[1]
# # print(parentwindowid, childwindowid)
# driver.switch_to.window(childwindowid)
# print("title of child window ", driver.title)
#
# driver.switch_to.window(parentwindowid)
# print("title of parent window ", driver.title)

# Approach2

for winid in windowIds:
    driver.switch_to.window(winid)
    print(driver.title)

for winid in windowIds:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM":
        driver.close()