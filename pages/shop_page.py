from selenium.webdriver.common.by import By

from pages.base_page import Page


class ShopPage(Page):
    """
        Page Object Model for the shop page
    """
    SHOP_TITLE = (By.CSS_SELECTOR, '.breadcrumbs-custom-title')

    def verify_shop_page_has_text(self, page_text):
        self.wait_for_element_appear(*self.SHOP_TITLE)
        self.verify_text(page_text, *self.SHOP_TITLE)
