Feature: Google.com Web Browsing
  As a web surfer,
  I want to have possibility to interact with all Google services available on the main page


  Background:
    Given the Google.com home page is displayed(english)

@google @image
  Scenario: Go to Google Image page
    When I click "Image"
    Then I am redirected to the Google "Images" page
    And title is correct on the "Images" page

@gmail
  Scenario: Go to Gmail page
    When I click "Gmail"
    Then I redirected to the "Gmail" page(Gmail)
    And title is correct on the "Gmail" page

@google @signin
  Scenario: Go to Sign In page
    When I click "Sign in"
    Then I redirected to the "Sign in" page(Sign In)
    And title is correct on the "Sign in" page

@google @about
  Scenario: Go to How Google Search works page
    When I click "How Search works"
    Then I redirected to the "How Google Search works" page(How Google Search works)
    And title is correct on the "How Google Search works" page


@google @search
  Scenario Outline: Basic Google Search
    When I search for "<phrase>" text
    Then the results with "<phrase>" shown
    And title is correct on the "<phrase>" page

    Examples: text
    | phrase         |
    | Hello World    |
    | Test automation|


@google @googleapps
  Scenario: The user can go to Google apps
    When I click "Google apps" button
    And I click "Account" icon
    Then I can see Google "Account"
    And title is correct on the "Account" page



