import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("./drivers/chromedriver.exe")

    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    dr = webdriver.Chrome(service=serv_obj, options=ops)
    return dr


def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("./drivers/msedgedriver.exe")

    preferences = {"download.default_directory": location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    dr = webdriver.Chrome(service=serv_obj, options=ops)
    return dr


def firefox_set():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("./drivers/geckodriver.exe")

    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  # msword
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)  # 0-desktop, #1-default #2 desired location
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disable", True)

    dr = webdriver.Firefox(service=serv_obj, options=ops)
    return dr


driver = chrome_setup()
# driver = edge_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a").click()
time.sleep(3)

# upload file
# driver.find_element(By.TAG_NAME, "input").send_keys("path of the file")
