from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:\driver-999\chromedriver_win32 (4)\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
menu=driver.find_element_by_id("sub-menu")
google_link=driver.find_element_by_id("link2")

action=ActionChains(driver)
action.move_to_element(menu).move_to_element(google_link).click(google_link).perform()
driver.back()
action1= ActionChains(driver)
double_click99=driver.find_element_by_id("double-click")
action1.double_click(double_click99).perform()

alert=driver.switch_to_alert()
msg=alert.text
print(msg)
alert.accept()
