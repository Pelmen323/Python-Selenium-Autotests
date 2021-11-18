from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """
    Class for initializing Page object\n
    Receives browser and url during initialization\n
    Has in-built method open(self)
    """
    def __init__(self, browser: object, url: str, timeout: int = 10) -> object:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator_type, selector):
        try:
            self.browser.find_element(locator_type, selector)
        except NoSuchElementException:
            return False
        return True
