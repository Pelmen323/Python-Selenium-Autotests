from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "a[class='btn btn-default'][href*='/basket']")
    CURRENT_LANGUAGE_DDOWN_OPTION = (By.CSS_SELECTOR, "select[name='language'] [selected]")

# class MainPageLocators:
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, "div.product_main .price_color")
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, "div#messages div:nth-child(1) strong")
    PRODUCT_COST_ALERT = (By.CSS_SELECTOR, "div#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div:nth-child(1)")

class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")