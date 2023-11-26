from selenium.webdriver.common.by import By

from pages.base_page import Page


class AboutPage(Page):
    """
        Page Object Model for the about page
    """
    ABOUT_PAGE_TITLE = (
        By.CSS_SELECTOR,
        '.section-fullwidth-body-inner.section-fullwidth-body-offset-top.section-lg h3')

    def verify_about_page_has_text(self, page_text):
        self.wait_for_element_appear(*self.ABOUT_PAGE_TITLE)
        self.verify_text(page_text, *self.ABOUT_PAGE_TITLE)
