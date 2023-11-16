from pages.start_page import StartPage
from pages.order_first_page import OrderFirstPage
from pages.about_rent_page import AboutRent
from pages.order_status_page import OrderStatusPage
from datetime import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


class TestOrderPositiveFlow:
    data_set = [["Марк", "Твен", "Москва", "Орехово", "79999999999", "сутки", "black", ""],
                ["Фенимор", "Купер", "Подольск", "Сокольники", "79001236666", "двое суток", "grey", "комментарий"]]

    @pytest.mark.parametrize('name, surname, address, metro, phone, term, color, comment', data_set)
    def test_complete_order_positive_scenario(self, scooter_page, name, surname, address, metro, phone, term, color, comment):
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
        assert page.check_order_confirmation_window() == True
        page.click_check_status_button()
        page = OrderStatusPage(self.driver)
        page.click_scooter_logo_button()
        assert page.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
        page = StartPage(self.driver)
        page.click_yandex_logo_button()
        page.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//form[ @action = "https://yandex.ru/search/"]')))
        assert page.driver.current_url == 'https://dzen.ru/?yredirect=true'

    def test_click_bottom_order_button(self, scooter_page):
        self.driver = scooter_page
        page = StartPage(self.driver)
        page.close_cookie_notify()
        page.click_bottom_order_button()
        assert page.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'



