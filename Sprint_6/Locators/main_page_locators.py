from selenium.webdriver.common.by import By
from Locators.base_page_locator import BasePageLocator

class MainPageLocator(BasePageLocator):
    Requests = [
            (By.XPATH, '//div[@id="accordion__heading-8"]'),
            (By.XPATH, "//div[@id='accordion__heading-9']"),
            (By.XPATH, "//div[@id='accordion__heading-10']"),
            (By.XPATH, "//div[@id='accordion__heading-11']"),
            (By.XPATH, "//div[@id='accordion__heading-12']"),
            (By.XPATH, "//div[@id='accordion__heading-13']"),
            (By.XPATH, "//div[@id='accordion__heading-14']"),
            (By.XPATH, "//div[@id='accordion__heading-15']")
        ]

    Responses = [
            (By.XPATH, 'div[id="accordion__panel-8"]'),
            (By.XPATH, 'div[id="accordion__panel-9"]'),
            (By.XPATH, 'div[id="accordion__panel-10"]'),
            (By.XPATH, 'div[id="accordion__panel-11"]'),
            (By.XPATH, 'div[id="accordion__panel-12"]'),
            (By.XPATH, 'div[id="accordion__panel-13"]'),
            (By.XPATH, 'div[id="accordion__panel-14"]'),
            (By.XPATH, 'div[id="accordion__panel-15"]')
        ]
