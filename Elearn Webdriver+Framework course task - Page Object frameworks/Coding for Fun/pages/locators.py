from selenium.webdriver.common.by import By


class BasePageLocators:
    '''- Includes common locators'''
    LOGIN_LINK = (By.CSS_SELECTOR, ".user-nav a[href='/login']")
    RETURN_TO_MAIN_PAGE_LINK = (By.XPATH, "(//a[normalize-space()='HUMAN BENCHMARK'])[2]")
    DASHBOARD_ACTIVE_LINK = (By.CSS_SELECTOR, "a[class='current'][href='/dashboard']")
    SAVE_RESULTS_BUTTON = (By.XPATH, '//button[text()="Save score"]')


class LoginPageLocators:
    '''- Includes locators of a login/registration page'''
    INPUT_LOGIN = (By.CSS_SELECTOR, "input[name='username']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")


class NumMemoryPageLocators:
    '''- Includes locators of minigames pages'''
    START_BUTTON = (By.XPATH, '//button[text()="Start"]')
    TEXT_NUM_TO_SAVE = (By.CSS_SELECTOR, 'div[class*="big-number"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Submit"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="NEXT"]')


class ReactTimePageLocators:
    '''- Includes locators of minigames pages'''
    START_BUTTON = (By.XPATH, '//h1[text()="Reaction Time Test"]')
    TEXT_TO_CLICK = (By.XPATH, '//div[text()="Click!"]')
    NEXT_BUTTON = (By.XPATH, '//h2[text()="Click to keep going"]')


class TypingPageLocators:
    '''- Includes locators of minigames pages'''
    TEXT_SYMBOLS = (By.CSS_SELECTOR, 'span.incomplete')
    TEXT_FIELD = (By.CSS_SELECTOR, 'div.letters.notranslate')


class MemorySequencePageLocators:
    '''- Includes locators of minigames pages'''
    START_BUTTON = (By.XPATH, '//button[text()="Start"]')
    SQUARE_BUTTON = (By.CSS_SELECTOR, '.square')
    ACTIVE_BUTTON = (By.CSS_SELECTOR, 'div[class="square active"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Submit"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="NEXT"]')
