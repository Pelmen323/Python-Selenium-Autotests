from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait         # Explicit wait for verification
from selenium.webdriver.support import expected_conditions as EC   # Explicit wait condition
import math
from .locators import BasePageLocators

class BasePage:
    """
    Class for initializing Page object\n
    Receives browser and url during initialization\n
    Has in-built method open(self)
    """
    def __init__(self, browser: object, url: str, timeout: int = 10) -> object:
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not found"

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator_type, locator):
        try:
            self.browser.find_element(locator_type, locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator_type, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((locator_type, locator)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator_type, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((locator_type, locator)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")