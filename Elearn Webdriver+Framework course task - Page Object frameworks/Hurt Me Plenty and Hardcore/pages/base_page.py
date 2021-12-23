from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    '''
    Initial class that is inherited by all other Page classes
    '''

    def __init__(self, browser: webdriver.Chrome, url: str, timeout=0) -> object:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        '''- Opens the URL of the page object'''
        self.browser.get(self.url)

    def is_element_present(self, locator_type, locator: str) -> bool:
        '''Verifies if element is present on the page\n
        Example:
        - Input - locator_type=By.CSS_SELECTOR, locator="form#login_form"
        - Output - True if element is present otherwise False
        '''
        try:
            self.browser.find_element(locator_type, locator)
        except NoSuchElementException:
            return False
        return True

    def scroll_into_view(self, locator_type, locator: str):
        try:
            element = self.browser.find_element(locator_type, locator)
        except NoSuchElementException:
            pass
        self.browser.execute_script('arguments[0].scrollIntoView({block: "center"})', element)
