from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.start_page_locators import StartPageLocators


class StartPage(BasePage):
    accept_cookies_button = [By.ID, 'rcc-confirm-button']
    important_question = [By.ID, 'accordion__heading-{}']
    important_reply = [By.ID, 'accordion__panel-{}']
    header_order_button = [By.XPATH, '//div[ contains(@class, "Header")]/button[ text()="Заказать" ]']
    bottom_order_button = [By.XPATH, '//div[ contains(@class, "Home_FinishButton")]/button[ text()="Заказать" ]']
    yandex_logo_button = [By.XPATH, '//img[ @alt="Yandex" ]/parent::a']

    def close_cookie_notify(self):
        self.click_on_element(StartPageLocators.ACCEPT_COOKIES_BUTTON)

    def click_important_question(self, number):
        method, locator = self.important_question
        locator = locator.format(number)
        element = [method, locator]
        self.click_on_element(element)

    def get_important_reply(self, number):
        method, locator = self.important_reply
        locator = locator.format(number)
        return self.driver.find_element(method, locator).text

    def click_header_order_button(self):
        self.click_on_element(StartPageLocators.HEADER_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.click_on_element(StartPageLocators.BOTTOM_ORDER_BUTTON)

    def click_yandex_logo_button(self):
        self.click_on_element(StartPageLocators.YANDEX_LOGO_BUTTON)
