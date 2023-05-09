from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def typeText_action(self, element, textType):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).send_keys(textType)

    def click_action(self, element):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).click()

    def get_elementText(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).text()

    def elementEnabledStatus(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).is_enabled()

    def elementDisplayedStatus(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).is_displayed()

    def get_pageTitle(self):
        return self.driver.title

