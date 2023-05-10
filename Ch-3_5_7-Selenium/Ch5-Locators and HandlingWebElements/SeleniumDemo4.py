from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.get("http://automationpractice.com/index.php")
driver.find_element(By.XPATH, "//*[@id='contact-link']//preceding-sibling::div/a").click()
driver.find_element(By.XPATH, "//*[@for='email']//following-sibling::input").send_keys("admin12@gmail.com")
driver.find_element(By.XPATH, "//label[text()='Password']//parent::div/span/input").send_keys("admin12!@")
driver.find_element(By.XPATH, "//p[@class='submit']//child::button").click()
