from selenium.webdriver.common.by import By


class CreatePastePageLocators:
    PASTE_INPUT_FIELD = (By.XPATH, "//textarea[contains(@name, 'paste')]")
    PASTE_EXPIRATION_DDOWN = (By.CSS_SELECTOR, "span.selection [aria-labelledby*='expiration-container']")
    PASTE_EXPIRATION_DDOWN_OPTIONS = "//ul[contains(@id, 'expiration')]"
    PASTE_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Give this section a title']")
    PASTE_SYNTAX_DDOWN = (By.CSS_SELECTOR, "span.selection [aria-labelledby*='syntax']")
    PASTE_SYNTAX_DDOWN_OPTIONS = "//ul[contains(@id, 'syntax')]"
    PASTE_SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

class ReadPastePageLocators:
    PASTE_INFO_CONTAINER = (By.CSS_SELECTOR, "div [class*='section-container']")
    PASTE_SWITCH_TO_RAW_FORMAT = (By.CSS_SELECTOR, 'a.raw')
    PASTE_TEXT_AREA = (By.CSS_SELECTOR, 'textarea')
