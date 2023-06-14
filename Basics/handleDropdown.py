import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.nopcommerce.com/en/register?returnUrl=%2Fen")
time.sleep(5)

# dropdown = driver.find_element(By.XPATH, "//select[@id='CountryId']")
select = Select(driver.find_element(By.XPATH, "//select[@id='CountryId']"))
# select.select_by_index(3)
# select.select_by_value("373")
# select.select_by_visible_text("India")
# capture all the options and print them
alloptions = select.options
print("total number of options ", len(alloptions))

for option in alloptions:
    print(option.text)

# select options from dropdown without using buit-in methods
for option in alloptions:
    if option.text == "India":
        option.click()
        break

driver.quit()
