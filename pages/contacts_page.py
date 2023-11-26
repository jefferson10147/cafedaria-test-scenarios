from selenium.webdriver.common.by import By

from pages.base_page import Page


class ContactsPage(Page):
    """ 
        Page Object Model for the contact page
    """
    CONTACTS_TITLE = (By.CSS_SELECTOR, '.col-sm-12.section-mailform-wrap-25 h3')

    def verify_contacts_page_has_text(self, page_text):
        self.wait_for_element_appear(*self.CONTACTS_TITLE)
        self.verify_text(page_text, *self.CONTACTS_TITLE)