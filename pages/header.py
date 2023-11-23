from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    TITLE = (By.CSS_SELECTOR, '.brand')
    SUBTITLES = (By.CSS_SELECTOR, '.rd-nav-link')
    SEARCH_ICON = (By.CSS_SELECTOR, '.rd-navbar-search-toggle.toggle-original')
    CART_ICON = (By.CSS_SELECTOR, '.icon.icon-sm.mdi.mdi-cart-outline')

    def verify_title_exists_on_header(self):
        assert self.find_element(*self.TITLE), f'Title is not present'

    def verify_subtitles_on_header(self, expected_subtitles):
        subtitles = self.find_elements(*self.SUBTITLES)
        assert len(subtitles) == int(expected_subtitles), f'No subtitles found'

        for subtitle in subtitles:
            assert subtitle.is_enabled(), f'Subtitle {subtitle.text} is not clickable'

    def verify_cart_and_search_icons(self):
        assert self.find_element(*self.SEARCH_ICON), f'Search icon is not present'
        assert self.find_element(*self.CART_ICON), f'Cart icon is not present'
