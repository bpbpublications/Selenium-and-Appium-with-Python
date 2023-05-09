from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'platformName': 'IOS',
                'platformVersion': '15.5',
                'deviceName': 'iPhone 13 Pro Max',
                'autoWebview': 'true',
                'browserName': 'safari',
                'automationName': 'XCUITest'}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

explicitWait = WebDriverWait(driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
driver.get("https://www.apple.com")
print(driver.contexts)

learnMoreLink = explicitWait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//a[@data-analytics-title='Learn more about iPhone 14']")))
learnMoreLink.click()

sleep(10)
driver.quit()
