from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# self
text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'India Pesticides')]/self::a").text
print("self Element : " + text_msg)

# parent
text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'India Pesticides')]/parent::td").text
print("Parent Element : " + text_msg)

# child
childs = driver.find_elements(By.XPATH, "//a[contains(text(),'India Pesticides')]/ancestor::tr/child::td")
print("Child Elements : ", len(childs))

# Ancestor
text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'India Pesticides')]/ancestor::tr").text
print("Ancestor Element : " + text_msg)

# Descendant
descendants = driver.find_elements(By.XPATH, "//a[contains(text(),'India Pesticides')]/ancestor::tr/descendant::*")
print("Descendant Elements : ", len(descendants))

# Following
followings = driver.find_elements(By.XPATH, "//a[contains(text(),'India Pesticides')]/ancestor::tr/following::*")
print("Following Elements : ", len(followings))

# following-sibling
followingSiblings = driver.find_elements(By.XPATH,
                                         "//a[contains(text(),'India Pesticides')]/ancestor::tr/following-sibling::tr")
print("following-sibling Elements : ", len(followingSiblings))

# Preceding
precedings = driver.find_elements(By.XPATH, "//a[contains(text(),'India Pesticides')]/ancestor::tr/preceding::*")
print("Preceding Elements : ", len(precedings))

# Preceding-sibling
precedingSiblings = driver.find_elements(By.XPATH,
                                         "//a[contains(text(),'India Pesticides')]/ancestor::tr/preceding-sibling::tr")
print("Preceding-sibling Elements : ", len(precedingSiblings))



driver.close()
