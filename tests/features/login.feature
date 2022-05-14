Feature: User login


  Scenario: User logs in with valid credentials
    Given an existing user with the username "user" and password "pass1234"
    When I send a POST request with the username and password
    Then the response status code is "200"
    And the response contains the field "access_token"

  Scenario: Non existent user can't log in
    Given a non existent user with the username "non-existent" and password "pass1234"
    When I send a POST request with the username and password
    Then the response status code is "401"
    And the response does not contain the field "access_token"

  Scenario: User can't log in with invalid password
    Given an existing user with the username "user" and password "invalid-password"
    When I send a POST request with the username and password
    Then the response status code is "401"
    And the response does not contain the field "access_token"

  Scenario Outline: User can't log in without required fields
    Given the username "<username>" and password "<password>"
    When I send a POST request with the username and password
    Then the response status code is "<status_code>"

    Examples:
      | username | password | status_code |
      | N/A      | pass1234 | 422         |
      | user     | N/A      | 422         |
      | N/A      | N/A      | 400         |
