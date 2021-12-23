from .base_page import BasePage
from selenium import webdriver
from .locators import EmailPageLocators as locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EmailPage(BasePage):
    def __init__(self, browser: webdriver.Chrome, url="https://yopmail.com/en/", timeout=0) -> object:
        super().__init__(browser=browser, url=url, timeout=timeout)

    def open_new_email_inbox(self):
        self.browser.find_element(*locator.GET_RANDOM_EMAIL_LINK).click()
        self.browser.find_element(*locator.CHECK_INBOX_BUTTON).click()

    def get_email_address(self):
        return self.browser.find_element(*locator.CURRENT_EMAIL_LABEL).text

    def wait_for_email(self):
        for i in range(5):
            self.browser.find_element(*locator.REFRESH_EMAIL_INBOX_BUTTON).click()
            print(self.is_element_present(*locator.EMAIL_ELEMENT_TO_INDICATE_NEW_EMAIL))
            if self.is_element_present(*locator.EMAIL_INBOX_IFRAME):
                self.browser.switch_to.frame(self.browser.find_element(*locator.EMAIL_INBOX_IFRAME))
                if self.is_element_present(*locator.EMAIL_ELEMENT_TO_INDICATE_NEW_EMAIL):
                    self.browser.switch_to.default_content()
                    break
                else:
                    self.browser.switch_to.default_content()
            time.sleep(3)

    def verify_emailed_monthly_costs(self, expected_monthly_cost: str):
        self.browser.switch_to.frame(self.browser.find_element(*locator.EMAIL_PAGE_BODY_IFRAME))
        email_monthly_cost = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator.EMAIL_ESTIMATED_MONTHLY_COST_LABEL)).text
        assert expected_monthly_cost in email_monthly_cost, f"The expected monthly cost and emailed monthly cost don't match. Expected '{expected_monthly_cost}', but found '{email_monthly_cost}'"
