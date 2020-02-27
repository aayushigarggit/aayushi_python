from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:\driver-999\chromedriver_win32 (4)\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/fetchcat.htm")
window_before = driver.window_handles[0]
about=driver.find_element_by_link_text("AboutUs")
office=driver.find_element_by_xpath("//*[@id='menu3']/li[3]/ul/li/a/span")
chennai=driver.find_element_by_xpath("//*[@id='menu3']/li[3]/ul/li/ul/li[1]/a/span")

action=ActionChains(driver)
action.move_to_element(about).move_to_element(office).move_to_element(chennai).click(chennai).perform()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.switch_to_frame("main_page")
msg=driver.find_element_by_id("demo3").text
print(msg)


