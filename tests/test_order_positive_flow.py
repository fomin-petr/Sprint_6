from pages.start_page import StartPage
from pages.order_first_page import OrderFirstPage
from pages.about_rent_page import AboutRent
from pages.order_status_page import OrderStatusPage
from datetime import datetime
from locators.external_locators import ExternalLocators
from selenium.webdriver.common.by import By
from data import DataForTests, Urls
import pytest


class TestOrderPositiveFlow:

    @pytest.mark.parametrize('name, surname, address, metro, phone, term, color, comment', DataForTests.data_set)
    def test_complete_order_positive_scenario(self, scooter_page, name, surname, address, metro, phone, term, color,
                                              comment):
        self.driver = scooter_page
        page = StartPage(self.driver)
        page.close_cookie_notify()
        page.click_header_order_button()
        page = OrderFirstPage(self.driver)
        page.fill_out_form(name, surname, address, metro, phone)
        page = AboutRent(self.driver)
        order_date = datetime.now().day
        order_date += 1
        page.fill_out_form(order_date, term, color, comment)
        assert page.check_order_confirmation_window()

    @pytest.mark.parametrize('name, surname, address, metro, phone, term, color, comment', DataForTests.data_set)
    def test_scooter_logo_button_after_order(self, scooter_page, name, surname, address, metro, phone, term, color,
                                             comment):
        self.driver = scooter_page
        page = StartPage(self.driver)
        page.close_cookie_notify()
        page.click_header_order_button()
        page = OrderFirstPage(self.driver)
        page.fill_out_form(name, surname, address, metro, phone)
        page = AboutRent(self.driver)
        order_date = datetime.now().day
        order_date += 1
        page.fill_out_form(order_date, term, color, comment)
        page.click_check_status_button()
        page = OrderStatusPage(self.driver)
        page.click_scooter_logo_button()
        assert page.driver.current_url == Urls.start_page

    @pytest.mark.parametrize('name, surname, address, metro, phone, term, color, comment', DataForTests.data_set)
    def test_yandex_logo_button_after_order(self, scooter_page, name, surname, address, metro, phone, term, color,
                                            comment):
        self.driver = scooter_page
        page = StartPage(self.driver)
        page.close_cookie_notify()
        page.click_header_order_button()
        page = OrderFirstPage(self.driver)
        page.fill_out_form(name, surname, address, metro, phone)
        page = AboutRent(self.driver)
        order_date = datetime.now().day
        order_date += 1
        page.fill_out_form(order_date, term, color, comment)
        page.click_check_status_button()
        page = StartPage(self.driver)
        page.click_yandex_logo_button()
        page.driver.switch_to.window(self.driver.window_handles[1])
        page.wait_for_element(ExternalLocators.DZEN_SEARCH_FIELD)
        assert page.check_element_present([By.XPATH, ExternalLocators.DZEN_SEARCH_FIELD])

    def test_click_bottom_order_button(self, scooter_page):
        self.driver = scooter_page
        page = StartPage(self.driver)
        page.close_cookie_notify()
        page.click_bottom_order_button()
        assert page.driver.current_url == Urls.order_page
