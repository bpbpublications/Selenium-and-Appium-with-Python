import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_capabilities = {'platformName': 'Android', 'platformVersion': '13', 'deviceName': 'Pixel 6',
                        'app': '/Users/yogashivamathivanan/Downloads/DEMO_APP.apk',
                        'appPackage': 'com.Testing.karthik.extractionofuserid',
                        'appActivity': 'com.Testing.karthik.extractionofuserid.MainActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

signInButton = driver.find_element(AppiumBy.ID, 'com.Testing.karthik.extractionofuserid:id/signin')
signInButton.click()
time.sleep(2)
countryDropdown = driver.find_element(AppiumBy.ID, 'android:id/text1')
countryDropdown.click()
time.sleep(2)
countryUK = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[14]')
countryUK.click()
time.sleep(2)
email = driver.find_element(AppiumBy.ID, 'com.Testing.karthik.extractionofuserid:id/email')
email.send_keys('yogashiva1990@gmail.com')
password = driver.find_element(AppiumBy.ID, 'com.Testing.karthik.extractionofuserid:id/password')
password.send_keys('password')
signInButtonLogin = driver.find_element(AppiumBy.ID, 'com.Testing.karthik.extractionofuserid:id/signin')
signInButtonLogin.click()
time.sleep(2)
loggedInText = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TextView[2]').text
if loggedInText == 'Logged in':
    print('Successfully Logged in')
else:
    print('Log in Unsuccessful')

