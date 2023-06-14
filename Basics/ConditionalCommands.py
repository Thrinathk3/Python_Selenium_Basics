import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://demo.nopcommerce.com/register/")

# is_display() is enabled()
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Displayed Status: ", search_box.is_displayed())
print("Enable Status : ", search_box.is_enabled())

# is_selected()
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("default radio button status..............")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()
print("After selecting male radio button..............")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_female.click()
print("After selecting female radio button..............")
print(rd_male.is_selected())
print(rd_female.is_selected())


# close vs quit
driver.find_element(By.LINK_TEXT, "nopCommerce").click()
time.sleep(6)
driver.close()
driver.quit()
