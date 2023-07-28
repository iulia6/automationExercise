Feature: Verification of Cart Page

  Scenario: Verify Subscription in Cart page
    Given I am on the main page
    When I click the 'Cart' button
    And I scroll down to footer
    And I enter email address in input and click arrow button
    Then I should see message 'You have been successfully subscribed!'
