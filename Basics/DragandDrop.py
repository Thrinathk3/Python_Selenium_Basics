import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
act = ActionChains(driver)
# drag and drop
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

act.drag_and_drop(source, target).perform()
time.sleep(3)
