import time

import allure
from allure_commons.types import AttachmentType
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import Utilities.PyLogging as alLog


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = alLog.appLogger()
        self.element = None
        self.explicitWait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                          ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

    def click_element_action(self, element):
        try:
            self.explicitWait.until(ec.presence_of_element_located(element)).click()
            self.log.info("Element is successfully Located and Clicked")
        except:
            self.log.error("Element is not Located")

    def typeText_action(self, element, typeText):
        try:
            self.explicitWait.until(ec.presence_of_element_located(element)).send_keys(typeText)
            self.log.info("Element is successfully Located and text is typed")
        except:
            self.log.error(f"Element is not Located to type the text {typeText}")

    def elementEnabledStatus(self, element):
        elementEnabledStatus = None
        try:
            elementEnabledStatus = self.explicitWait.until(ec.presence_of_element_located(element)).is_enabled()
            self.log.info("Element is in Enabled Status")
        except:
            self.log.error("Element is not Located to check the status of element enabled or not")
        return elementEnabledStatus

    def elementDisplayedStatus(self, element):
        elementDisplayedStatus = None
        try:
            elementDisplayedStatus = self.explicitWait.until(ec.presence_of_element_located(element)).is_displayed()
            self.log.info("Element is Displayed")
        except:
            self.log.error("Element is not Located to check the status of element displayed or not")
        return elementDisplayedStatus

    def get_pageTitle(self):
        return self.driver.title

    def get_screenshot(self, screenshot_name):
        fileName = screenshot_name + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "./screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot saved to the Path : " + screenshotPath)

        except:
            self.log.error("Unable to save Screenshot to the Path : " + screenshotPath)

    def get_allure_screenshot(self, screenshotText):
        allure.attach(self.driver.get_screenshot_as_png(), name=screenshotText,
                      attachment_type=AttachmentType.PNG)
