from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderFirstPage:
    name_field = [By.XPATH, '//input[ @placeholder="* Имя"]']
    surname_field = [By.XPATH, '//input[ @placeholder="* Фамилия"]']
    address_field = [By.XPATH, '//input[ contains(@placeholder, "Адрес") ]']
    metro_selection_field = [By.XPATH, '//input[ contains(@placeholder, "метро") ]']
    phone_field = [By.XPATH, '//input[ contains(@placeholder, "Телефон") ]']
    order_next_button = [By.XPATH, '//button[ contains(text(), "Далее") ]']
    metro_selection_item = [By.XPATH, '//li[ @class ="select-search__row"]//div[text()="{}"]']

    def __init__(self, driver):
        self.driver = driver

    def input_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def input_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def input_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def select_metro(self, metro):
        method, locator = self.metro_selection_item
        locator = locator.format(metro)
        self.driver.find_element(*self.metro_selection_field).click()
        self.driver.find_element(method, locator).click()

    def input_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.order_next_button).click()

    def fill_out_form(self, name, surname, address, metro, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.select_metro(metro)
        self.input_phone(phone)
        self.click_next_button()