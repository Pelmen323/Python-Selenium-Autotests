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


def pytest_addoption(parser):
    parser.addoption('--scope',
                     action='store',
                     default='all',
                     help="Choose executed tests - 'all', 'human_aim', 'number_memory', 'reaction_time', 'typing', 'sequence_memory', 'visual_memory', 'chimp_test', 'verbal_memory'",
                     choices=("all", "human_aim", "number_memory", "reaction_time", "typing", "sequence_memory", "visual_memory", "chimp_test", "verbal_memory"))
    parser.addoption('--rounds',
                     action='store',
                     default='1',
                     help="Choose the number of games to play")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--scope") == "all":
        # --runslow given in cli: do not skip slow tests
        return
    skip_test = pytest.mark.skip(reason="need to pass this script name as arg in cli, or pass nothing/'all' to execute all scripts at the same time")
    for item in items:
        if f'{config.getoption("--scope")}' not in item.keywords:
            item.add_marker(skip_test)


@pytest.fixture
def num_of_games_played(request):
    if int(request.config.getoption("--rounds")) > 0:
        return int(request.config.getoption("--rounds"))
    else:
        raise ValueError("The number of times the game played should be integer and it should be > 0")
