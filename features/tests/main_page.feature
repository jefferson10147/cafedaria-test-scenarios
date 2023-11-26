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

    Scenario: User can click on “about” option 
        Given Open the main page
        When Click on the “about” option
        Then Verify the word “about” is in the URL
        And Verify the page has a text "A Few Words About Us"

    Scenario: User can click on “about” option and verify the FAQ option
        Given Open the main page
        When Hover over the “about” option
        And Click on the “FAQ” option
        Then Verify the word “faq” is in the URL

    Scenario: User can click on “about” option and verify the Careers option 
        Given Open the main page
        When Hover over the “about” option
        And Click on the “Careers” option
        Then Verify the word “careers” is in the URL

    Scenario: User can click on “Shop” option 
        Given Open the main page
        When Click on the “Shop” option
        Then Verify the word “catalog” is in the URL
        And Verify the shop page has a text "Catalog"

    Scenario: User can add two products to the cart
        Given Open the main page
        When Click on the “Shop” option
        And Click on the “Add to cart” button for the first 2 products
        And Click on cart icon
        Then Verify the cart has 2 products
        And Verify the word “shopping-cart” is in the URL
        And Verify checkout button is clickable

    Scenario: User can click on “Contacts” option
        Given Open the main page
        When Click on the “Contacts” option
        Then Verify the word “contacts” is in the URL
        And Verify the contacts page has a text "Get in Touch"

    Scenario: User can click on “Contacts” option and user can fill out the form
        Given Open the main page
        When Click on the “Contacts” option
        And Fill out the form on contacts page
        Then Verify "Send" button is clickable
 