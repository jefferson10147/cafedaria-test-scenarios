from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Page:
    """
        Base class for all pages
    """

    def __init__(self, driver):
        """
            Constructor for the Page object
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(5)
        self.actions = ActionChains(self.driver)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        """
            Clicks on the element
        """
        self.driver.find_element(*locator).click()

    def refresh(self):
        """
            Refreshes the current page
        """
        self.driver.refresh()

    def find_element(self, *locator):
        """
            Finds the element on the page
        """
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        """
            Finds the elements on the page
        """
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        """
            Inputs text into the element
        """
        e = self.driver.find_element(*locator)
        e.send_keys(text)

    def wait_for_element_clickable(self, *locator):
        """
            Waits for the element to be clickable
        """
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable: {locator}'
        )

    def wait_for_element_to_be_clickable_and_click(self, *locator):
        """
            Waits for the element to be clickable and clicks on it
        """
        e = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable: {locator}'
        )
        e.click()

    def wait_for_element_disappear(self, *locator):
        """
            Waits for the element to disappear
        """
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element did not disappear: {locator}'
        )

    def verify_text(self, expected_text, *locator):
        """
            Verifies the text of the element
        """
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        """
            Verifies the partial text of the element
        """
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Error, expected partial text {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_part_of_url):
        """
            Verifies the partial url of the page
        """
        self.wait.until(EC.url_contains(expected_part_of_url))
