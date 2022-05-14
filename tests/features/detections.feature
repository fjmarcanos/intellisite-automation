Feature: Car detections


  Scenario: Get detections
    When I send a GET request to detections
    Then the response status code is "200"
    And the response elements contain the property "_id"
    And the response elements contain the property "Year"
    And the response elements contain the property "Make"
    And the response elements contain the property "Model"
    And the response elements contain the property "Category"

  Scenario Outline: Get a specific number of detections
    Given I want to get a number of "<detections_number>" detections
    When I send a GET request with the number of detections to limit
    Then the response status code is "200"
    And the number of detections is equal to "<detections_received>"

    Examples:
      | detections_number | detections_received |
      | 3                 | 3                   |
      | 10                | 10                  |