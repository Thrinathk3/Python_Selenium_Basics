from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()
act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login success")
else:
    print("Login Failed")
    print("Check your creditionals")
driver.close()

