from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_capabilities = {'platformName': 'Android',
                        'platformVersion': '13', 'deviceName': 'Pixel 6 Pro API 33',
                        'app': '/Users/yogashivamathivanan/Downloads/Android_Demo_App.apk',
                        'appPackage': 'com.code2lead.kwad',
                        'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("CONTACT US FORM")').click()
