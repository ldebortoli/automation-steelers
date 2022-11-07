import re
from datetime import date, datetime

from src.pages.base_page import BasePage
from src.locators.schedule_page_locators import SchedulePageLocators


class SchedulePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_stanzacal_iframe(self):
        iframe = self.find_element(SchedulePageLocators.iframe_stanzacal)
        self.driver.switch_to.frame(iframe)

    def stranzacal_upcoming_events(self):
        return self.find_elements(
            SchedulePageLocators.stranzacal_upcoming_events
        )

    def stranzacal_past_events(self):
        return self.find_elements(
            SchedulePageLocators.stranzacal_past_events
        )

    def get_event_date(self, event):
        event_date = self.find_element(
            SchedulePageLocators.event_date,
            relative_to=event
        )
        date = event_date.text.title()

        # Add padding
        length = len(date)
        if date[length - 2] == " ":
            date = date[:(length - 2)] + f" 0{date[length - 1]}"

        today = datetime.today().date()
        parsed_date = datetime.strptime(date, '%a, %b %d').date().replace(year=today.year)

        if parsed_date < today:
            parsed_date = parsed_date.replace(year=today.year + 1)

        return parsed_date

    def get_ticket_link_from_event(self, event):
        return self.return_element_if_present(
            SchedulePageLocators.ticket_link,
            relative_to=event
        )

    def ticket_is_not_present(self, event):
        return self.is_not_present(
            SchedulePageLocators.ticket_link,
            relative_to=event
        )

    def get_date_from_ticket_link_url(self, ticket_link):
        url = ticket_link.get_attribute('href')
        regexp = r'www\.ticketmaster\.com\%2F([a-z]+-)+([01]\d-[0123]\d-\d\d\d\d)%2Fevent'
        matches = re.search(regexp, url)
        return datetime.strptime(matches.group(2), '%m-%d-%Y').date()

    def add_to_calendar(self):
        add_to_calendar = self.find_element(SchedulePageLocators.add_to_calendar)
        self.driver.execute_script("arguments[0].scrollIntoView({block: \"center\"});", add_to_calendar)
        add_to_calendar.click()
