from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AboutRent:
    date_field = [By.XPATH, '//input[ contains(@placeholder, "Когда") ]']
    pick_date = [By.XPATH, '//div[ contains(@class, "react-datepicker__day--0{}") ]']
    rent_term = [By.XPATH, '//div[ contains(text(), "Срок") ]']
    pick_term = [By.XPATH, '//div[ @class="Dropdown-option" and text()="{}" ]' ]
    pick_color = [By.ID, '{}']
    comment_field = [By.XPATH, '//input[ contains(@placeholder, "Комментарий") ]']
    order_button = [By.XPATH, '//div[ contains(@class, "Order_Buttons")]/button[ text()="Заказать" ]']
    yes_order_button = [By.XPATH, '//button[ text()="Да" ]']
    order_confirmation_window = [By.XPATH, '//div[ contains(text(), "Заказ оформлен") ]']
    check_status_button = [By.XPATH, '//button[ text()="Посмотреть статус" ]']

    def __init__(self, driver):
        self.driver = driver

    def select_date(self, when_date):
        self.driver.find_element(*self.date_field).click()
        method, locator = self.pick_date
        locator = locator.format(when_date)
        self.driver.find_element(method, locator).click()

    def select_term(self, term):
        method, locator = self.pick_term
        locator = locator.format(term)
        self.driver.find_element(*self.rent_term).click()
        self.driver.find_element(method, locator).click()

    def select_color(self, color):
        method, locator = self.pick_color
        locator = locator.format(color)
        self.driver.find_element(method, locator).click()

    def input_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def click_next_button(self):
        self.driver.find_element(*self.order_button).click()

    def click_yes_order_button(self):
        self.driver.find_element(*self.yes_order_button).click()

    def check_order_confirmation_window(self):
        try:
            self.driver.find_element(*self.order_confirmation_window)
        except NoSuchElementException:
            return False
        return True

    def click_check_status_button(self):
        self.driver.find_element(*self.check_status_button).click()
    def fill_out_form(self, when_date, term, color, comment):
        self.select_date(when_date)
        self.select_term(term)
        self.select_color(color)
        self.input_comment(comment)
        self.click_next_button()
        self.click_yes_order_button()






