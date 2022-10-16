Feature: Validate
  empty field updated with NV

  Scenario: As a user I want to validate empty field updated with NV
    Given I have following input
    When I get the empty field in the dataframe userId "<userId>" ssid "<ssid>" resource_seq "<resource_seq>" entl_seq "<entl_seq>" cert_ind "<cert_ind>" job_desc "<job_desc>"
      |userId|ssid|resource_seq|entl_seq|cert_ind|job_desc|
      |abc|abc|abc|abc|abc|abc|
      |empty|abc|abc|abc|abc|abc|
      |abc|empty|abc|abc|abc|abc|
      |abc|abc|empty|abc|abc|abc|
      |abc|abc|abc|empty|abc|abc|
      |abc|abc|abc|abc|empty|abc|
      |abc|abc|abc|abc|abc|empty|
      |abc|abc|abc|abc|abc|#$%|

    Then validate empty string field is updated with NV



