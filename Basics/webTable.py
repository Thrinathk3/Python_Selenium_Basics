import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

# 1) count no of rows and columns

noOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
noOfColumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
print(noOfRows)
print(noOfColumns)

# 2) Read specific row and column data

data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
print(data)

# 3) Read all the rows and noOfColumns

for r in range(2, noOfRows + 1):
    for c in range(1, noOfColumns + 1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(data, end="        ")
    print()

# 4) Read data based on condition(list books name based on author name)
for r in range(2, noOfRows + 1):
    author = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[2]").text
    if author == "Amod":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        author1 = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[2]").text

print(bookName, "    ", author1, "     ", price)

driver.close()
