import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://jqueryui.com/datepicker/")
time.sleep(3)

driver.switch_to.frame(0)

# driver.find_element(By.ID, "datepicker").send_keys("10/03/1997")

exp_year="2021"
exp_month="March"
day="10"
driver.find_element(By.ID, "datepicker").click()
while True:
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if  exp_year == year and exp_month == month:
        break
    else:
        driver.find_element(By.XPATH, "// span[text() = 'Prev']").click()


date = driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']/a")
for d in date:
        if day == d.text:
           d.click()

time.sleep(3)
