from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, relative_to=None, wait=0):
        root = relative_to if relative_to else self.driver
        return WebDriverWait(self.driver, wait).until(
            lambda _: root.find_element(*locator)
        )

    def find_elements(self, locator, relative_to=None):
        root = relative_to if relative_to else self.driver
        return root.find_elements(*locator)

    def is_present(self, locator, relative_to=None):
        return len(self.find_elements(locator, relative_to)) > 0

    def is_not_present(self, locator, relative_to=None):
        return not self.is_present(locator, relative_to)

    def return_element_if_present(self, locator, relative_to=None):
        elements = self.find_elements(locator, relative_to)

        if len(elements) > 0:
            return elements[0]
        else:
            return None

    def get_page_url(self):
        return self.driver.current_url

    def switch_to_recent_open_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_tab(self):
        self.driver.close()

    def return_to_main_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
