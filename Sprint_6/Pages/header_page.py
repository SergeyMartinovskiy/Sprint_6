import allure
from Locators.header_page_locators import HeaderPageLocator
from Pages.base_page import BasePage

class HeaderPage(BasePage):
    @allure.step('Нажимаем на кнопку Логотип Яндекса')
    def click_logo_yandex(self):
        self.click_element(HeaderPageLocator.button_logo_yandex)


    @allure.step('Нажимаем на кнопку Логотип Самокат')
    def click_logo_samokat(self):
        self.click_element(HeaderPageLocator.button_logo_samokat)

