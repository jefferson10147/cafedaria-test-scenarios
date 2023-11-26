from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    """ 
        Page Object Model for the cart page
    """
    CART_COUNT = (By.CSS_SELECTOR, '.js-cart-items-counter')
    CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.button.button-sm.button-primary')

    def verify_cart_has_two_products(self, number_of_products):
        self.wait_for_element_appear(*self.CART_COUNT)
        cart_count = self.find_element(*self.CART_COUNT)
        assert number_of_products in cart_count.text, f'Cart count is not {number_of_products}'

    def verify_checkout_button_is_enabled(self):
        self.wait_for_element_appear(*self.CHECKOUT_BTN)
        checkout_btn = self.find_element(*self.CHECKOUT_BTN)
        assert checkout_btn.is_enabled(), f'Checkout button is not enabled'
