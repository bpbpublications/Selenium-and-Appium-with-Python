from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class MenPage(BasePage):
    mens_pants_category_loc = (By.XPATH, "//a[text()='Pants']")
    mens_pants_firstProduct_loc = (By.XPATH, "//div[@class='product-item-info']/parent::li/parent::ol/li[1]")
    mens_pants_size = (By.XPATH, "//span[text()='Size']/following-sibling::div/div[1]")
    mens_pants_color = (By.XPATH, "//span[text()='Color']/following-sibling::div/div[1]")
    addToCart = (By.ID, "product-addtocart-button")
    cartIcon = (By.XPATH, "/div[@data-block='minicart']")
    checkout_proceed = (By.ID, "top-cart-btn-checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def clickMensPantsCategory(self):
        BasePage.click_action(self, element=self.mens_pants_category_loc)

    def addMenPants_first_ToCart_checkout(self):
        BasePage.click_action(self, element=self.mens_pants_category_loc)
        BasePage.click_action(self, element=self.mens_pants_firstProduct_loc)
        BasePage.click_action(self, element=self.mens_pants_size)
        BasePage.click_action(self, element=self.mens_pants_color)
        BasePage.click_action(self, element=self.addToCart)
        BasePage.click_action(self, element=self.cartIcon)
        BasePage.click_action(self, element=self.checkout_proceed)




