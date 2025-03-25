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
    def enter_phone_field(self, telephone_number):
        self.waiting_visibility_element(OrderPageLocator.phone_field).send_keys(telephone_number)

    @allure.step('Нажимаем кнопку Далее')
    def click_continue_button(self):
        self.waiting_visibility_element(OrderPageLocator.button_next).click()

    @allure.step('Заполняем поле начала аренды')
    def enter_date_delivery(self):
        self.waiting_visibility_element(OrderPageLocator.date_field).click()
        self.waiting_visibility_element(OrderPageLocator.delivery_date).click()

    @allure.step('Заполняем поле срока аренды')
    def enter_rental_period(self):
        self.waiting_visibility_element(OrderPageLocator.rent_time_field).click()
        self.waiting_visibility_element(OrderPageLocator.rent_time_one_day).click()

    @allure.step('Нажимаем кнопку Заказать')
    def click_order_button(self):
        self.waiting_visibility_element(OrderPageLocator.button_order).click()

    @allure.step('Подтверждаем оформление заказа')
    def click_button_yes_in_confirm(self):
        self.waiting_visibility_element(OrderPageLocator.button_yes).click()

