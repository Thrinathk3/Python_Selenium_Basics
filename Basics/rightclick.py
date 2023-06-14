import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element(By.XPATH, "//span[text()='right click me']")
act = ActionChains(driver)
act.context_click(button).perform()
driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()
driver.switch_to.alert.accept()
time.sleep(3)