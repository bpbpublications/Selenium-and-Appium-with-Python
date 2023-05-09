from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'IOS', 'platformVersion': '15.5', 'deviceName': 'iPhone 13 Pro Max',
                'automationName': 'XCUITest', 'app': (
        '/Users/yogashivamathivanan/Library/Developer/Xcode/DerivedData/UIKitCatalog-dskplzeeekmyvnbwtcjosyjblrks/Build/Products/Debug-iphonesimulator/UIKitCatalog.app')}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Views").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Simple").click()

alertElement = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='A Short Title Is Best']")
print(alertElement.get_attribute("type"))
print(alertElement.get_attribute("index"))
print(alertElement.get_attribute("label"))
print(alertElement.is_enabled())
print(alertElement.location)
print(alertElement.text)
