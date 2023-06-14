import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(5)
driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']/li[1]").click()
time.sleep(10)
empnames = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']/descendant::div[@class='oxd-table-cell "
                                          "oxd-padding-cell'][2]/div")

for empname in empnames:
    print(empname.text)

empstatus = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']/descendant::div[@class='oxd-table-cell "
                                           "oxd-padding-cell'][5]/div")
count = 0

for status in empstatus:
    if "Enabled" == status.text:
        count = count + 1

print("total no of employees ", len(empstatus))
print("enabled employess ", count)
print("disabled employees ", len(empstatus) - count)
