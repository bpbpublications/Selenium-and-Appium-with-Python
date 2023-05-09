from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_capabilities = {'platformName': 'Android',
                        'platformVersion': '13', 'deviceName': 'Pixel 6 Pro API 33',
                        'app': '/Users/yogashivamathivanan/Downloads/selendroid-test-app.apk',
                        'appPackage': 'io.selendroid.testapp',
                        'appActivity': 'io.selendroid.testapp.HomeScreenActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
sleep(10)
# displayAndFocusLayout = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(9)")
# displayAndFocusLayout.click()
# button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "buttonStartWebviewCD")
# button.click()
# button = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='buttonStartWebviewCD']")
# button.click()
# buttonList = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
# print(len(buttonList))

# print(driver.current_activity)
# print(driver.current_package)
# print(driver.current_context)
# print(driver.orientation)
# print(driver.location)
# print(driver.is_locked())

driver.find_element(AppiumBy.ACCESSIBILITY_ID, "startUserRegistrationCD").click()
usernameElement = driver.find_element(AppiumBy.ID, "io.selendroid.testapp:id/inputUsername")
print(usernameElement.get_attribute("focusable"))
print(usernameElement.get_attribute("class"))
print(usernameElement.is_enabled())
print(usernameElement.is_selected())
print(usernameElement.is_displayed())
driver.quit()
