import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
time.sleep(3)
eur = driver.find_element(By.XPATH, "//span[text()='EUR']")
euro = driver.find_element(By.XPATH, "//a[contains(text(), 'Euro')]")
act = ActionChains(driver)
act.move_to_element(eur).perform()
euro.click()
