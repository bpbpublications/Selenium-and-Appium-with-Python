from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.google.com")

# service_object = Service(executable_path="/Users/yogashivamathivanan/Drivers/chromedriver")
driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.refresh()
driver.set_page_load_timeout(30)
print(driver.get_window_size())
print(driver.get_window_position())
print(driver.title)
driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print(driver.title)
driver.close()
driver.quit()

