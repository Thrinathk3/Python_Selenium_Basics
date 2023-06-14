import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://text-compare.com/")

input1 = driver.find_element(By.ID, "inputText1")
input2 = driver.find_element(By.ID, "inputText2")

input1.send_keys("Welcome")
time.sleep(2)
act = ActionChains(driver)
# copy
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# click tab button
act.send_keys(Keys.TAB).perform()
# paste
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(2)
