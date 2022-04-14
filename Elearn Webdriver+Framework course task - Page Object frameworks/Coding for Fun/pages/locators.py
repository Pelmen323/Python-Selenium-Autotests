from selenium.webdriver.common.by import By


class BasePageLocators:
    '''- Includes common locators'''
    LOGIN_LINK = (By.CSS_SELECTOR, ".user-nav a[href='/login']")
    RETURN_TO_MAIN_PAGE_LINK = (By.XPATH, "(//a[normalize-space()='HUMAN BENCHMARK'])[2]")
    TILE_AIM_MINIGAME = (By.XPATH, "//h3[normalize-space()='Aim Trainer']")
    DASHBOARD_ACTIVE_LINK = (By.CSS_SELECTOR, "a[class='current'][href='/dashboard']")


class LoginPageLocators:
    '''- Includes locators of a login/registration page'''
    INPUT_LOGIN = (By.CSS_SELECTOR, "input[name='username']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")
