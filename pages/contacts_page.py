from selenium.webdriver.common.by import By

from pages.base_page import Page


class ContactsPage(Page):
    """ 
        Page Object Model for the contact page
    """
    CONTACTS_TITLE = (By.CSS_SELECTOR, '.col-sm-12.section-mailform-wrap-25 h3')
    CONTACTS_NAME_FIELD = (By.ID, 'contacts-name')
    CONTACTS_LASTNAME_FIELD = (By.ID, 'contacts-last-name')
    CONTACTS_EMAIL_FIELD = (By.ID, 'contacts-email')
    CONTACTS_PHONE_FIELD = (By.ID, 'contacts-phone')
    CONTACTS_MESSAGE_FIELD = (By.ID, 'contacts-message')
    SEND_BTN = (By.CSS_SELECTOR, '.button.button-primary.js-contact-submit')

    def verify_contacts_page_has_text(self, page_text):
        self.wait_for_element_appear(*self.CONTACTS_TITLE)
        self.verify_text(page_text, *self.CONTACTS_TITLE)

    def fill_out_form(self):
        test_data = {
            'name': 'John',
            'last_name': 'Smith',
            'email': 'john@example',
            'phone': '1234567890',
            'message': 'Hello World'
        }

        self.wait_for_element_appear(*self.CONTACTS_TITLE)
        self.input_text(test_data['name'], *self.CONTACTS_NAME_FIELD)
        self.input_text(test_data['last_name'], *self.CONTACTS_LASTNAME_FIELD)
        self.input_text(test_data['email'], *self.CONTACTS_EMAIL_FIELD)
        self.input_text(test_data['phone'], *self.CONTACTS_PHONE_FIELD)
        self.input_text(test_data['message'], *self.CONTACTS_MESSAGE_FIELD)

    def verify_send_button_is_enabled(self):
        send_btn = self.find_element(*self.SEND_BTN)
        assert send_btn.is_enabled(), 'Send button is not enabled'
