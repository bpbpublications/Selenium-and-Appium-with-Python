import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=['Chrome'], scope="class")
def fixtureSetup(request):
    driver = None
    if request.param == "Chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
    elif request.param == "Firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager("").install()))
    return driver
