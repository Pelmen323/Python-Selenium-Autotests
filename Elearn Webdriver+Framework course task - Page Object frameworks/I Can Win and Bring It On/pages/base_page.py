from selenium import webdriver


class BasePage:
    def __init__(self, browser: webdriver.Chrome, url: str, timeout=0) -> object:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        '''- Opens the URL of the page object'''
        self.browser.get(self.url)
