from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy

desired_capabilities = {'platformName': 'Android',
                        'platformVersion': '13', 'deviceName': 'Pixel 6 Pro API 33',
                        'app': '/Users/yogashivamathivanan/Downloads/selendroid-test-app.apk',
                        'appPackage': 'io.selendroid.testapp',
                        'appActivity': 'io.selendroid.testapp.HomeScreenActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
sleep(10)
actions = TouchAction(driver)
element = driver.find_element(AppiumBy.ID, 'io.selendroid.testapp:id/input_adds_check_box')
# # actions.tap(x=800, y=900, count=1).perform()
# actions.tap(element=element, count=1).perform()
longPressElement = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='buttonTestCD']")
# actions.long_press(longPressElement, duration=50000000)
# actions.long_press(longPressElement, duration=5).perform()
scrollToElementView = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "")
scrollToElementView.click()