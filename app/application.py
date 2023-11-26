from pages.main_page import MainPage
from pages.header import Header
from pages.about_page import AboutPage
from pages.shop_page import ShopPage
from pages.cart_page import CartPage


class Application:
    """
        Class for storing the driver and page objects
    """

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.about_page = AboutPage(self.driver)
        self.shop_page = ShopPage(self.driver)
        self.cart_page = CartPage(self.driver)
