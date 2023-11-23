from behave import given, when, then


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Scroll down to the footer')
def scroll_down_to_the_footer(context):
    context.app.main_page.scroll_down_to_the_footer()


@when('Verify the title Cafedaria exists on the navigation bar')
def verify_navigation_bar(context):
    context.app.header.verify_title_exists_on_header()


@when('Verify there are {expected_subtitles} sub-titles in the navigation bar are clickable')
def verify_navigation_bar(context, expected_subtitles):
    context.app.header.verify_subtitles_on_header(expected_subtitles)


@then('Verify footer title is present')
def verify_footer_title_is_present(context):
    context.app.main_page.verify_footer_title_is_present()


@then('Verify footer contains a map')
def verify_footer_contains_a_map(context):
    context.app.main_page.verify_footer_contains_a_map()


@then('Verify the cart and search icons exists')
def verify_icons(context):
    context.app.header.verify_cart_and_search_icons()