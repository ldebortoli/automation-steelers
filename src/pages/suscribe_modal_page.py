from src.pages.base_page import BasePage
from src.locators.suscribe_modal_page_locators import SuscribeModalPageLocators

class SuscribeModalPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def close_modal(self):
        if self.is_present(SuscribeModalPageLocators.modal):
            self.find_element(SuscribeModalPageLocators.later).click()
