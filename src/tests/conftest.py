import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def config(scope='session'):

    with open("config.json", 'r') as file:
        config = json.load(file)

    sanitized_browsers = []

    for browser in config["browsers"]:
        browser_lowercase = browser.lower()
        assert browser_lowercase in ["firefox", "chrome"]
        sanitized_browsers.append(browser_lowercase)

    config["browsers"] = sanitized_browsers
    return config


@pytest.fixture
def driver(config):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.google.com")

    yield driver

    driver.close()
