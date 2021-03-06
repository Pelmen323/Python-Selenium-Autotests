from selenium.webdriver.common.by import By


class BasePageLocators:
    '''- Includes common locators'''
    LOGIN_LINK = (By.CSS_SELECTOR, ".user-nav a[href='/login']")
    RETURN_TO_MAIN_PAGE_LINK = (By.XPATH, "(//a[normalize-space()='HUMAN BENCHMARK'])[2]")
    DASHBOARD_ACTIVE_LINK = (By.CSS_SELECTOR, "a[class='current'][href='/dashboard']")
    SAVE_RESULTS_BUTTON = (By.XPATH, '//button[text()="Save score"]')
    CLICK_ANYWHERE_ELEMENT = (By.XPATH, '//*[text()="Click anywhere to start."]')

    START_BUTTON = (By.XPATH, '//button[text()="Start"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Submit"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="NEXT"]')
    CONTINUE_BUTTON = (By.XPATH, '//button[text()="Continue"]')


class LoginPageLocators(BasePageLocators):
    '''- Includes locators of a login/registration page'''
    INPUT_LOGIN = (By.CSS_SELECTOR, "input[name='username']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")


class HumanAimPageLocators(BasePageLocators):
    '''- Includes locators of minigames pages'''
    TARGET_TO_CLICK = (By.CSS_SELECTOR, 'div[data-aim-target=true] div[class="css-z6vxiy e6yfngs3"]')

class NumMemoryPageLocators(BasePageLocators):
    '''- Includes locators of minigames pages'''
    TEXT_NUM_TO_SAVE = (By.CSS_SELECTOR, 'div[class*="big-number"]')


class ReactTimePageLocators(BasePageLocators):
    '''- Includes locators of minigames pages'''
    START_BUTTON = (By.XPATH, '//h1[text()="Reaction Time Test"]')
    TEXT_TO_CLICK = (By.XPATH, '//div[text()="Click!"]')
    NEXT_BUTTON = (By.XPATH, '//h2[text()="Click to keep going"]')


class TypingPageLocators(BasePageLocators):
    '''- Includes locators of minigames pages'''
    TEXT_SYMBOLS = (By.CSS_SELECTOR, 'span.incomplete')
    TEXT_FIELD = (By.CSS_SELECTOR, 'div.letters.notranslate')


class MemorySequencePageLocators(BasePageLocators):
    '''- Includes locators of minigames pages'''
    SQUARE_BUTTON = (By.CSS_SELECTOR, '.square')
    ACTIVE_BUTTON = (By.CSS_SELECTOR, 'div[class="square active"]')


class VisualMemoryPageLocators(BasePageLocators):
    '''- Includes locators of minigames pages'''
    ACTIVE_BUTTON = (By.CSS_SELECTOR, '.memory-test .active')
    CONTINUE_BUTTON = (By.XPATH, '//button[text()="Continue"]')


class ChimpTestPageLocators(BasePageLocators):
    '''- Includes locators of minigames pages'''
    START_BUTTON = (By.XPATH, '//button[text()="Start Test"]')
    ACTIVE_BUTTON = (By.CSS_SELECTOR, 'div[data-cellnumber]')


class VerbalMemoryPageLocators(BasePageLocators):
    '''- Includes locators of minigames pages'''
    WORD_LOCATOR = (By.CSS_SELECTOR, 'div.word')
    SEEN_BUTTON = (By.XPATH, '//button[text()="SEEN"]')
    NEW_BUTTON = (By.XPATH, '//button[text()="NEW"]')
