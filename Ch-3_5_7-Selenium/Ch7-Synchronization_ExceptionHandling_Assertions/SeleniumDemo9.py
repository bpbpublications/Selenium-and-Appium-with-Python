import random
import time
import traceback

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import FluentWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchCookieException


driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
# driver.implicitly_wait(time_to_wait=30)
driver.get("https://magento.softwaretestingboard.com/customer/account/login")

time.sleep(5)  # This Halts the execution for 15 seconds - Unconditional Synchronization
emailElement = driver.find_element(By.XPATH, "//*[@id='email' and @type='email']")
elementWait = FluentWait(driver, 5, ignored_exceptions=[Exception], poll_frequency=2).until(ec.invisibility_of_element(emailElement))
emailElement.send_keys("admin12@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='pass' or @title='password']").send_keys("admin12!@")
# driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
# driver.find_element(By.XPATH, "//span[text()='Men']").click()
# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("adminadmin@gmail.com")
# driver.find_element(By.XPATH, "//*[contains(text(),'Subs')]").click()
#
# # Random text to find - The Webdriver waited for 30 seconds implicit wait before throwing NOSuchElementException
#
# driver.find_element(By.XPATH, "//a[text()='Tops']").click()

# driver.find_element(By.XPATH, "//*[@id='email']").send_keys("admin12@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='pass' or @title='password']").send_keys("admin12!@")
# driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
# driver.switch_to.frame("0")
# driver.switch_to.alert.accept()
# driver.switch_to.window(random.randint(5000, 5000000))





#Exception Handling

emailFieldName = driver.find_element(By.XPATH, "//div[contains(text(), 'email address')]/following-sibling::div[1]/label/span").text
# try:
#     emailTextElement = driver.find_element(By.XPATH, "//*[@id='email@#']")
# except NoSuchElementException:
#     print("No Such Element Exception happened")
try:
    raise NoSuchCookieException
except Exception:
    print("Exception is parent of all exception")

driver.find_element(By.XPATH, "//*[@id='email']").send_keys("admin12@gmail.com")
driver.find_element(By.XPATH, "//input[@id='pass' or @title='password']").send_keys("admin12!@")
driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()

assertEqual ("Selenium Python", "Selenium Python", "Comparison Done")
driver.quit()

