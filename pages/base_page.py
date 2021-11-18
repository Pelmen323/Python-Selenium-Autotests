class BasePage:
    """
    Class for initializing Page object\n
    Receives browser and url during initialization\n
    Has in-built method open(self)
    """
    def __init__(self, browser: object, url: str) -> None:
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
