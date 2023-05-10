from appium.webdriver.common.appiumby import AppiumBy
from Base.BasePage import BasePage


class Home(BasePage):
    loginIn_button_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("LOGIN")')
    tabActivity = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("TAB ACTIVITY")')
    contactUsForm = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("CONTACT US FORM")')

    def __init__(self, driver):
        super().__init__(driver)

    def clickLogin(self):
        BasePage.click_element_action(self, element=self.loginIn_button_loc)

    def isLoginButtonDisplayed(self):
        return BasePage.elementDisplayedStatus(self, element=self.loginIn_button_loc)

    def clickTabActivity(self):
        BasePage.click_element_action(self, element=self.tabActivity)

    def clickContactUsForm(self):
        BasePage.click_element_action(self, element=self.contactUsForm)
