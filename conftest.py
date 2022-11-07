import pytest
import json
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Browser to run the test cases (options: chrome, firefox)"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Set headless mode"
    )


@pytest.fixture
def args(request, scope='session'):
    return {
        "browser": request.config.getoption("--browser"),
        "headless": request.config.getoption("--headless")
    }


@pytest.fixture
def driver(args):
    # Set Up driver
    driver = browser_selection(args["browser"])
    driver.maximize_window()
    driver.get("https://www.steelers.com/schedule/")

    yield driver

    driver.quit()


def browser_selection(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    elif browser == "edge":
        driver = None
    elif browser == "opera":
        driver = None
    elif browser == "brave":
        driver = None
    elif browser == "chromium":
        driver = None
    return driver
