import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser(*args):
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    yield browser
    browser.quit()
