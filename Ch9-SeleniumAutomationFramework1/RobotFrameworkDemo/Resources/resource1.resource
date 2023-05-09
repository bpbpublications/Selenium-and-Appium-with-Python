*** Keywords ***
User is able to navigate to the application
    Goto                    ${url}

Enter the valid login credentials and submit
    Input Text              email                           ${username}
    Input Password          pass                            ${password}
    Click Element           xpath://*[@id="send2"]

Validate user is successfully logged into the application
    Sleep                   5s
    ${pageTitle}            GetTitle
    Log                     ${pageTitle}
    Should be Equal         ${pageTitle}                    My Account Magento Commerce - website to practice selenium | demo website for automation testing | selenium practice sites

Get Todays date and time
    ${dateTime}             Python1.todaysTime
    Log to Console          ${dateTime}
