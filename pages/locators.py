from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, "div.product_main .price_color")
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, "div#messages div:nth-child(1) strong")
    PRODUCT_COST_ALERT = (By.CSS_SELECTOR, "div#messages div:nth-child(3) strong")