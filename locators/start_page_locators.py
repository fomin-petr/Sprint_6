from selenium.webdriver.common.by import By


class StartPageLocators:
    ACCEPT_COOKIES_BUTTON = [By.ID, 'rcc-confirm-button']
    IMPORTANT_QUESTION = [By.ID, 'accordion__heading-{}']
    IMPORTANT_REPLY = [By.ID, 'accordion__panel-{}']
    HEADER_ORDER_BUTTON = [By.XPATH, '//div[ contains(@class, "Header")]/button[ text()="Заказать" ]']
    BOTTOM_ORDER_BUTTON = [By.XPATH, '//div[ contains(@class, "Home_FinishButton")]/button[ text()="Заказать" ]']
    YANDEX_LOGO_BUTTON = [By.XPATH, '//img[ @alt="Yandex" ]/parent::a']
