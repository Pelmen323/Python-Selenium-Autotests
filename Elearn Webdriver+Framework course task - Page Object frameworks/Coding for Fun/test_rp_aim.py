from pages.hb_main_page import HbMainPage
from pages.hb_login_page import HbLoginPage
from pages.hb_minigames_page import HbMinigamesPage
from pages.locators import NumMemoryPageLocators, ReactTimePageLocators, BasePageLocators, MemorySequencePageLocators
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

            page.save_minigame_results()

            time.sleep(5)

    @pytest.mark.skip()
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

            # Intentional fail to finish the game
            page.fill_number_memory_number(number_to_insert="123")
            page.save_minigame_results()

            time.sleep(5)

    @pytest.mark.skip()
    def test_reaction_time(self, browser):
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
            page.go_to_minigame(minigame_name="Reaction Time")

            # Start the minigame
            element = page.browser.find_element(*ReactTimePageLocators.START_BUTTON)
            ac = ActionChains(browser)
            ac.move_to_element(element).click().perform()
            # Complete the minigame for some time
            for i in range(4):
                page.perform_reaction_time_action()
                page.browser.find_element(*ReactTimePageLocators.NEXT_BUTTON).click()

            # Final click - moved here to not click on next button
            page.perform_reaction_time_action()
            page.save_minigame_results()

            time.sleep(5)

    @pytest.mark.skip()
    def test_typing_time(self, browser):
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
            page.go_to_minigame(minigame_name="Typing")

            # Start the minigame
            page.perform_typing_time_test()
            page.save_minigame_results()

            time.sleep(5)

    def test_sequence_memory(self, browser):
        rounds_to_play = 30
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
            page.go_to_minigame(minigame_name="Sequence Memory")

            # Start the minigame
            element = page.browser.find_element(*MemorySequencePageLocators.START_BUTTON)
            ac = ActionChains(browser)
            ac.move_to_element(element).click().perform()
            # Complete the minigame for some time
            num_of_elements_to_save = 1
            for level in range(rounds_to_play):
                active_buttons_list = []
                for i in range(num_of_elements_to_save):
                    active_element = WebDriverWait(page.browser, 10).until(EC.visibility_of_element_located(MemorySequencePageLocators.ACTIVE_BUTTON))
                    active_buttons_list.append(active_element)
                    while "active" in active_element.get_attribute("class"):
                        time.sleep(0.2)

                if num_of_elements_to_save < rounds_to_play:
                    for item in active_buttons_list:
                        item.click()

                else:
                    active_buttons_list[1].click()
                    break

                num_of_elements_to_save += 1

            # Final click - moved here to not click on next button
            page.save_minigame_results()

            time.sleep(5)
            
