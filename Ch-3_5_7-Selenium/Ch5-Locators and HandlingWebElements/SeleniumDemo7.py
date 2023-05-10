from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
dropdownSelect = Select(driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select"))
dropdownSelect.select_by_value("USA")

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.find_element(By.XPATH, "//input[@name='alert']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//input[@name='confirmation']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//input[@name='confirmation']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()
driver.find_element(By.XPATH, "//input[@name='prompt']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys('Test')
driver.switch_to.alert.accept()


driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
NumberOfLinksMain = driver.find_elements(By.TAG_NAME, "a")
print(len(NumberOfLinksMain))
iframeElement = driver.find_element(By.XPATH, "//*[@id='post-2632']/div[2]/div/div/div[3]/p/iframe")
# driver.switch_to.frame("globalSqa")
driver.switch_to.frame(1)
# driver.switch_to.frame(iframeElement)
NumberOfLinksIframe = driver.find_elements(By.TAG_NAME, "a")
print(len(NumberOfLinksIframe))
driver.switch_to.default_content()
driver.quit()

driver.get("https://www.globalsqa.com/")
driver.find_element(By.XPATH, "//li[@id='menu-item-6898']//a[normalize-space()='CheatSheets']").click()
mainHandle = driver.current_window_handle
driver.find_element(By.XPATH, "//a[text()='GIT Cheat Sheet']").click()
driver.find_element(By.XPATH, "//a[text()='VIM Cheat Sheet']").click()
driver.find_element(By.XPATH, "//a[text()='SQL Cheat Sheet']").click()
driver.find_element(By.XPATH, "//a[text()='Python Beginner Cheat Sheet']").click()
windowIds = driver.window_handles
for id in windowIds:
    if mainHandle != id:
        driver.switch_to.window(id)
driver.switch_to.window(windowIds[1])
pageText = driver.find_element(By.XPATH, "//strong[text()='Download GIT CheatSheet PDF']").text
driver.switch_to.window(mainHandle)
driver.find_element(By.XPATH, "//a[normalize-space()='VIM Cheat Sheet']").click()
driver.quit()


driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
numberOfRows = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
numberOfCol = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[1]/th")
print(str(len(numberOfRows)) + " and " +  str(len(numberOfCol)))
for rowData in range(2, len(numberOfRows) + 1):
    for colData in range(1, len(numberOfCol)+1):
        rowColData = driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr["+str(rowData)+"]/td["+str(colData)+"]")
        if rowColData.text == 'Amazon':
            print(driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr["+str(rowData)+"]/td[2]").text)
            print(driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr[" + str(rowData) + "]/td[3]").text)




