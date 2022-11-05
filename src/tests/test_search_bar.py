import time
import pytest
from src.pages.base_page import BasePage


class BaseTest:
    pass


class TestSearchBar(BaseTest):

    def test_search_bar(self, driver):
        BasePage(driver).search_word_in_bar("PC")
        time.sleep(2)
