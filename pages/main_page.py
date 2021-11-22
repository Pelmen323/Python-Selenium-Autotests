from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """
    Class for Main Page\n
    Inherits init and open(self) methods\n
    Own methods:
    - go_to_login_page - finds element by login link
    """
    def __init__(self, *args, **kwargs) -> object:
        super(MainPage, self).__init__(*args, **kwargs)
