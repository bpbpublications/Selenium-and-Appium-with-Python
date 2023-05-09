from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
# print(driver.page_source)
driver.find_element(By.XPATH, "//*[@id='contact-link']//preceding-sibling::div/a").click()
print(driver.get_cookies())
print(driver.get_cookie('name'))
driver.find_element(By.XPATH, "//*[@for='email']//following-sibling::input").send_keys("admin12@gmail.com")
driver.find_element(By.XPATH, "//label[text()='Password']//parent::div/span/input").send_keys("admin12!@")
print(driver.find_element(By.XPATH, "//p[@class='submit']//child::button").get_attribute('class'))
driver.find_element(By.XPATH, "//p[@class='submit']//child::button").click()
print(driver.title)
driver.find_element(By.CSS_SELECTOR, "a[title='Women']").click()
print(driver.find_element(By.CSS_SELECTOR, "a[title='Women']").text)
driver.back()
print(driver.current_url)
# countLinks = driver.find_elements(By.TAG_NAME, "a")
# priceContentNumber = driver.find_elements(By.CLASS_NAME, 'content_price')
# print("Number of Links =" + str(len(countLinks)) +" and Number of priceContent " + str(len(priceContentNumber)))
