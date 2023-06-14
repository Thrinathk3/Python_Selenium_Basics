import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# luanching browser
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
min_slider=  driver.find_element(By.XPATH, "//body/div/div/span[1]")
max_slider=  driver.find_element(By.XPATH, "//body/div/div/span[2]")

print("locationf of sliders before moving.......")
print(min_slider.location)
print(max_slider.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -50, 0).perform()

print("locationf of sliders after moving.......")
print(min_slider.location)
print(max_slider.location)
