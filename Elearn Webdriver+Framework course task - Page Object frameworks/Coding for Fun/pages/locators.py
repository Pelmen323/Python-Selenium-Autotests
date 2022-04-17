from selenium.webdriver.common.by import By


class BasePageLocators:
    '''- Includes common locators'''
    LOGIN_LINK = (By.CSS_SELECTOR, ".user-nav a[href='/login']")
    RETURN_TO_MAIN_PAGE_LINK = (By.XPATH, "(//a[normalize-space()='HUMAN BENCHMARK'])[2]")
    DASHBOARD_ACTIVE_LINK = (By.CSS_SELECTOR, "a[class='current'][href='/dashboard']")


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
