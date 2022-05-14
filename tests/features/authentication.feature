Feature: User authentication


  Scenario Outline: User is not logged in and can't access the resource
    When I send a "<http_verb>" request to the endpoint "<endpoint>"
    Then the response status code is "401"

    Examples:
      | http_verb | endpoint      |
      | POST      | /users        |
      | GET       | /users/me     |
      | GET       | /stats        |
      | GET       | /detections   |
      | GET       | /auth/refresh |
