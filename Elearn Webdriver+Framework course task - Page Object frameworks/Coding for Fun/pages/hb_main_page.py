from .generic_page import GenericPage
from .locators import BasePageLocators
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class HbMainPage(GenericPage):
    def __init__(self, browser: webdriver.Chrome, url: str = "https://humanbenchmark.com/", timeout=0) -> object:
        super().__init__(browser, url, timeout=timeout)

    def go_to_login_page(self):
        '''Navigates to login page'''
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def go_to_main_page(self):
        '''Navigates to login page'''
        element = self.browser.find_element(*BasePageLocators.RETURN_TO_MAIN_PAGE_LINK)
        ac = ActionChains(self.browser)
        ac.move_to_element(element).click().perform()

    def go_to_minigame(self, minigame_name: str):
        self.browser.find_element(By.XPATH, f"//h3[normalize-space()='{minigame_name}']").click()

    def verify_is_on_dashboard_page(self):
        '''- Verifies the page has dashboard link active'''
        assert self.is_element_present(*BasePageLocators.DASHBOARD_ACTIVE_LINK), "Dashboard link is active"

    def save_minigame_results(self):
        self.browser.find_element(*BasePageLocators.SAVE_RESULTS_BUTTON).click()
