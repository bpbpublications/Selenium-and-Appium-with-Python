import allure
from allure_commons.types import AttachmentType

from Base.Driver import Driver
import Utilities.PyLogging as alLog
from Pages.HomePage import Home
from Base.BasePage import BasePage
from Pages.ContactUsPage import ContactPage
import Utilities.readProp as propRead


class Test_AppHome:

    def test_valid_contactFormSubmission(self, fixtureSetup):
        log = alLog.appLogger()
        driver = fixtureSetup
        log.info("Launching Application")
        Home(driver).clickContactUsForm()
        ContactPage(driver).enterName(propRead.contactName)
        ContactPage(driver).enterEmail(propRead.contactEmail)
        ContactPage(driver).enterAddress(propRead.contactAddress)
        ContactPage(driver).enterNumber(propRead.contactPhone)
        ContactPage(driver).clickSubmitButton()
        BasePage(driver).get_allure_screenshot("ContactUsDetailsSubmitted")
        alLog.allureLogs("Successfully entered contact us form details and submitted")

