from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    '''
    Class for the login/registration page
    '''
    def register_new_user(self, email: str, password: str):
        '''- Registers a new user. Input - email and password, both string'''
        self.browser.find_element(*LoginPageLocators.REGISTRATION_LOGIN_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_RPT_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON).click()

    def should_be_login_page(self):
        '''- Verifies the page has login page url, login form and registration form'''
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        '''- Verifies the page has login page url'''
        assert "login" in self.browser.current_url, "There should be 'login' string in page URL"

    def should_be_login_form(self):
        '''- Verifies the page has login form'''
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form should be present on the page"

    def should_be_register_form(self):
        '''- Verifies the page has registration form'''
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form should be present on the page"
