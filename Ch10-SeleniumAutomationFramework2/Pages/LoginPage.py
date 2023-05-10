import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class Login(BasePage):
    textbox_username_id = (By.ID, "email")
    textbox_password_id = (By.ID, "pass")
    button_signIn_id = (By.ID, "send2")
    forgotpassword_linktext = (By.LINK_TEXT, "Forgot Your Password?")
    createAccount_xpath = (By.XPATH, "//a[@class='action create primary']/span")
    customerLoginText = (By.XPATH, "//*[text()='Customer Login']")

    def __init__(self, driver):
        super().__init__(driver)

    def loginToApp(self, username, password):
        BasePage.typeText_action(self, element=self.textbox_username_id, textType=username)
        BasePage.typeText_action(self, element=self.textbox_password_id, textType=password)
        BasePage.click_action(self, element=self.button_signIn_id)

    def clickForgotPassword(self):
        BasePage.click_action(self, element=self.forgotpassword_linktext)

    def clickCreateAccount(self):
        BasePage.click_action(self, element=self.createAccount_xpath)

    def customerLoginTextDisplayed(self):
        BasePage.elementDisplayedStatus(self, element=self.customerLoginText)

