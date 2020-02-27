from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:\driver-999\chromedriver_win32 (4)\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(0)
src=driver.find_element_by_id("draggable")
tgt=driver.find_element_by_id("droppable")

action=ActionChains(driver)
action.drag_and_drop(src, tgt).perform()