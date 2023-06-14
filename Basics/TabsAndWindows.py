import time
from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


# open link in new tab
# driver.get("https://www.dummyticket.com/")
# time.sleep(3)
# buyLink = Keys.CONTROL + Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Buy Ticket").send_keys(buyLink)

# open switch to new tab and windows
driver.get("https://www.dummyticket.com/")
driver.switch_to.new_window("tab")
driver.get("http://www.orangehrm.com/")
driver.switch_to.new_window("window")
driver.get("http://www.orangehrm.com/")
time.sleep(7)
