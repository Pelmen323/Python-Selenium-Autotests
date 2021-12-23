from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import PriceCalcPageLocators as locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PriceCalcPage(BasePage):
    def __init__(self, browser: webdriver.Chrome, url="https://cloud.google.com/products/calculator", timeout=0) -> object:
        super().__init__(browser=browser, url=url, timeout=timeout)

    def activate_section(self, section: str):
        self.browser.switch_to.frame(self.browser.find_element(By.CSS_SELECTOR, "article#cloud-site devsite-iframe iframe"))
        self.browser.switch_to.frame(self.browser.find_element(By.CSS_SELECTOR, "iframe#myFrame"))
        self.browser.find_element(By.XPATH, f"(//div[text()='{section}'])[1]").click()

    def select_option_from_md_dropdown(self, dropdown_selector: tuple, option_to_choose: str) -> str:  
        self.scroll_into_view(*dropdown_selector)
        self.browser.find_element(*dropdown_selector).click()
        dropdown_option = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'md-select-menu-container')][contains(@class, 'md-active md-clickable')]//div[contains(text(), '{option_to_choose}')]")))
        dropdown_option.click()

    def input_num_of_instances(self, number_of_instances: int):
        self.browser.find_element(*locator.COMPUTE_ENGINE_FORM_MACHINE_QUANTITY).send_keys(number_of_instances)

    def select_gpu(self, gpu_type: str, gpu_quantity: int):
        self.browser.find_element(*locator.COMPUTE_ENGINE_FORM_GPU_CHECKBOX).click()
        self.select_option_from_md_dropdown(locator.COMPUTE_ENGINE_FORM_GPU_MODEL, gpu_type)
        self.select_option_from_md_dropdown(locator.COMPUTE_ENGINE_FORM_GPU_QUANTITY, gpu_quantity)

    def submit_calculation(self):
        self.browser.find_element(*locator.COMPUTE_ENGINE_FORM_SUBMIT_ESTIMATE_BUTTON).click()

    def verify_item_in_estimate_section(self, locator: tuple, expected_option: str):
        estimated_option = self.browser.find_element(*locator).text.lower()
        assert expected_option.lower() in estimated_option, f"The expected and actual options in the estimate section don't match. Expected '{expected_option}', but found '{estimated_option}'"

    def email_estimate(self, email_address: str):
        self.browser.find_element(*locator.ESTIMATE_BUTTON_EMAIL).click()
        self.browser.find_element(*locator.EMAIL_FORM_EMAIL_FIELD).send_keys(email_address)
        self.scroll_into_view(*locator.EMAIL_FORM_SEND_EMAIL)
        self.browser.find_element(*locator.EMAIL_FORM_SEND_EMAIL).click()
