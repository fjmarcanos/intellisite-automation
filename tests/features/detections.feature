Feature: Car detections


  Scenario Outline: Get a specific number of detections
    Given I want to get a number of "<detections_number>" detections
    When I send a GET request with the number of detections to limit
    Then the response status code is "200"
    And the number of detections is equal to "<detections_received>"

    Examples:
      | detections_number | detections_received |
      | 3                 | 3                   |
      | 10                | 10                  |
