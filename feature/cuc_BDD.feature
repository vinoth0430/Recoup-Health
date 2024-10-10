@all
Feature: login functionality

  @smoke
  Scenario: validate username and password
    Given open browser
    When provide valid "vinothraj+1@recoup.health" and "4CssF6$5"
    Then go to all patient
    Then verify successful login or error message

  @reg
  Scenario Outline:
    Given open browser
    When provide valid "<username>" and "<password>"
    Then verify successful message
    Examples:
      | username | password |
      | vinothraj+1@recoup.health |  4CssF6$5 |
      | sdsadfssff                | dasdda    |

