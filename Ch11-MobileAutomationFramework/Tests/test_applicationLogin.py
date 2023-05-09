import allure

from Base.Driver import Driver
import Utilities.PyLogging as alLog
import Utilities.readProp as propRead
from Pages.HomePage import Home
from Pages.LoginPage import Login
from Base.BasePage import BasePage


class Test_AppHome:

    def test_loginbutton_displayed(self, fixtureSetup):
        log = alLog.appLogger()
        driver = fixtureSetup
        log.info("Launching Application")
        assert Home(driver).isLoginButtonDisplayed(), "The Login Button is Not displayed"
        alLog.allureLogs("The login button is displayed and verified successfully")

    def test_successful_login(self, fixtureSetup):
        log = alLog.appLogger()
        if fixtureSetup == 'Android':
            driver = fixtureSetup
            log.info("Launching Android Application")
            Home(driver).clickLogin()
            Login(driver).enterUsernamePasswordAndLogin(propRead.username_qa, propRead.password_qa)
            alLog.allureLogs("Successfully entered username and password, Logged in")
            BasePage(driver).get_screenshot("AfterLoginPage")
        # if fixtureSetup == 'IOS':
        #     driver = fixtureSetup
        #     log.info("Launching IOS Application")