from .generic_page import GenericPage
from .hb_main_page import HbMainPage
from .locators import LoginPageLocators


class HbLoginPage(HbMainPage):
    def login(self, login: str, password: str):
        '''- Registers a new user. Input - email and password, both string'''
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(login)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT).click()


