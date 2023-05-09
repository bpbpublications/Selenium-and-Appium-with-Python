from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class Home(BasePage):
    signIn_link_loc = (By.LINK_TEXT, "Sign In")
    MenCategoryItemLink = (By.XPATH, "//a[@role = 'menuitem']//span[text()='Men']")

    def __init__(self, driver):
        super().__init__(driver)

    def clickSignIn(self):
        BasePage.click_action(self, element=self.signIn_link_loc)

    def clickMenCategoryItem(self):
        BasePage.click_action(self, element=self.MenCategoryItemLink)
