import pytest
from selenium import webdriver
from URLS import URL_Scooter

@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(URL_Scooter)
    yield firefox_driver
    firefox_driver.quit()
