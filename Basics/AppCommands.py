from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://demo.nopcommerce.com/register/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)
