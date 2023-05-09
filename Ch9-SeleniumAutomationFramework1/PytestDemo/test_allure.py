from time import sleep

import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import allure


@allure.severity(allure.severity_level.CRITICAL)
class TestAllure:

    @allure.description("Login Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
        driver.get("https://magento.softwaretestingboard.com/customer/account/login")
        driver.find_element(By.CSS_SELECTOR, "#email").send_keys("admin12@gmail.com")
        driver.find_element(By.ID, "pass").send_keys("admin12!@")
        driver.find_element(By.NAME, "send").click()
        sleep(5)

    @allure.severity(allure.severity_level.MINOR)
    def test_skipTheTest(self):
        pytest.skip("This test will be skipped")

    @allure.severity(allure.severity_level.NORMAL)
    def test_navigateToMenAndSubscribe(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
        driver.get("https://magento.softwaretestingboard.com/customer/account/login")
        driver.find_element(By.CSS_SELECTOR, "#email").send_keys("admin12@gmail.com")
        driver.find_element(By.ID, "pass").send_keys("admin12!@")
        driver.find_element(By.NAME, "send").click()
        sleep(5)
        driver.find_element(By.XPATH, "//span[text()='Men']").click()
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("adminadmin@gmail.com")
        driver.find_element(By.XPATH, "//button[@title='Subscribe' and @type='submit']").click()
        allure.attach(driver.get_screenshot_as_png(), name="subscribe_submitted", attachment_type=AttachmentType.PNG)
