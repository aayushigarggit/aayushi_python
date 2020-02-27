from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Hello Python")
driver=webdriver.Chrome("C:\driver-999\chromedriver_win32 (4)\chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("selenium")
time.sleep(10)
driver.find_element_by_name("btnK").click()