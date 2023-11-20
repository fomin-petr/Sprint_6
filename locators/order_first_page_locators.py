from selenium.webdriver.common.by import By


class OrderFirstPageLocators:
    NAME_FIELD = [By.XPATH, '//input[ @placeholder="* Имя"]']
    SURNAME_FIELD = [By.XPATH, '//input[ @placeholder="* Фамилия"]']
    ADDRESS_FIELD = [By.XPATH, '//input[ contains(@placeholder, "Адрес") ]']
    METRO_SELECTION_FIELD = [By.XPATH, '//input[ contains(@placeholder, "метро") ]']
    PHONE_FIELD = [By.XPATH, '//input[ contains(@placeholder, "Телефон") ]']
    ORDER_NEXT_BUTTON = [By.XPATH, '//button[ contains(text(), "Далее") ]']
    METRO_SELECTION_ITEM = [By.XPATH, '//li[ @class ="select-search__row"]//div[text()="{}"]']
