from appium import webdriver


class Driver:

    def getAndroidDriverInstance(self):
        desired_capabilities = {'platformName': 'Android',
                                'platformVersion': '13', 'deviceName': 'Pixel 6 Pro API 33',
                                'app': '/Users/yogashivamathivanan/Downloads/Android_Demo_App.apk',
                                'appPackage': 'com.code2lead.kwad',
                                'appActivity': 'com.code2lead.kwad.MainActivity'}
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        return driver

    def getIOSDriverInstance(self):
        desired_capabilities = {'platformName': 'Android',
                                'platformVersion': '13', 'deviceName': 'Pixel 6 Pro API 33',
                                'app': '/Users/yogashivamathivanan/Downloads/Android_Demo_App.apk',
                                'appPackage': 'com.code2lead.kwad',
                                'appActivity': 'com.code2lead.kwad.MainActivity'}
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        return driver
