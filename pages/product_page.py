from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """
    Class for Product Page\n
    Inherits init and open(self) methods\n
    Own methods:
    - add_to_cart - adds product to the cart
    """
    def store_item_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def store_product_cost(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text

    def add_item_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_cart.click()

    def should_be_the_same_product_in_alert(self, product_name):
        alert_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        assert product_name == alert_text, "Product name should be present in the alert"

    def should_be_the_price_in_cart(self, product_cost):
        alert_text = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_ALERT).text
        assert product_cost == alert_text, "Product cost should be present in the alert"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message should dissapear, but it still exists"
