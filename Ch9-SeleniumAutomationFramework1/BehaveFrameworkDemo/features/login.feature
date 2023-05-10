Feature: Login functionality
  As a user,
  I want to be able to log in to the website,
  So that I can access my account.
  Background:
    Given I am on the login page

  Scenario: Valid credentials
    When I enter valid "admin12@gmail.com" and "admin12!@"
    And I click the login button
    Then I should see the dashboard page
    And I close the browser

  Scenario: Invalid credentials
    When I enter invalid username and password
    And I click the login button
    Then I should see an error message
    And I close the browser


  Scenario Outline: Multiple credentials
    When I enter valid "<username>" and "<password>"
    And I click the login button

    Examples:
      |username                   |password           |
      |admin12@gmail.com          |admin12!@          |
      |admin12invalid@gmail.com   |admin12!@invalid   |
      |admin12invalid1@gmail.com  |admin12!@invalid1  |