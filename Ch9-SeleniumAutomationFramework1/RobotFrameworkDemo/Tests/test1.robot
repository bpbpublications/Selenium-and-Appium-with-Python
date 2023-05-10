*** settings ***
Library                 SeleniumLibrary
Library                 /Users/yogashivamathivanan/PycharmProjects/Frameworks/RobotFrameworkDemo/Libraries/Python1.py          name=${name}
Resource                /Users/yogashivamathivanan/PycharmProjects/Frameworks/RobotFrameworkDemo/Resources/resource1.resource
Resource                /Users/yogashivamathivanan/PycharmProjects/Frameworks/RobotFrameworkDemo/Resources/coreResource.resource
Test Setup              Open Application
Test Teardown           Close Browser

*** variables ***
${url}                  https://magento.softwaretestingboard.com/customer/account/login
${username}             admin12@gmail.com
${password}             admin12!@
${name}                 Admin

*** Test Cases ***
Validate User is able to login to the application
    Given User is able to navigate to the application
    And Enter the valid login credentials and submit
    Then Validate user is successfully logged into the application
    And Get Todays date and time


#    The value of ${EXECDIR} is different when executing the test case or suite in PyCharm compared to when executing it through the command line. This could be because PyCharm and the command line are executing the test from different directories.






