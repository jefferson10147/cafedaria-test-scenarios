from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    """
        Page Object Model for the main page
    """

    MAIN_URL = 'https://cafedaria.com/'
    FOOTER = (
        By.CSS_SELECTOR, 
        '.page-footer.page-footer-corporate.section-lg.section-lg--inset-bottom-60.bg-gray-dark.text-left.context-dark'
    )
    FOOTER_TITLE = (By.CSS_SELECTOR, 'footer a.brand')
    MAP = (By.CSS_SELECTOR, '.google-map')

    def open_main_page(self):
        self.open_url(self.MAIN_URL)

    def scroll_down_to_the_footer(self):
        self.scroll_down_to_the_element(*self.FOOTER)

    def verify_footer_title_is_present(self):
        assert self.find_element(*self.FOOTER_TITLE), f'Footer title is not present'

    def verify_footer_contains_a_map(self):
        assert self.find_element(*self.MAP), f'Footer does not contain a map'

    def verify_url_query(self, url_query):
        self.verify_partial_url(url_query)
        assert url_query in self.driver.current_url, f'URL query {url_query} is not in the URL'
