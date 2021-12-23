from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import CreatePastePageLocators


class CreatePastePage(BasePage):
    def add_text_to_paste(self, text: str):
        self.browser.find_element(*CreatePastePageLocators.PASTE_INPUT_FIELD).send_keys(text)

    def select_paste_expiration_time(self, expiration_time: str):
        self.browser.find_element(*CreatePastePageLocators.PASTE_EXPIRATION_DDOWN).click()
        self.browser.find_element(By.XPATH, f"{CreatePastePageLocators.PASTE_EXPIRATION_DDOWN_OPTIONS}/li[text()='{expiration_time}']").click()

    def add_title_to_paste(self, title: str):
        self.browser.find_element(*CreatePastePageLocators.PASTE_NAME_INPUT).send_keys(title)

    def select_syntax_highlighting(self, syntax: str):
        self.browser.find_element(*CreatePastePageLocators.PASTE_SYNTAX_DDOWN).click()
        self.browser.find_element(By.XPATH, f"{CreatePastePageLocators.PASTE_SYNTAX_DDOWN_OPTIONS}/li[text()='{syntax}']").click()

    def submit_new_paste(self):
        self.browser.find_element(*CreatePastePageLocators.PASTE_SUBMIT_BUTTON).click()
