from pages.base_page import Page


class MainPage(Page):
    """
        Page Object Model for the main page
    """

    MAIN_URL = 'https://cafedaria.com/'

    def open_main_page(self):
        self.open_url(self.MAIN_URL)
