import allure
import data
from Locators.order_page_locators import OrderPageLocator
from Pages.base_page import BasePage

class OrderPage(BasePage,data):
    @allure.step('Находим поле и вводим Имя')
    def enter_name_in_field(self, name):
        name_in_field = self.waiting_visibility_element(OrderPageLocator.name_field)
        name_in_field.send_keys(name)

    @allure.step('Находим и вводим Фамилию')
    def enter_surname_in_field(self, surname):
        surname_in_field = self.waiting_visibility_element(OrderPageLocator.surname_field)
        surname_in_field.send_keys(surname)

    @allure.step('Находим и Вводим Адрес')
    def enter_address_in_field(self, address):
        address_in_field = self.waiting_visibility_element(OrderPageLocator.address_field)
        address_in_field.send_keys(address)

    @allure.step('Находим поле Метро')
    def find_metro_field(self):
        self.waiting_visibility_element(OrderPageLocator.box_set_metro).click()

    @allure.step('Выбираем станцию Метро')
    def choose_metro_station(self):
        self.waiting_visibility_element(OrderPageLocator.set_metro_one).click()

    @allure.step('Находим поле и заполняем Номер телефона')
    @allure.step('Нажимаем кнопку Далее')
    @allure.step('Заполняем поле Срок аренды')
    @allure.step('Нажимаем кнопку Заказать')
    @allure.step('Подтверждаем оформление заказа')
    @allure.step('Вводим Имя')
