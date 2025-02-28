import pytest
from selenium import webdriver
from URLS import URL_Scooter

@pytest.fixture()
def general_settings():
    driver = webdriver.Firefox()
    driver.get(URL_Scooter)
    yield driver
    driver.quit()
