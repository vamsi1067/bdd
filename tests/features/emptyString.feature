Feature: Validate empty field updated with NV

  Scenario Outline: As a user I want to validate empty field updated with NV
    When I get the empty field in the dataframe field userId "<userId>" ssId "<ssId>"
    Then validate empty string field is updated with NV
    Examples:
      | userId | ssId |
      | abc | empty |
      | empty | abc |


