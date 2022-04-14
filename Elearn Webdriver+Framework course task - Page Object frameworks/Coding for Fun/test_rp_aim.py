from pages.generic_page import GenericPage
from pages.hb_main_page import HbMainPage
from pages.hb_login_page import HbLoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestHumanBenchmark:
    login = "Pelmen323"
    password = "17071997"

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
            page.go_to_minigame(minigame_name="Aim")

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
