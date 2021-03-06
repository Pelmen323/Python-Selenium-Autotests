from pages.hb_main_page import HbMainPage
from pages.hb_login_page import HbLoginPage
from pages.hb_minigames_page import HbMinigamesPage
from pages.locators import HumanAimPageLocators, NumMemoryPageLocators, ReactTimePageLocators, MemorySequencePageLocators, VisualMemoryPageLocators, ChimpTestPageLocators, VerbalMemoryPageLocators, BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class TestHumanBenchmark:
    login = "Pelmen323"
    password = "17071997"

    @pytest.mark.human_aim
    def test_human_aim(self, browser, num_of_games_played: int):
        rounds_to_play = 30
        page = HbMainPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(num_of_games_played):
            login_page.go_to_main_page()
            page.go_to_minigame(minigame_name="Aim Trainer")
            page.start_minigame(HumanAimPageLocators.TARGET_TO_CLICK)

            # Perform clicks for each of 30 targets. AC is used since usual clicks not working here
            for i in range(rounds_to_play):
                element = page.browser.find_element(*HumanAimPageLocators.TARGET_TO_CLICK)
                ac = ActionChains(browser)
                ac.move_to_element(element).click().perform()

            page.save_minigame_results()

            time.sleep(5)

    @pytest.mark.number_memory
    def test_number_memory(self, browser, num_of_games_played: int):
        rounds_to_play = 30
        page = HbMinigamesPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(num_of_games_played):
            login_page.go_to_main_page()
            page.go_to_minigame(minigame_name="Number Memory")
            page.start_minigame(NumMemoryPageLocators.START_BUTTON)

            # Complete the minigame for some time
            for i in range(rounds_to_play):
                number_to_store = page.browser.find_element(*NumMemoryPageLocators.TEXT_NUM_TO_SAVE).text
                page.fill_number_memory_number(number_to_insert=number_to_store)
                page.browser.find_element(*NumMemoryPageLocators.NEXT_BUTTON).click()

            # Intentionally fail the game to save results
            page.fill_number_memory_number(number_to_insert="123")
            page.save_minigame_results()

            time.sleep(5)

    @pytest.mark.reaction_time
    def test_reaction_time(self, browser, num_of_games_played: int):
        page = HbMinigamesPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(num_of_games_played):
            login_page.go_to_main_page()
            page.go_to_minigame(minigame_name="Reaction Time")
            page.start_minigame(ReactTimePageLocators.START_BUTTON)

            # Complete the minigame for some time
            for i in range(4):
                page.perform_reaction_time_action()
                page.browser.find_element(*ReactTimePageLocators.NEXT_BUTTON).click()

            # Final click - moved here to not click on next button
            page.perform_reaction_time_action()
            page.save_minigame_results()

            time.sleep(5)

    @pytest.mark.typing
    def test_typing_time(self, browser, num_of_games_played: int):
        page = HbMinigamesPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(num_of_games_played):
            login_page.go_to_main_page()
            page.go_to_minigame(minigame_name="Typing")
            page.perform_typing_time_test()
            page.save_minigame_results()

            time.sleep(5)

    @pytest.mark.sequence_memory
    def test_sequence_memory(self, browser, num_of_games_played: int):
        rounds_to_play = 50
        page = HbMinigamesPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(num_of_games_played):
            login_page.go_to_main_page()
            page.go_to_minigame(minigame_name="Sequence Memory")
            page.start_minigame(MemorySequencePageLocators.START_BUTTON)

            # Complete the minigame for some time
            num_of_elements_to_save = 1
            for level in range(rounds_to_play):
                active_buttons_list = []
                for i in range(num_of_elements_to_save):
                    active_element = WebDriverWait(page.browser, 10).until(EC.visibility_of_element_located(MemorySequencePageLocators.ACTIVE_BUTTON))
                    active_buttons_list.append(active_element)
                    while "active" in active_element.get_attribute("class"):
                        time.sleep(0.2)

                if num_of_elements_to_save < 40:
                    for item in active_buttons_list:
                        item.click()

                # Intentionally fail the game to save results
                else:
                    try:
                        for item in active_buttons_list[::-1]:
                            item.click()
                    except Exception:
                        page.save_minigame_results()
                        time.sleep(5)
                        break

                num_of_elements_to_save += 1

    @pytest.mark.visual_memory
    def test_visual_memory(self, browser, num_of_games_played: int):
        rounds_to_play = 200
        page = HbMinigamesPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(num_of_games_played):
            login_page.go_to_main_page()
            page.go_to_minigame(minigame_name="Visual Memory")
            page.start_minigame(VisualMemoryPageLocators.START_BUTTON)

            # Complete the minigame for some time
            for level in range(rounds_to_play):
                page = HbMinigamesPage(browser=browser, timeout=5)
                WebDriverWait(page.browser, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[@class = 'css-dd6wi1']/span[text()='{level+1}']")))
                active_buttons_list = page.browser.find_elements(*VisualMemoryPageLocators.ACTIVE_BUTTON)
                time.sleep(2)

                for i in active_buttons_list:
                    i.click()

                try:
                    quick_page = HbMinigamesPage(browser=browser)
                    if WebDriverWait(quick_page.browser, 0.1).until(EC.visibility_of_element_located(BasePageLocators.SAVE_RESULTS_BUTTON)) is not False:
                        page.save_minigame_results()
                except TimeoutException:
                    continue

            time.sleep(5)

    @pytest.mark.chimp_test
    def test_chimp_test(self, browser, num_of_games_played: int):
        rounds_to_play = 50
        page = HbMinigamesPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(num_of_games_played):
            login_page.go_to_main_page()
            page.go_to_minigame(minigame_name="Chimp Test")
            page.start_minigame(ChimpTestPageLocators.START_BUTTON)

            # Complete the minigame for some time
            for level in range(rounds_to_play):
                page = HbMinigamesPage(browser=browser)
                WebDriverWait(page.browser, 2).until(EC.presence_of_element_located(ChimpTestPageLocators.ACTIVE_BUTTON))
                active_buttons_list = page.browser.find_elements(*ChimpTestPageLocators.ACTIVE_BUTTON)

                for i in sorted(active_buttons_list, key=lambda x: int(x.get_attribute("data-cellnumber"))):
                    i.click()

                try:
                    page.browser.find_element(*ChimpTestPageLocators.CONTINUE_BUTTON).click()
                except NoSuchElementException:
                    page.save_minigame_results()
                    break

            time.sleep(5)

    @pytest.mark.verbal_memory
    def test_verbal_memory(self, browser, num_of_games_played: int):
        rounds_to_play = 1000
        page = HbMinigamesPage(browser=browser, timeout=5)
        page.open()
        # Login
        page.go_to_login_page()
        login_page = HbLoginPage(browser=browser, timeout=5)
        login_page.login(login=TestHumanBenchmark.login, password=TestHumanBenchmark.password)
        page.verify_is_on_dashboard_page()
        for i in range(num_of_games_played):
            login_page.go_to_main_page()
            page.go_to_minigame(minigame_name="Verbal Memory")
            page.start_minigame(VerbalMemoryPageLocators.START_BUTTON)

            words_list = []
            # Complete the minigame for some time
            for level in range(rounds_to_play):
                page = HbMinigamesPage(browser=browser)
                active_word = WebDriverWait(page.browser, 2).until(EC.presence_of_element_located(VerbalMemoryPageLocators.WORD_LOCATOR))
                active_element_text = active_word.text

                if active_element_text not in words_list:
                    page.browser.find_element(*VerbalMemoryPageLocators.NEW_BUTTON).click()
                    words_list.append(active_element_text)
                else:
                    page.browser.find_element(*VerbalMemoryPageLocators.SEEN_BUTTON).click()

            # Intentionally fail the game to save results
            for i in range(3):
                active_word = WebDriverWait(page.browser, 2).until(EC.presence_of_element_located(VerbalMemoryPageLocators.WORD_LOCATOR))
                active_element_text = active_word.text

                if active_element_text in words_list:
                    page.browser.find_element(*VerbalMemoryPageLocators.NEW_BUTTON).click()
                    words_list.append(active_element_text)
                else:
                    page.browser.find_element(*VerbalMemoryPageLocators.SEEN_BUTTON).click()

            page.save_minigame_results()
            time.sleep(5)
