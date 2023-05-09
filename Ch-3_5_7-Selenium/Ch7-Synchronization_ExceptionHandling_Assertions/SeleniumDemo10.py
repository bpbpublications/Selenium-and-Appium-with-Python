from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.get("https://magento.softwaretestingboard.com/customer/account/login")
# assert "LoginInvalid" in driver.title, "The Title does not contain Login"
LinksElement = driver.find_elements(By.TAG_NAME, "a")
forgotYourPasswordLink = driver.find_element(By.XPATH, "//a[@class='action remind']")
emailTextElement = driver.find_element(By.XPATH, "//*[@id='email' and @type='email']")
noOfLinks = len(LinksElement)
assert 49 == noOfLinks, "No of Links are no as expected"
if noOfLinks == 49:
    assert True
else:
    assert False

assert forgotYourPasswordLink in LinksElement, "The forgot your password link is not a part of the page."
assert forgotYourPasswordLink not in LinksElement, "The email Text element is not a link"
driver.quit()

try:
    # num = int(input("Enter First Number"))
    # num2 = int(input("Enter Second Number"))
    num = 34
    num2 = 0
    assert num2 != 0, "Number 2 Cannot be equal to 0"
    print(num/num2)
except AssertionError:
    print("Please Provide non zero number")

list1 = [1, 2, 3, 4, 4]
list2 = [1, 2, 3, 4, 4]
list3 = [1, 2, 3, 4, 4]
list4 = [1, 2, 3, 4, 4]
list5 = [1, 2, 3, 4, 5]

assert list1 == list2 == list3 == list4, "All lists are not equal"

dict1 = {"List One": list1,
         "list two": list2}
dict2 = {"List One": list3,
         "list two": list5}

assert dict1 == dict2, "the two dict are not equal"
