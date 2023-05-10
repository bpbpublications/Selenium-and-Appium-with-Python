from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

desired_capabilities = {'platformName': 'Android',
                        'platformVersion': '13', 'deviceName': 'Pixel 6 Pro API 33',
                        'app': '/Users/yogashivamathivanan/Downloads/WebView_3.3.5_Apkpure.apk',
                        'appPackage': 'info.android1.webview',
                        'appActivity': 'info.android1.webview.MainActivity'}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

explicitWait = WebDriverWait(driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

acceptButton1 = explicitWait.until(ec.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
acceptButton1.click()

acceptButton2 = explicitWait.until(ec.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
acceptButton2.click()
print(driver.contexts)

driver.switch_to.context("WEBVIEW_info.android1.webview")