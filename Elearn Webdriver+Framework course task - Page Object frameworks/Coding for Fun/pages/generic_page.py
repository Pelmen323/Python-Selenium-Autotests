from .base_page import BasePage
from selenium import webdriver


class GenericPage(BasePage):
    def __init__(self, browser: webdriver.Chrome, url: str, timeout=0) -> object:
        super().__init__(browser, url, timeout=timeout)
