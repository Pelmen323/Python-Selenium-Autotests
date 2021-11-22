from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), f"The shopping cart should be empty, but there are items in the page with locator {BasketPageLocators.BASKET_ITEM}"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), f"The message about empty cart should appear"

    def empty_basket_message_should_include_text(self):
        page_text = self.browser.find_element(*BasketPageLocators.EMPTY_CART_MESSAGE).text
        current_locale = self.browser.find_element(*BasePageLocators.CURRENT_LANGUAGE_DDOWN_OPTION).get_attribute("value")
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en-gb": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }
        message_text = languages[current_locale]
        assert message_text in page_text, f"The message about empty cart should contain valid text {message_text}, actual - {page_text}"
