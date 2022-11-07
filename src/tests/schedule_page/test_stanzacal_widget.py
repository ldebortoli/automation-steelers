import time
import pytest

from src.tests.base_test import BaseTest
from src.pages.schedule_page import SchedulePage
from src.pages.suscribe_modal_page import SuscribeModalPage
from src.pages.stanza_suscription_page import StanzaSuscriptionPage

from src.locators.schedule_page_locators import SchedulePageLocators
from src.locators.suscribe_modal_page_locators import SuscribeModalPageLocators


@pytest.fixture
def schedule_page(driver):
    suscribe_modal_page = SuscribeModalPage(driver)
    suscribe_modal_page.close_modal()

    schedule_page = SchedulePage(driver)
    schedule_page.switch_to_stanzacal_iframe()
    yield schedule_page


@pytest.fixture
def stanza_suscription_page(driver):
    stanza_suscription_page = StanzaSuscriptionPage(driver)
    yield stanza_suscription_page


@pytest.mark.usefixtures("schedule_page")
class TestStanzacalWidget(BaseTest):

    def test_validate_ticket_links_in_upcoming_events(self, schedule_page):
        upcoming_events = schedule_page.stranzacal_upcoming_events()

        for event in upcoming_events:
            event_date = schedule_page.get_event_date(event)
            ticket_link = schedule_page.get_ticket_link_from_event(event)
            assert ticket_link is not None, f"Ticket link is not present in event date {event_date}"

            ticket_link_date = schedule_page.get_date_from_ticket_link_url(ticket_link)
            assert event_date == ticket_link_date

    def test_no_ticket_links_in_past_events(self, schedule_page):
        past_events = schedule_page.stranzacal_past_events()

        for event in past_events:
            assert schedule_page.ticket_is_not_present(event), \
                   f"Ticket link is present in event date {schedule_page.get_event_date(event)}"

    def test_add_to_calendar_button_loads_correct_url(self, schedule_page, stanza_suscription_page):
        schedule_page.add_to_calendar()
        calendar_suscription_url = stanza_suscription_page.get_url()
        assert "nfl-steelers" in calendar_suscription_url
