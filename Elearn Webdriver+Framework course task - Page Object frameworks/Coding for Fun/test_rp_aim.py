from pages.hb_main_page import HbMainPage
from pages.hb_login_page import HbLoginPage
from pages.hb_minigames_page import HbMinigamesPage
from pages.locators import NumMemoryPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestHumanBenchmark:
    login = "Pelmen323"
    password = "17071997"

    @pytest.mark.skip()
    def test_human_aim(self, browser):
        locator_target = 'div[data-aim-target=true] div[class="css-z6vxiy e6yfngs3"]'

        page = HbMainPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(10):
            login_page.go_to_main_page()
            # Navigate to minigame
            page.go_to_minigame(minigame_name="Aim Trainer")

            # Start the minigame
            element = page.browser.find_element(By.CSS_SELECTOR, locator_target)
            ac = ActionChains(browser)
            ac.move_to_element(element).click().perform()
            # Perform clicks for each of 30 targets
            for i in range(30):
                element = page.browser.find_element(By.CSS_SELECTOR, locator_target)
                ac = ActionChains(browser)
                ac.move_to_element(element).click().perform()

            # Save results
            page.browser.find_element(By.XPATH, '//button[text()="Save score"]').click()

            time.sleep(5)

    def test_number_memory(self, browser):
        page = HbMinigamesPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(1):
            login_page.go_to_main_page()
            # Navigate to minigame
            page.go_to_minigame(minigame_name="Number Memory")

            # Start the minigame
            element = page.browser.find_element(*NumMemoryPageLocators.START_BUTTON)
            ac = ActionChains(browser)
            ac.move_to_element(element).click().perform()
            # Complete the minigame for some time
            for i in range(30):
                number_to_store = page.browser.find_element(*NumMemoryPageLocators.TEXT_NUM_TO_SAVE).text
                page.fill_number_memory_number(number_to_insert=number_to_store)
                page.browser.find_element(*NumMemoryPageLocators.NEXT_BUTTON).click()

            page.fill_number_memory_number(number_to_insert="123")
            time.sleep(30)
            # Save results
            page.browser.find_element(By.XPATH, '//button[text()="Save score"]').click()

            time.sleep(5)
