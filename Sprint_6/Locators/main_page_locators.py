from selenium.webdriver.common.by import By
from Locators.base_page_locator import BasePageLocator

class MainPageLocator(BasePageLocator):
    Requests = [
            (By.XPATH, '//div[@id="accordion__heading-0"]'),
            (By.XPATH, "//div[@id='accordion__heading-1']"),
            (By.XPATH, "//div[@id='accordion__heading-2']"),
            (By.XPATH, "//div[@id='accordion__heading-3']"),
            (By.XPATH, "//div[@id='accordion__heading-4']"),
            (By.XPATH, "//div[@id='accordion__heading-5']"),
            (By.XPATH, "//div[@id='accordion__heading-6']"),
            (By.XPATH, "//div[@id='accordion__heading-7']")
        ]

    Responses = [
            (By.XPATH, 'div[id="accordion__panel-0"]'),
            (By.XPATH, 'div[id="accordion__panel-1"]'),
            (By.XPATH, 'div[id="accordion__panel-2"]'),
            (By.XPATH, 'div[id="accordion__panel-3"]'),
            (By.XPATH, 'div[id="accordion__panel-4"]'),
            (By.XPATH, 'div[id="accordion__panel-5"]'),
            (By.XPATH, 'div[id="accordion__panel-6"]'),
            (By.XPATH, 'div[id="accordion__panel-7"]')
        ]
