import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class PageTitleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))


    def test_verifyAmazonHomeTitle(self):
        self.driver.get("http://www.amazon.com")
        assert "Amazon.com" in self.driver.title

    def test_verifyMacysHomeTitle(self):
        self.driver.get("http://www.macys.com")
        assert "Macy's" in self.driver.title

    # @unittest.skip("Reason")
    @unittest.skipIf(1!=1, "Number is equal")
    def test_verifyEbayHomeTitle(self):
        self.driver.get("http://www.ebay.com")
        assert "eBay" in self.driver.title

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


# driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
# driver.get("http://automationpractice.com/index.php")


