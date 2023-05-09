import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

desired_capabilities = {'platformName': 'Android',
                        'platformVersion': '13', 'deviceName': 'Pixel 6 Pro API 33',
                        'app': '/Users/yogashivamathivanan/Downloads/Android_Demo_App.apk',
                        'appPackage': 'com.code2lead.kwad',
                        'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

explicitWait = WebDriverWait(driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
# text = "TAB ACTIVITY"
element = explicitWait.until(ec.presence_of_element_located((AppiumBy.ID, "com.testapp.sel:id/Value")))

# element = explicitWait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f"new UiSelector().text(\"{text}\")")))
element.click()
driver.quit()
