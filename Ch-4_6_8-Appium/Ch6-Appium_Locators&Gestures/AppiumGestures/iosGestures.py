from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'IOS', 'platformVersion': '15.5', 'deviceName': 'iPhone 13 Pro Max',
                'automationName': 'XCUITest', 'app': (
        '/Users/yogashivamathivanan/Library/Developer/Xcode/DerivedData/UIKitCatalog-dskplzeeekmyvnbwtcjosyjblrks/Build/Products/Debug-iphonesimulator/UIKitCatalog.app')}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
original_ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text View")
destination_ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Views")
driver.scroll(original_ele, destination_ele)
destination_ele.click()
