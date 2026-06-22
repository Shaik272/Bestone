Feature: User registration
  Scenario: Registering with valid details
    Given I am on the ParaBank registration page
    When I fill the registration form with valid details
    And I submit the registration form
    Then the registration page should not display validation errors
