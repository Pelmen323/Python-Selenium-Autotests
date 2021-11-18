from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
     """
    Class for Main Page\n
    Inherits init and open(self) methods\n
    Own methods: 
    - go_to_login_page - finds element by login link
    """
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
