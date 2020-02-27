from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\driver-999\chromedriver_win32 (4)\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.find_element_by_link_text("REGISTER").click()
driver.find_element_by_name("firstName").send_keys("Aayushi")
driver.find_element_by_name("lastName").send_keys("Garg")
driver.find_element_by_name("phone").send_keys("9012696508")
driver.find_element_by_name("userName").send_keys("aayushi@gmail.com")
driver.find_element_by_name("address1").send_keys("Shaheed Ripon Katyal Marg, Sector 17b, Gurugram")
driver.find_element_by_name("city").send_keys("Gurugram")
driver.find_element_by_name("state").send_keys("Haryana")
driver.find_element_by_name("postalCode").send_keys("122001")
select= Select(driver.find_element_by_name("country"))
select.select_by_visible_text('INDIA')
driver.find_element_by_name("email").send_keys("aayushigarg")
driver.find_element_by_name("password").send_keys("aayugarg")
driver.find_element_by_name("confirmPassword").send_keys("aayugarg")
driver.find_element_by_name("submit").click()


