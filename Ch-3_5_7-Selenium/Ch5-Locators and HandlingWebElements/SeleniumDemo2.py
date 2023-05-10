from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.get("https://magento.softwaretestingboard.com/customer/account/login")
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("admin12@gmail.com")
driver.find_element(By.ID, "pass").send_keys("admin12!@")
driver.find_element(By.NAME, "send").click()
# driver.find_element(By.CSS_SELECTOR, "span:contains('Men')").click()
# driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("adminadmin@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "button[title='Subscribe'][type='submit']").click()
driver.find_element(By.XPATH, "//span[text()='Men']").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("adminadmin@gmail.com")
driver.find_element(By.XPATH, "//button[@title='Subscribe' and @type='submit']").click()



sleep(5)



# Luma website user creating
# https://magento.softwaretestingboard.com/customer/account/login
# admin12@gmail.com
# admin12!@