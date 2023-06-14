
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# luanching browser
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# 1. scroll by pixels
# driver.execute_script("window.scrollBy(0,300)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixel moved:", value)

# # 2. scroll down page till the element is visible
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")

# print("Number of pixel moved:", value)

# # 3. scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:", value)

# # 4. scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:", value)
