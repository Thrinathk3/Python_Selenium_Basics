import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://itera-qa.azurewebsites.net/home/automation")
# 1) select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()
time.sleep(3)


# 2) select mutliple checkbox

# checkboxs = driver.find_elements(By.XPATH, "//label[starts-with(text(), 'Which')]
#                                       /following-sibling::div[@class='form-check']")
# checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
#
# for  checkbox in checkboxs:
#     checkbox.click()

# for i in range(len(checkboxs)):
#     checkboxs[i].click()

# 3) select multiple checkbox by choice
# checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")


# for checkbox in checkboxs:
#     weekname = checkbox.get_attribute('id')
#     if weekname == 'monday' or weekname == 'friday':
#         checkbox.click()

# 4) select last two checkbox
checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
for i in range(len(checkboxs)-2, len(checkboxs)):
    checkboxs[i].click()

# 5) select first two checkbox
for i in range(len(checkboxs)-5):
    checkboxs[i].click()

# or
# for i in range(len(checkboxs)):
#     if i < 2:
#         checkboxs[i].click()

# 6) unselect the checkbox
for checkbox in checkboxs:
    if checkbox.is_selected():
        checkbox.click()
