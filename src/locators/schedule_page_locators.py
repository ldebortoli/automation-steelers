from selenium.webdriver.common.by import By


class SchedulePageLocators:
    iframe_stanzacal = By.XPATH, "//div[@class=\"stanzacal\"]/iframe[@name=\"sdk-stanzacal\"][@data-loaded=\"true\"]"

    stranzacal_past_events = By.XPATH, "//div[@id=\"tile-list\"]//span[contains(@class, \"past\")]/parent::div/parent::div/parent::div"
    stranzacal_upcoming_events = By.XPATH, "//div[@id=\"tile-list\"]//span[contains(@class, \"future\")]/parent::div/parent::div/parent::div"

    ticket_link = By.XPATH, ".//div[@class=\"tile-link-text\"]/parent::a"
    event_date = By.XPATH, ".//span[starts-with(@class, \"tile-data-date\")]"

    add_to_calendar = By.ID, "stanza-add-to-calendar"
