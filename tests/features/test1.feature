Feature: Validate
  not allowed vals

  Scenario: As a user I want to validate not allowed vals
    Given I have not allowed vals
    When I get the not allowed vals in the dataframe
      |cert_int|
      |abc|
      |Y|
      |y|
      |N|
      |n|
      |#|
      |!|
      |@|
      |1|
      |=|
      |-|
    Then remove the not allowed vals in the dataframe



