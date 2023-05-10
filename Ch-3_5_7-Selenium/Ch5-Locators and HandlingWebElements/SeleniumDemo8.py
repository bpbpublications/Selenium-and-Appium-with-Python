from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
# driver.get("https://jqueryui.com/datepicker/")
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe"))
# driver.find_element(By.ID, 'datepicker').click()
# while True:
#     month = driver.find_element(By.XPATH, "//*[@class='ui-datepicker-month']").text
#     year = driver.find_element(By.XPATH, "//*[@class='ui-datepicker-year']").text
#     print(month)
#     print(year)
#     if month == "April" and year == "2019":
#         driver.find_element(By.XPATH, "//*[@class='ui-datepicker-calendar']/tbody//a[text()='20']").click()
#         break
#     driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
# sleep(10)
# driver.quit()

# driver.get("https://demoqa.com/menu/")
actionPerform = ActionChains(driver)
# sleep(5) # actionPerform.move_to_element(driver.find_element(By.XPATH, "//a[text()='Main Item
# 2']")).move_to_element(driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")).move_to_element(
# driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 1']")).perform() # sleep(5) actionPerform.context_click(
# driver.find_element(By.XPATH, "//a[text()='Main Item 1']")).perform() actionPerform.double_click(
# driver.find_element(driver.find_element(By.XPATH, "//span[@id='double_click']"))).perform() sleep(5)
# driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manager")
# driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content
# resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']")) sourceElement = driver.find_element(By.XPATH,
# "//h5[text()='High Tatras 3']/following-sibling::img") targetElement = driver.find_element(By.XPATH,
# "//div[@id='trash']") actionPerform.drag_and_drop(sourceElement, targetElement).perform()



driver.get("https://www.globalsqa.com/samplepagetest/")
driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2599-comment']").send_keys("testEmail@gmail.com")
actionPerform.double_click(driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2599-comment']"))
sleep(2)
actionPerform.key_down(Keys.ALT).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
sleep(5)