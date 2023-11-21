from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_first_page_locators import OrderFirstPageLocators


class OrderFirstPage(BasePage):

    def input_name(self, name):
        self.input_in_field(OrderFirstPageLocators.NAME_FIELD, name)

    def input_surname(self, surname):
        self.input_in_field(OrderFirstPageLocators.SURNAME_FIELD, surname)

    def input_address(self, address):
        self.input_in_field(OrderFirstPageLocators.ADDRESS_FIELD, address)

    def select_metro(self, metro):
        method, locator = OrderFirstPageLocators.METRO_SELECTION_ITEM
        locator = locator.format(metro)
        element = [method, locator]
        self.click_on_element(OrderFirstPageLocators.METRO_SELECTION_FIELD)
        self.click_on_element(element)

    def input_phone(self, phone):
        self.input_in_field(OrderFirstPageLocators.PHONE_FIELD, phone)

    def click_next_button(self):
        self.click_on_element(OrderFirstPageLocators.ORDER_NEXT_BUTTON)

    def fill_out_form(self, name, surname, address, metro, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.select_metro(metro)
        self.input_phone(phone)
        self.click_next_button()