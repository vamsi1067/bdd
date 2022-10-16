Feature: Validate user organisation privileges

  Scenario Outline: As a user I want to validate user organisation privileges
    When I get the user organisation privileges "<userCol>" orgCol "<orgCol>"
    Then validate user organisation privileges
    Examples:
      | userCol | orgCol|
      | abc | abc |

