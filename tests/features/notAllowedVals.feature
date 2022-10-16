
Feature: Validate not allowed values

  Scenario Outline: As a user I want to validate not allowed values
    When I get the values that are not allowred cert_ind "<cert_ind>"
    Then validate not allowed values are removed
    Examples:
      |cert_ind|
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