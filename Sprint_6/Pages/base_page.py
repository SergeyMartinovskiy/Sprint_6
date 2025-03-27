import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators.main_page_locators import MainPageLocator


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание видимости элемента по локатору')
    def waiting_visibility_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание кликабельности элемента по локатору')
    def waiting_clickable_element(self, locator):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return element

    @allure.step('Кликаем по элементу с нужным локатором')
    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скроллим до нужного элемента по локатору')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимаем кнопку Принять Cookies')
    def click_button_accept_cookie(self):
        self.click_element(MainPageLocator.button_cookie)

    @allure.step('Получение URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дожидаемся смены URL страницы')
    def wait_url_changes(self, expected_url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(expected_url))

    @allure.step('Появления заголовка на странице')
    def wait_headline_on_top(self, headline):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_is(headline))













