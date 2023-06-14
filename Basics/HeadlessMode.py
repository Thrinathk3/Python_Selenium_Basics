from selenium import webdriver


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("./drivers/chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    dr = webdriver.Chrome(service=serv_obj, options=ops)
    return dr


def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("./drivers/msedgedriver.exe")
    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless")
    dr = webdriver.Edge(service=serv_obj, options=ops)
    return dr


def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("./drivers/geckodriver.exe")
    ops = webdriver.FirefoxOptions()
    ops.add_argument("--headless")
    dr = webdriver.Firefox(service=serv_obj, options=ops)
    return dr


# driver = chrome_setup()
driver = edge_setup()
# driver = firefox_setup()
driver.get("https://www.nopcommerce.com/")
print(driver.title)
print()
print(driver.current_url)
driver.close()
