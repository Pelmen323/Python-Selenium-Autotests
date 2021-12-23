from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from .pages.base_page import BasePage
import allure

@allure.severity(allure.severity_level.CRITICAL)
def test_pass(browser):
    page = BasePage(browser=browser, url="https://www.google.com/", timeout=5)
    page.open()
    logo = page.browser.find_element(By.CSS_SELECTOR, "img[alt='Google']")
    assert logo.is_displayed()

@allure.severity(allure.severity_level.MINOR)
@pytest.mark.skip
def test_skip(browser):
    page = BasePage(browser=browser, url="https://www.google.com/")
    page.open()
    logo = page.browser.find_element(By.CSS_SELECTOR, "img[alt='Google']")
    assert logo.is_displayed()

@allure.severity(allure.severity_level.NORMAL)
def test_fail(browser):
    page = BasePage(browser=browser, url="https://www.google.com/", timeout=5)
    page.open()
    search_bar = page.browser.find_element(By.CSS_SELECTOR, "input[type='text']")
    search_bar.send_keys('Google')
    page.browser.find_element(By.CSS_SELECTOR, "input[name='btnK'][type='submit']").click()
    search_bar = page.browser.find_element(By.CSS_SELECTOR, "input[role='combobox']")
    assert search_bar.get_attribute('value') != 'Google'
