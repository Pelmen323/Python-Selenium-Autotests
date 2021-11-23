from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    '''
    Class for shop pages with goods. Example - a book page where item can be viewed and added to cart
    '''
    def add_item_to_cart(self):
        '''- Adds item on the product page to the basket'''
        add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_cart.click()

    def should_be_the_same_product_in_alert(self, product_name: str):
        '''- Verifies that passed product name is in alert message "ProductName added to the cart"'''
        alert_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        assert product_name == alert_text, "Product name should be present in the alert"

    def should_be_the_price_in_cart(self, product_cost: str):
        '''- Verifies that passed product price is in alert message "Cart cost is xx$ now"'''
        alert_text = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_ALERT).text
        assert product_cost == alert_text, "Product cost should be present in the alert"

    def should_not_be_success_message(self):
        '''- Verifies the success message is not presented (Something successfully added to your cart)'''
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        '''- Verifies the success message (Something successfully added to your cart) disappears in x seconds'''
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should dissapear, but it still exists"

    def store_item_name(self) -> str:
        '''- Returns the name of the product on the product page'''
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def store_product_cost(self) -> str:
        '''- Returns the price of the product on the product page'''
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
