from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class OrderStatusPage:
    scooter_logo_button = [By.XPATH, '//img[@alt="Scooter"]/parent::a']

    def __init__(self, driver):
        self.driver = driver

    def click_scooter_logo_button(self):
        self.driver.find_element(*self.scooter_logo_button).click()
