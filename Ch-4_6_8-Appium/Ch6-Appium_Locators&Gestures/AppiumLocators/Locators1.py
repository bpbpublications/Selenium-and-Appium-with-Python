from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'IOS', 'platformVersion': '15.5', 'deviceName': 'iPhone 13 Pro Max',
                'automationName': 'XCUITest', 'app': (
        '/Users/yogashivamathivanan/Library/Developer/Xcode/DerivedData/UIKitCatalog-dskplzeeekmyvnbwtcjosyjblrks/Build/Products/Debug-iphonesimulator/UIKitCatalog.app')}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# segmentElement = driver.find_element(AppiumBy.NAME, "Segmented Controls")
# segmentElement.click()
datePicker = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Date Picker")
datePicker.click()

for _ in range(10):
    try:
        value = driver.find_element(AppiumBy.ID, "elementID").is_displayed()
        if value is True:
            break
    except:
        driver.swipe(340, 1500, 3400, 1000, 5000)
        continue
driver.find_element(AppiumBy.ID, "elementID").click()