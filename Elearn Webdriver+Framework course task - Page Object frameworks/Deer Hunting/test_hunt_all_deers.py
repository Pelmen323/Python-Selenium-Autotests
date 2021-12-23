from pages.hunt_deers_page import HuntDeersPage
from selenium.webdriver.common.by import By
import time


class TestHuntDeers:
    LINK = "https://interacty.me/projects/ccff51c3495df0ae"

    def test_hunt_deers(self, browser):
        page = HuntDeersPage(browser=browser, url=TestHuntDeers.LINK, timeout=5)
        page.open()
        page.browser.switch_to.frame(page.browser.find_element(By.CSS_SELECTOR, "iframe#remix-iframe"))
        page.browser.find_element(By.CSS_SELECTOR, "input.registration__form-input").send_keys("Pelmen323")
        page.browser.find_element(By.CSS_SELECTOR, "button[type='button']").click()
        time.sleep(2)
        deers = page.browser.find_elements(By.CSS_SELECTOR, "div.z_pin.hid")
        for deer in deers:
            deer.click()
            page.browser.find_element(By.CSS_SELECTOR, "div.modal__content-close-icon").click()
        time.sleep(25)
