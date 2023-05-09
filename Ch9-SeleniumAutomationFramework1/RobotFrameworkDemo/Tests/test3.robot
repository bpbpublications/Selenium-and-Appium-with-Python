*** settings ***
Library         SeleniumLibrary

*** variables ***
${url}                          https://magento.softwaretestingboard.com/customer/account/login
${username}                     admin12@gmail.com
${password}                     admin12!@
${name}                         Admin

*** Test Cases ***
Login Test
    Open Browser                browser=chrome
    Goto                        ${url}
    Input Text                  email                           ${username}
    Input Password              pass                            ${password}
    Click Element               xpath://*[@id="send2"]
    Wait Until Page Contains    Welcome, admin admin!
    Close Browser