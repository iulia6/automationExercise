Feature: Login to Website
  @smoke
  Scenario: Successful Login
    Given I am on the login page
    When I enter my username and password
    And I click the login button
    Then I should be redirected to the home page