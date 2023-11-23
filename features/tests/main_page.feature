Feature: test cases for the main page

    Scenario: User can open the main page and verify it has a map
        Given Open the main page
        When Scroll down to the footer
        Then Verify footer title is present
        And Verify footer contains a map

    Scenario: User can see and click on the elements in the navigation bar
        Given Open the main page
        When Verify the title Cafedaria exists on the navigation bar
        And Verify there are 6 sub-titles in the navigation bar are clickable
        Then Verify the cart and search icons exists
