Feature: API automation using Behave

  Scenario Outline: Verify user API response
    Given I send a GET request for user "<user_id>"
    Then the response status code should be <expected_status>
    And the response should contain user data
    And the response time should be less than 5 seconds

    Examples:
      | user_id | expected_status |
      | 2       | 200             |
      | 3       | 200             |
      | 4       | 200             |