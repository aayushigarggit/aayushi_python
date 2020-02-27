from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:\driver-999\chromedriver_win32 (4)\chromedriver.exe")
driver.maximize_window()
driver.get("https://netbanking.hdfcbank.com/netbanking/?_ga=2.168672418.285822194.1582690649-2086868676.1568884235")
driver.switch_to_frame("login_page")
driver.find_element_by_name("fldLoginUserId").send_keys("aayu1234")
driver.find_element_by_xpath("//img[@alt='continue']").click()
driver.switch_to_default_content()
driver.switch_to_frame(1)
driver.find_element_by_link_text("Privacy Policy").click()