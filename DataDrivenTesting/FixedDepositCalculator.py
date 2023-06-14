import time
import XLUtils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
file = "D:\\programs work space\\Python\\caldata.xlsx"
sheet = "Sheet1"
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/"
           "fixed-deposit-calculator-SBI-BSB001.html?classic=true")
row = XLUtils.getRowCount(file, sheet)
for r in range(2, row + 1):
    price = XLUtils.readData(file, sheet, r, 1)
    roi = XLUtils.readData(file, sheet, r, 2)
    pd = XLUtils.readData(file, sheet, r, 3)
    pd1 = XLUtils.readData(file, sheet, r, 4)
    frc = XLUtils.readData(file, sheet, r, 5)
    act_value = XLUtils.readData(file, sheet, r, 6)

    driver.find_element(By.ID, "principal").send_keys(price)
    driver.find_element(By.ID, "interest").send_keys(roi)
    driver.find_element(By.ID, "tenure").send_keys(pd)
    period = Select(driver.find_element(By.ID, "tenurePeriod"))
    period.select_by_visible_text(pd1)
    frequency = Select(driver.find_element(By.ID, "frequency"))
    frequency.select_by_visible_text(frc)
    driver.find_element(By.XPATH, "//div[@class='CTR PT15']/a[1]").click()
    time.sleep(3)
    exp_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text
    if float(act_value) == float(exp_value):
        XLUtils.writeData(file, sheet, r, 8, "Pass")
        XLUtils.fillGreenColor(file, sheet, r, 8)

    else:
        XLUtils.writeData(file, sheet, r, 8, "Fail")
        XLUtils.fillRedColor(file, sheet, r, 8)

    driver.find_element(By.XPATH, "//div[@class='CTR PT15']/a[2]").click()
