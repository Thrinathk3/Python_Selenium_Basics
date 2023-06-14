import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.ID, "select2-billing_country-container").click()
time.sleep(3)

countries = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
for country in countries:
    if country.text == "Russia":
        country.click()
        break
print(len(countries))
time.sleep(3)
