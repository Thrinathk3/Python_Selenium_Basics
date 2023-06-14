import time

import mysql.connector

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

con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="classicmodels")
curs = con.cursor()
curs.execute("select * from caldata")

try:
    for row in curs:
        price = row[0]
        roi = row[1]
        pd = row[2]
        pd1 = row[3]
        frc = row[4]
        act_value = row[5]
        print("ACT_V",act_value)
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
        time.sleep(2)
        print("EXP_V", exp_value)
        if float(exp_value) == float(act_value):
            print("test passed")

        else:
            print("test failed")

        driver.find_element(By.XPATH, "//div[@class='CTR PT15']/a[2]").click()
        # print(act_value, ":", exp_value)

    con.close()

except:
    print("Conction unsuccessful..........")

driver.close()
