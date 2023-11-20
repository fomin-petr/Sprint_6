from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.about_rent_locators import AboutRentLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    def input_in_field(self, element, keys):
        self.driver.find_element(*element).send_keys(keys)

    def check_element_present(self, element):
        try:
            self.driver.find_element(*element)
        except NoSuchElementException:
            return False
        return True

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, element)))
        return True
