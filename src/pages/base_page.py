from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def search_word_in_bar(self, word):
        self.driver.find_element(By.XPATH, "//input[@name=\"q\"][@type=\"text\"]").send_keys(word)
        self.driver.find_element(By.XPATH, "//form/div[1]/div[1]/div[4]/center//input[@role=\"button\"]").click()
