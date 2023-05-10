import time
from selenium import webdriver


class Test_Web():
    # Using Chrome
    def test_chrome(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=chrome_options
        )

        chrome_driver.get("https://www.google.com")

        chrome_driver.quit()

    # Using Firefox
    def test_firefox(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--ignore-ssl-errors=yes')
        firefox_options.add_argument('--ignore-certificate-errors')
        ff_driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=firefox_options
        )

        ff_driver.get("https://www.google.com")

        ff_driver.quit()

    def test_edge(self):
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--ignore-ssl-errors=yes')
        edge_options.add_argument('--ignore-certificate-errors')
        edge_driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=edge_options
        )

        edge_driver.get("https://www.google.com")

        edge_driver.quit()
