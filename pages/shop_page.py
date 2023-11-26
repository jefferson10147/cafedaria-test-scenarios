from selenium.webdriver.common.by import By

from pages.base_page import Page


class ShopPage(Page):
    """
        Page Object Model for the shop page
    """
    SHOP_TITLE = (By.CSS_SELECTOR, '.breadcrumbs-custom-title')
    ADD_TO_CART_BTN = (
        By.CSS_SELECTOR,
        '.button.button-sm.button-primary.button-icon.button-icon-left.js-add-to-cart')

    def verify_shop_page_has_text(self, page_text):
        self.wait_for_element_appear(*self.SHOP_TITLE)
        self.verify_text(page_text, *self.SHOP_TITLE)

    def click_add_to_cart_button(self, number_of_products):
        self.wait_for_element_clickable(*self.ADD_TO_CART_BTN)
        add_to_cart_buttons = self.find_elements(*self.ADD_TO_CART_BTN)
        for i in range(int(number_of_products)):
            add_to_cart_buttons[i].click()
