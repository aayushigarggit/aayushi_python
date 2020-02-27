from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome("C:\driver-999\chromedriver_win32 (4)\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/RegisterUser.htm")
driver.find_element_by_name("userName").send_keys("AayushiGarg")
driver.find_element_by_id("firstName").send_keys("Aayushi")
driver.find_element_by_id("lastName").send_keys("Garg")
driver.find_element_by_id("password").send_keys("aayugarg")
driver.find_element_by_id("pass_confirmation").send_keys("aayugarg")
driver.find_element_by_xpath("//input[@value='Female']").click()
driver.find_element_by_name("emailAddress").send_keys("aayushi@gmail.com")
driver.find_element_by_name("mobileNumber").send_keys("9012696508")
'''driver.find_element_by_name("dob").send_keys("08/16/1997")'''
driver.find_element_by_xpath("//img[@alt='Ch']").click()
select1=Select(driver.find_element_by_xpath("//select[@data-handler='selectMonth']"))
select1.select_by_visible_text("Aug")
select2=Select(driver.find_element_by_xpath("//select[@data-handler='selectYear']"))
select2.select_by_visible_text("1997")
driver.find_element_by_xpath("//a[contains(.,'16')]").click()
driver.find_element_by_name("address").send_keys("Sector 17b Gurugram")
select= Select(driver.find_element_by_name("securityQuestion"))
select.select_by_visible_text('What is your Birth Place?')
time.sleep(2)
driver.find_element_by_name("answer").send_keys("Roorkee")
driver.find_element_by_name("Submit").click()