from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '15.5'
desired_caps['deviceName'] = 'iPhone 13 Pro Max'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = ('/Users/yogashivamathivanan/Library/Developer/Xcode/DerivedData/UIKitCatalog-dskplzeeekmyvnbwtcjosyjblrks/Build/Products/Debug-iphonesimulator/UIKitCatalog.app')

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


# {
#   "platformName": "IOS",
#   "appium:platformVersion": "15.5",
#   "appium:deviceName": "iPhone 13 Pro Max",
#   "appium:automationName": "XCUITest",
#   "appium:app": "/Users/yogashivamathivanan/Library/Developer/Xcode/DerivedData/UIKitCatalog-dskplzeeekmyvnbwtcjosyjblrks/Build/Products/Debug-iphonesimulator/UIKitCatalog.app"
# }