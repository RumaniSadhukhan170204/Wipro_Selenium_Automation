Feature: Selenium automation using Page Object Model

  Scenario Outline: Fill registration form using POM
    Given I open the Test Automation Practice website using POM
    When I enter "<name>" in the name field using POM
    And I enter "<email>" in the email field using POM
    And I enter "<phone>" in the phone field using POM
    Then the name field should contain "<name>" using POM

    Examples:
      | name  | email             | phone      |
      | Rumani| rumani@gmail.com  | 9876543210 |
      | Alice | alice@gmail.com   | 9876543211 |


  Scenario: Select country using POM
    Given I open the Test Automation Practice website using POM
    When I select "India" from the country dropdown using POM
    Then the country dropdown should contain "India" using POM


  Scenario: Handle mouse hover using POM
    Given I open the Test Automation Practice website using POM
    When I hover over the Mouse Hover menu using POM
    And I select Mobiles using POM
    Then the mouse hover action should be completed