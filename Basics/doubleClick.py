import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")

input1 = driver.find_element(By.ID, "field1")
input1.clear()
input1.send_keys("Hi Tingu")

button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
act = ActionChains(driver)
act.double_click(button).perform()
time.sleep(3)
input2 = driver.find_element(By.ID, "field2").get_attribute("value")
print(input2)


