import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Pages.LoginPage import Login
from Pages.HomePage import Home
from Configurations.TestData import TestData
from Utilities import readProperties
from Utilities.LoggerInfo import LogInfo
from Utilities import XLUtils
from pathlib import Path


class Test_Login():
    # logger = LogInfo.logGen()
    #
    # def test_logging(self, fixtureSetup):
    #     self.logger.info("________test_loginPageTitle_________")
    #     self.driver = fixtureSetup
    #     self.logger.info("________Fixture Setup Successfully created Webdriver instance_________")
    #     self.driver.get(TestData().getEnvUrlsCredentials()[0])
    #     self.logger.info("________Application URL Successfully retrieved and logged in_________")
    #     lp = Login(self.driver)
    #     pageTitle = lp.get_pageTitle()
    #     self.logger.info("________Login Page title Retrieved successfully_________")
    #     assert "Customer Login" in pageTitle, "Not a valid Page"
    #     self.logger.info("________Assertion Passed________")
    #
    # def test_loginPageTitle(self, fixtureSetup, request):
    #     self.driver = fixtureSetup
    #     self.driver.get(readProperties.login_url)
    #     # self.driver.get(TestData.URL)
    #     # Home(self.driver).clickSignIn()
    #     # self.driver.save_screenshot("/Users/yogashivamathivanan/PycharmProjects/POMFramework/Screenshots/" + "test_loginPageTitle.png")
    #     lp = Login(self.driver)
    #     pageTitle = lp.get_pageTitle()
    #     assert "Customer Login" in pageTitle, "Not a valid Page"
    #     # Take a screenshot if the test fails
    #     # if request.node.rep_call.failed:
    #     #     screenshot_path = "./Screenshots/test_loginPageTitle.png"
    #     #     self.driver.save_screenshot(screenshot_path)
    #
    #
    # def test_successful_login(self, fixtureSetup):
    #     self.driver = fixtureSetup
    #     self.driver.get(readProperties.login_url)
    #     # self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    #     lp = Login(self.driver)
    #     lp.loginToApp(username=TestData.USERNAME, password=TestData.PASSWORD)
    #     pageTitle = lp.get_pageTitle()
    #     print("Successful Login " + pageTitle)
    #     assert "My Account" in pageTitle, "Login Not Successful"
    #
    # # def test_invalid_login(self, fixtureSetup, request):
    # #     self.driver = fixtureSetup
    # #     self.driver.get(readProperties.login_url)
    # #     lp = Login(self.driver)
    # #     lp.loginToApp(username="incorrectUserName", password="incorrectPassword")
    # #     time.sleep(2)
    # #     pageTitle = lp.get_pageTitle()
    # #     print("Invalid Login " + pageTitle)
    # #     assert "Login" in pageTitle, "Login Not Successful"
    #
    def test_successful_login_ddt(self, fixtureSetup):
        self.driver = fixtureSetup
        self.driver.get(readProperties.login_url)
        lp = Login(self.driver)
        path = Path(__file__).parent.parent.joinpath('TestData/DDT-Login.xlsx')
        rowCount = XLUtils.getRowCount(path, 'Sheet1')
        for i in range(2, rowCount+1):
            lp.loginToApp(XLUtils.readData(path, 'Sheet1', i, 1), XLUtils.readData(path, 'Sheet1', i, 2))
            pageTitle = lp.get_pageTitle()
            assert "My Account" in pageTitle, "Login Not Successful"
        self.driver.close()
