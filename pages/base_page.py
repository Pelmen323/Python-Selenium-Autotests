from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators


class BasePage:
    '''
    Initial class that is inherited by all other Page classes
    '''
    def __init__(self, browser: object, url: str, timeout: int = 3) -> object:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        '''- Navigates to a login page by clicking a link in the header'''
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def go_to_basket_page(self):
        '''- Navigates to a basket page by clicking a link in the header'''
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

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

    def is_not_element_present(self, locator_type, locator: str, timeout: int = 4) -> bool:
        '''Verifies if element is NOT present on the page during timeout period\n
        Example:
        - Input - locator_type=By.CSS_SELECTOR, locator="form#login_form, timeout (optional, default - 4s)"
        - Output - True if element is not present otherwise False
        '''
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((locator_type, locator)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator_type, locator: str, timeout: int = 4) -> bool:
        '''Verifies if element DISAPPEARED during timeout period\n
        Example:
        - Input - locator_type=By.CSS_SELECTOR, locator="form#login_form, timeout (optional, default - 4s)"
        - Output - True if element disappeared otherwise False
        '''
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((locator_type, locator)))
        except TimeoutException:
            return False
        return True

    def open(self):
        '''- Opens the URL of the page object'''
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        '''- Verifies if the current user is authorized based on user icon'''
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorized user"

    def should_be_login_link(self):
        '''- Verifies the login link is present on the page'''
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not found"

    def solve_quiz_and_get_code(self):
        '''- Solves the popup quiz and inputs the code on the second alert'''
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
