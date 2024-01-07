import time

import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture()
def scooter_page():
    driver = webdriver.Firefox()
    driver.get(Urls.start_page)
    yield driver
    driver.quit()
