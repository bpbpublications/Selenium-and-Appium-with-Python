from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_capabilities = {'platformName': 'Android',
                        'platformVersion': '13', 'deviceName': 'Pixel 6 Pro API 33',
                        'app': '/Users/yogashivamathivanan/Downloads/Android_Demo_App.apk',
                        'appPackage': 'com.code2lead.kwad',
                        'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("TAB ACTIVITY")').click()

deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']
print('width: ' + str(screenWidth) + 'height: ' + str(screenHeight))
# Swipe right to left
driver.swipe(start_x=screenWidth * .9, start_y=screenHeight * .5, end_x=screenWidth * .1, end_y=screenHeight * .5,
             duration=5000)
# Swipe left to right
driver.swipe(start_x=screenWidth * .1, start_y=screenHeight * .5, end_x=screenWidth * .9, end_y=screenHeight * .5,
             duration=5000)
# Swipe bottom to top
driver.swipe(start_x=screenWidth * .5, start_y=screenHeight * .8, end_x=screenWidth * .5, end_y=screenHeight * .3,
             duration=5000)
# Swipe top to bottom
driver.swipe(start_x=screenWidth * .5, start_y=screenHeight * .3, end_x=screenWidth * .5, end_y=screenHeight * .8,
             duration=5000)
