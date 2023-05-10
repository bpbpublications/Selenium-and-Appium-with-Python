*** Settings ***
Library                 OperatingSystem

*** Test Cases ***
Reading content of test file
    ${contents}         Get File         ${EXECDIR}/RobotFrameworkDemo/TestData/testData1.json
    Log to Console      ${contents}