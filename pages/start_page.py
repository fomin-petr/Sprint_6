from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.start_page_locators import StartPageLocators


class StartPage(BasePage):

    def close_cookie_notify(self):
        self.click_on_element(StartPageLocators.ACCEPT_COOKIES_BUTTON)

    def click_important_question(self, number):
        method, locator = StartPageLocators.IMPORTANT_QUESTION
        locator = locator.format(number)
        element = [method, locator]
        self.click_on_element(element)

    def get_important_reply(self, number):
        method, locator = StartPageLocators.IMPORTANT_REPLY
        locator = locator.format(number)
        return self.driver.find_element(method, locator).text

    def click_header_order_button(self):
        self.click_on_element(StartPageLocators.HEADER_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.click_on_element(StartPageLocators.BOTTOM_ORDER_BUTTON)

    def click_yandex_logo_button(self):
        self.click_on_element(StartPageLocators.YANDEX_LOGO_BUTTON)
