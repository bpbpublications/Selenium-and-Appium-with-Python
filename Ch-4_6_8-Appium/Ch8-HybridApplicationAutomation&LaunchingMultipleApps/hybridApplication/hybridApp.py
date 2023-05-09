from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

desired_capabilities = {'platformName': 'Android',
                        'platformVersion': '13', 'deviceName': 'Pixel 6 Pro API 33',
                        'app': '/Users/yogashivamathivanan/Downloads/selendroid-test-app.apk',
                        'appPackage': 'com.android.chrome',
                        'appActivity': 'com.google.android.apps.chrome.Main',
                        'chromedriverExecutable':'/Users/yogashivamathivanan/Downloads/chromedriver'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

explicitWait = WebDriverWait(driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
acceptButton = explicitWait.until(ec.presence_of_element_located((AppiumBy.ID, "com.android.chrome:id/terms_accept")))
acceptButton.click()

noThanksButton = explicitWait.until(ec.presence_of_element_located((AppiumBy.ID, "com.android.chrome:id/negative_button")))
noThanksButton.click()


searchBox = explicitWait.until(ec.presence_of_element_located((AppiumBy.ID, "com.android.chrome:id/search_box_text")))
searchBox.click()

urlButton = explicitWait.until(ec.presence_of_element_located((AppiumBy.ID, "com.android.chrome:id/url_bar")))
urlButton.click()
urlButton.send_keys("https://www.apple.com")
driver.press_keycode(66)
appContexts = driver.contexts
print(driver.contexts)
for appType in appContexts:
    if appType == "WEBVIEW_chrome":
        driver.switch_to.context(appType)
        break

learnMoreLink = explicitWait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//a[@data-analytics-title='Learn more about iPhone 14']")))
learnMoreLink.click()
latestIphoneEle = explicitWait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//a[@data-analytics-title='product index']")))
latestIphone = latestIphoneEle.text
assert latestIphone == "iPhone 14", "The latest iphone is incorrect"
buylatestIphoneEle = explicitWait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//a[@class='ac-ln-button']")))
buylatestIphoneEle.click()

driver.switch_to.context("NATIVE_APP")

urlButton = explicitWait.until(ec.presence_of_element_located((AppiumBy.ID, "com.android.chrome:id/url_bar")))
urlButton.click()
urlButton.send_keys("https://www.samsung.com")
driver.quit()