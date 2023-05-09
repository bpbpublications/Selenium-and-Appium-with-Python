import csv
import time

import pandas as pd

from Pages.LoginPage import Login
from Utilities import readProperties
from pathlib import Path


class Test_Login2():
    #
    # def test_successful_login_ddt(self, fixtureSetup):
    #     self.driver = fixtureSetup
    #     self.driver.get(readProperties.login_url)
    #     lp = Login(self.driver)
    #     path = Path(__file__).parent.parent.joinpath('TestData/CSV-Login.csv')
    #     with open(path, 'r') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             username = row['username']
    #             password = row['password']
    #             lp.loginToApp(username, password)
    #             pageTitle = lp.get_pageTitle()
    #             assert "My Account" in pageTitle, "Login Not Successful"
    #
    #     self.driver.close()

    def test_successful_login_ddt_pandas(self, fixtureSetup):
        self.driver = fixtureSetup
        self.driver.get(readProperties.login_url)
        lp = Login(self.driver)
        path = Path(__file__).parent.parent.joinpath('TestData/CSV-Login.csv')
        test_data = pd.read_csv(path)
        for index, row in test_data.iterrows():
            username = row['username']
            password = row['password']
            lp.loginToApp(username, password)
            pageTitle = lp.get_pageTitle()
            assert "My Account" in pageTitle, "Login Not Successful"

        self.driver.close()
