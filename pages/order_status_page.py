from pages.base_page import BasePage
from locators.order_status_page_locators import OrderStatusPageLocators


class OrderStatusPage(BasePage):

    def click_scooter_logo_button(self):
        self.click_on_element(OrderStatusPageLocators.SCOOTER_LOGO_BUTTON)
