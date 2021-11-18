import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose locale")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    if user_language in ("ar", "ca", "cs", "da", "de", "en", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "zh-hans", "uk"):
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    else:
        raise pytest.UsageError(f"--language {user_language} is not supported")
    yield browser
    browser.quit()
