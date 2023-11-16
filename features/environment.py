from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application


def browser_init(context):
    """
        This function will run before each scenario.
        It will start the browser and open the application.
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    """ 
        This function will run before each scenario.
    """
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    """
        This function will run before each step.
    """
    print('\nStarted step: ', step)


def after_step(context, step):
    """
        This function will run after each step.
    """
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    """
        This function will run after each scenario.
        It will close the browser.
    """
    context.driver.delete_all_cookies()
    context.driver.quit()