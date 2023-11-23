Feature: test cases for the main page

    Scenario: User can open the main page and verify it has a map
        Given Open the main page
        When Scroll down to the footer
        Then Verify footer title is present
        And Verify footer contains a map
