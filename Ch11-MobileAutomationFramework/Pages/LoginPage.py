from appium.webdriver.common.appiumby import AppiumBy
from Base.BasePage import BasePage


class Login(BasePage):
    email_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Enter Email")')
    password_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Enter Password")')
    loginButton = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("LOGIN")')

    def __init__(self, driver):
        super().__init__(driver)

    def enterUsernamePasswordAndLogin(self, username, password):
        BasePage.typeText_action(self, element=self.email_loc, typeText=username)
        BasePage.typeText_action(self, element=self.password_loc, typeText=password)
        BasePage.click_element_action(self, element=self.loginButton)
