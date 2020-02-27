from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:\driver-999\chromedriver_win32 (4)\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

menu=driver.find_element_by_id("menu_admin_viewAdminModule")
usermgmt=driver.find_element_by_id("menu_admin_UserManagement")
user=driver.find_element_by_id("menu_admin_viewSystemUsers")
action=ActionChains(driver)
action.move_to_element(menu).move_to_element(usermgmt).move_to_element(user).click(user).perform()
