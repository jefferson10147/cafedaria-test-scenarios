from behave import given, when, then


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Scroll down to the footer')
def scroll_down_to_the_footer(context):
    context.app.main_page.scroll_down_to_the_footer()


@then('Verify footer title is present')
def verify_footer_title_is_present(context):
    context.app.main_page.verify_footer_title_is_present()


@then('Verify footer contains a map')
def verify_footer_contains_a_map(context):
    context.app.main_page.verify_footer_contains_a_map()
