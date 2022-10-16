Feature: Validate whether hierarchical manager data is appended

  Scenario Outline: As a user I want to validate whether hierarchical manager data is appended or not
    When I get the hierarchical manager level "<level>" userId "<userId>" ssId "<ssId>"
    Then Validate hierarchical manager data
    Examples:
      | level | userId | ssId|
      | 1 | abc | abc |

