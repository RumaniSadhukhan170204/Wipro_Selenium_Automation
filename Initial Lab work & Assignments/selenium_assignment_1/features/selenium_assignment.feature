Feature: Selenium automation using Behave

  Scenario: Fill the registration form
    Given I open the Test Automation Practice website
    When I enter "Rumani" in the name field
    And I enter "rumani@gmail.com" in the email field
    And I enter "9876543210" in the phone field
    Then the name field should contain "Rumani"

  Scenario: Select country from dropdown
    Given I open the Test Automation Practice website
    When I select "India" from the country dropdown
    Then the country dropdown should contain "India"

  Scenario: Handle mouse hover
    Given I open the Test Automation Practice website
    When I hover over the Mouse Hover menu
    And I select Mobiles
    Then the mouse hover action should be completed