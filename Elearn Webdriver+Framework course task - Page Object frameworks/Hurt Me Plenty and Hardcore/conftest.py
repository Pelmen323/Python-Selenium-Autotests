import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")                         # Invoked automatically for each test
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        s = Service(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=s)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture                                             # Invoked by @pytest.mark.usefixtures('browser2')
def browser2(request):
    browser_name = request.config.getoption("browser_name")
    browser2 = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        s = Service(ChromeDriverManager().install())
        browser2 = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        s = Service(GeckoDriverManager().install())
        browser2 = webdriver.Firefox(service=s)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser2.maximize_window()
    yield browser2
    browser2.quit()
