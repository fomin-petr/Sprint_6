from locators.about_rent_locators import AboutRentLocators
from pages.base_page import BasePage


class AboutRent(BasePage):

    def select_date(self, when_date):
        self.click_on_element(AboutRentLocators.DATE_FIELD)
        method, locator = AboutRentLocators.PICK_DATE
        locator = locator.format(when_date)
        element = [method, locator]
        self.click_on_element(element)

    def select_term(self, term):
        method, locator = AboutRentLocators.PICK_TERM
        locator = locator.format(term)
        element = [method, locator]
        self.click_on_element(AboutRentLocators.RENT_TERM)
        self.click_on_element(element)

    def select_color(self, color):
        method, locator = AboutRentLocators.PICK_COLOR
        locator = locator.format(color)
        element = [method, locator]
        self.click_on_element(element)

    def input_comment(self, comment):
        self.input_in_field(AboutRentLocators.COMMENT_FIELD, comment)

    def click_next_button(self):
        self.click_on_element(AboutRentLocators.ORDER_BUTTON)

    def click_yes_order_button(self):
        self.click_on_element(AboutRentLocators.YES_ORDER_BUTTON)

    def check_order_confirmation_window(self):
        return self.check_element_present(AboutRentLocators.ORDER_CONFIRMATION_WINDOW)

    def click_check_status_button(self):
        self.click_on_element(AboutRentLocators.CHECK_STATUS_BUTTON)

    def fill_out_form(self, when_date, term, color, comment):
        self.select_date(when_date)
        self.select_term(term)
        self.select_color(color)
        self.input_comment(comment)
        self.click_next_button()
        self.click_yes_order_button()






