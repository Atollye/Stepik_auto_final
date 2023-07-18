import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose for which locale (language) run the tests")


@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    browser = webdriver.Chrome(options=options)
    request.addfinalizer(browser.quit)
    return browser
