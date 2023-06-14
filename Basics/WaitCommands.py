from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)

mywait = WebDriverWait(driver, 10,
                       poll_frequency=2,
                       ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                           ElementNotSelectableException, Exception]
                       )
driver.get("http://www.google.com/")

searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
print("attribute", searchbox.get_attribute("value"))
print("text", searchbox.text)
searchbox.submit()
el = mywait.until(ec.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
el.click()

