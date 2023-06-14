from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "W"
                                  "ebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[7]").click()
