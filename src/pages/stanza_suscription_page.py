from src.pages.base_page import BasePage
from src.locators.stanza_suscription_page_locators import StanzaSuscriptionPageLocators


class StanzaSuscriptionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.switch_to_recent_open_tab()

        # wait until page loads
        self.find_element(StanzaSuscriptionPageLocators.page, wait=5)

        url = self.driver.current_url
        self.close_tab()
        self.return_to_main_tab()

        return url
