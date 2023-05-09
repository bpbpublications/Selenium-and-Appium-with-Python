import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I am on the login page')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/login")


@when(u'I enter valid username and password')
def valid_username_password(context):
    context.driver.find_element(By.CSS_SELECTOR, "#email").send_keys("admin12@gmail.com")
    context.driver.find_element(By.ID, "pass").send_keys("admin12!@")


@when(u'I enter valid "{username}" and "{password}"')
def valid_username_password_parameter(context, username, password):
    context.driver.find_element(By.CSS_SELECTOR, "#email").send_keys("admin12@gmail.com")
    context.driver.find_element(By.ID, "pass").send_keys("admin12!@")


@when(u'I click the login button')
def click_login(context):
    context.driver.find_element(By.NAME, "send").click()


@then(u'I should see the dashboard page')
def verify_homePage(context):
    status = context.driver.find_element(By.XPATH, "//*[@data-ui-id='page-title-wrapper']").is_displayed()
    assert status is True


@when(u'I enter invalid username and password')
def invalid_username_password(context):
    context.driver.find_element(By.CSS_SELECTOR, "#email").send_keys("admin12invalid@gmail.com")
    context.driver.find_element(By.ID, "pass").send_keys("admin12!@invalid")


@then(u'I should see an error message')
def verify_unsuccessful_login(context):
    status = context.driver.find_element(By.NAME, "send").is_displayed()
    assert status is True


@then(u'I close the browser')
def step_impl(context):
    context.driver.quit()
