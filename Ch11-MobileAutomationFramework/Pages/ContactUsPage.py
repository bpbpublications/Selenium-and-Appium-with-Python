from appium.webdriver.common.appiumby import AppiumBy
from Base.BasePage import BasePage


class ContactPage(BasePage):
    enter_Name = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Enter Name")')
    enter_Email = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Enter Email")')
    enter_Address = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Enter Address")')
    enter_MobileNumber = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Enter Mobile No")')
    submitButton = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("SUBMIT")')

    def __init__(self, driver):
        super().__init__(driver)

    def enterName(self, name):
        BasePage.typeText_action(self, element=self.enter_Name, typeText=name)

    def enterEmail(self, email):
        BasePage.typeText_action(self, element=self.enter_Email, typeText=email)

    def enterAddress(self, address):
        BasePage.typeText_action(self, element=self.enter_Address, typeText=address)

    def enterNumber(self, phoneNumber):
        BasePage.typeText_action(self, element=self.enter_MobileNumber, typeText=phoneNumber)

    def clickSubmitButton(self):
        BasePage.click_element_action(self, element=self.submitButton)
