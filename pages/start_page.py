from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class StartPage:
    accept_cookies_button = [By.ID, 'rcc-confirm-button']
    important_question = [By.ID, 'accordion__heading-{}']
    important_reply = [By.ID, 'accordion__panel-{}']
    header_order_button = [By.XPATH, '//div[ contains(@class, "Header")]/button[ text()="Заказать" ]']
    bottom_order_button = [By.XPATH, '//div[ contains(@class, "Home_FinishButton")]/button[ text()="Заказать" ]']

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    def wait_for_page_loading(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located('rcc-confirm-button'))

    def close_cookie_notify(self):
        self.driver.find_element(*self.accept_cookies_button).click()

    def click_important_question(self, number):
        method, locator = self.important_question
        locator = locator.format(number)
        self.driver.find_element(method, locator).click()

    def get_important_reply(self, number):
        method, locator = self.important_reply
        locator = locator.format(number)
        return self.driver.find_element(method, locator).text

    def click_header_order_button(self):
        self.driver.find_element(*self.header_order_button).click()

    def click_bottom_order_button(self):
        self.driver.find_element(*self.bottom_order_button).click()







