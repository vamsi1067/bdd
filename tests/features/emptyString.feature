Feature: Validate empty field updated with NV

  Scenario Outline: As a user I want to validate empty field updated with NV
    When I get the empty field in the dataframe field userId "<userId>" ssId "<ssId>" resource_seq "<resource_seq>" entl_seq "<entl_seq>" cert_ind "<cert_ind>" job_desc "<job_desc>"
    Then validate empty string field is updated with NV
    Examples:
      | userId | ssId | resource_seq| entl_seq | cert_ind | job_desc|
      | empty | abc | abc |abc |abc |abc |
      | abc | empty | abc | abc| abc | abc|
      | abc | abc | empty | abc | abc | abc|
      | abc | abc | abc | empty | abc | abc|
      | abc | abc | abc | abc | empty | abc|
      | abc | abc | abc| abc | abc  | empty|
      | abc | abc | abc| abc | abc | abc|
      | empty | empty | empty | empty | empty | empty|
      | abc | empty | abc | abc | abc | $%^|

