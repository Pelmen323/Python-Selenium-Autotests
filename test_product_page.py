from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser=browser, url=link)
    page.open()
    product_name = page.store_item_name()
    product_cost = page.store_product_cost()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_the_same_product_in_alert(product_name)
    page.should_be_the_price_in_cart(product_cost)
