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


@when('Click on the “about” option')
def click_about_option(context):
    context.app.header.click_about_option()


@when('Hover over the “about” option')
def hover_over_option(context):
    context.app.header.hover_over_about_option()


@when('Click on the “FAQ” option')
def click_option(context):
    context.app.header.click_faq_option()


@when('Click on the “Careers” option')
def click_option(context):
    context.app.header.click_careers_option()


@when('Click on the “Shop” option')
def click_option(context):
    context.app.header.click_shop_option()


@when('Click on the “Add to cart” button for the first {number_of_products} products')
def click_add_to_cart_button(context, number_of_products):
    context.app.shop_page.click_add_to_cart_button(number_of_products)


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@then('Verify footer title is present')
def verify_footer_title_is_present(context):
    context.app.main_page.verify_footer_title_is_present()


@then('Verify footer contains a map')
def verify_footer_contains_a_map(context):
    context.app.main_page.verify_footer_contains_a_map()


@then('Verify the cart and search icons exists')
def verify_icons(context):
    context.app.header.verify_cart_and_search_icons()


@then('Verify the word “{url_query}” is in the URL')
def verify_url_query(context, url_query):
    context.app.main_page.verify_url_query(url_query)


@then('Verify the page has a text "{page_text}"')
def verify_page_has_text(context, page_text):
    context.app.about_page.verify_about_page_has_text(page_text)


@then('Verify the shop page has a text "{page_text}"')
def verify_page_has_text(context, page_text):
    context.app.shop_page.verify_shop_page_has_text(page_text)


@then('Verify the cart has {number_of_products} products')
def verify_cart_has_two_products(context, number_of_products):
    context.app.cart_page.verify_cart_has_two_products(number_of_products)


@then('Verify checkout button is clickable')
def verify_checkout_button_is_enabled(context):
    context.app.cart_page.verify_checkout_button_is_enabled()
