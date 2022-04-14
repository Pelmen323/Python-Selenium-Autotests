from pages.generic_page import GenericPage
from selenium.webdriver.common.by import By
import time
import random


class TestHuntDeers:
    LINK = "https://interacty.me/projects/ccff51c3495df0ae"
    USER_NICKNAME = f'Pelmen323_{random.randint(1,100)}'

    def test_hunt_deers(self, browser):
        page = GenericPage(browser=browser, url=TestHuntDeers.LINK, timeout=5)
        page.open()
        # Input user nickname
        page.browser.switch_to.frame(page.browser.find_element(By.CSS_SELECTOR, "iframe#remix-iframe"))
        page.browser.find_element(By.CSS_SELECTOR, "input.registration__form-input").send_keys(TestHuntDeers.USER_NICKNAME)
        page.browser.find_element(By.CSS_SELECTOR, "button[type='button']").click()
        time.sleep(2)
        # The game starts here
        deers = page.browser.find_elements(By.CSS_SELECTOR, "div.z_pin.hid")
        for deer in deers:
            deer.click()
            page.browser.find_element(By.CSS_SELECTOR, "div.modal__content-close-icon").click()

        # For results verification
        time.sleep(15)
