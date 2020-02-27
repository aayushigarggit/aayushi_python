from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("C:\driver-999\chromedriver_win32 (4)\chromedriver.exe")
'''driver.maximize_window()'''
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
time.sleep(2)
driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
driver.switch_to_default_content()
time.sleep(2)
driver.back()

driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("AbstractAnnotations").click()
driver.switch_to_default_content()
time.sleep(2)
driver.back()

driver.switch_to_frame("classFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()