import os


class TestData:
    URL = "https://magento.softwaretestingboard.com/"
    USERNAME = "admin12@gmail.com"
    PASSWORD = "admin12!@"
    appEvn = os.environ.get("APP_TEST_ENVIRONMENT")

    def getEnvUrlsCredentials(self):
        if self.appEvn == "STAGING":
            URL_STAGING = "https://magento.softwaretestingboard.com/customer/account/login/"
            USERNAME_STAGING = "admin12@gmail.com"
            PASSWORD_STAGING = "admin12!@"
            return [URL_STAGING, USERNAME_STAGING, PASSWORD_STAGING]
        elif self.appEvn == "QA":
            URL_QA = "https://magento.qa.softwaretestingboard.com/"
            USERNAME_QA = "admin12_qa@gmail.com"
            PASSWORD_QA = "admin12!@"
            return [URL_QA, USERNAME_QA, PASSWORD_QA]

    def getCurrentUsersHomeDirectory(self):
        home_dir = os.environ['HOME']
        print(home_dir)
        os.environ['TEST_VAR'] = "Test_Value"
        print(os.environ['TEST_VAR'])


if __name__ == '__main__':
    TestData().getCurrentUsersHomeDirectory()




