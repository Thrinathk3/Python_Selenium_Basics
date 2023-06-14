import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")


driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(5)

alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("King")

# alert.dismiss()
# driver.switch_to.alert.accept()/dismiss()
alert.accept()
