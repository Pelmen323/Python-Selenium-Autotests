from .hb_main_page import HbMainPage
from .locators import NumMemoryPageLocators
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
