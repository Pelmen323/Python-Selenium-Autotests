import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import allure

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

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass # just ignore

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

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
