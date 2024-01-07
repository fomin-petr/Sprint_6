from selenium.webdriver.common.by import By


class AboutRentLocators:
    DATE_FIELD = [By.XPATH, '//input[ contains(@placeholder, "Когда") ]']
    PICK_DATE = [By.XPATH, '//div[ contains(@class, "react-datepicker__day--0{}") ]']
    RENT_TERM = [By.XPATH, '//div[ contains(text(), "Срок") ]']
    PICK_TERM = [By.XPATH, '//div[ @class="Dropdown-option" and text()="{}" ]' ]
    PICK_COLOR = [By.ID, '{}']
    COMMENT_FIELD = [By.XPATH, '//input[ contains(@placeholder, "Комментарий") ]']
    ORDER_BUTTON = [By.XPATH, '//div[ contains(@class, "Order_Buttons")]/button[ text()="Заказать" ]']
    YES_ORDER_BUTTON = [By.XPATH, '//button[ text()="Да" ]']
    ORDER_CONFIRMATION_WINDOW = [By.XPATH, '//div[ contains(text(), "Заказ оформлен") ]']
    CHECK_STATUS_BUTTON = [By.XPATH, '//button[ text()="Посмотреть статус" ]']
