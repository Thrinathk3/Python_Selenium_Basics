import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.ID, "dob").click()
time.sleep(3)

month = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
month.select_by_visible_text("Mar")

year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
year.select_by_visible_text("1997")

alldate = driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']/a")
for day in alldate:
    if day.text == "10":
        day.click()
        break

time.sleep(3)
