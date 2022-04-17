from .hb_main_page import HbMainPage
from .locators import NumMemoryPageLocators, ReactTimePageLocators, TypingPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HbMinigamesPage(HbMainPage):
    def fill_number_memory_number(self, number_to_insert: str):
        '''Navigates to login page'''
        WebDriverWait(self.browser, 45).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'input')))
        input_field = self.browser.find_element(By.CSS_SELECTOR, 'input')
        ac = ActionChains(self.browser)
        ac.move_to_element(input_field).send_keys(number_to_insert).perform()
        self.browser.find_element(*NumMemoryPageLocators.SUBMIT_BUTTON).click()

    def perform_reaction_time_action(self):
        element = WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(ReactTimePageLocators.TEXT_TO_CLICK))
        element.click()

    def perform_typing_time_test(self):
        list_with_elements = self.browser.find_elements(*TypingPageLocators.TEXT_SYMBOLS)
        text_to_insert = ''.join([i.text if i.text != "" else " " for i in list_with_elements])
        self.browser.find_element(*TypingPageLocators.TEXT_FIELD).send_keys(text_to_insert)
