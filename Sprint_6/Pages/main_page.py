from Pages.base_page import BasePage
import allure
from Locators.main_page_locators import MainPageLocator
from Locators.base_page_locator import BasePageLocator


@allure.step ('По номеру возвращается локатор из блока вопросов')
def requests_position(position):
    return MainPageLocator.Requests[position]

@allure.step ('По номеру возвращается локатор из блока ответов')
def responses_position(position):
    return MainPageLocator.Responses[position]

class MainPage(BasePage):

    @allure.step('Ищем блок FAQ, раскрываем вопросы и ответы')
    def click_and_get_answer(self, position):
        self.waiting_visibility_element(requests_position(position)).click()
        return self.waiting_visibility_element(responses_position(position))

    @allure.step('Скроллим до необходимого элемента')
    def scrolling_to_block_of_elements(self):
        self.scroll_to_element(MainPageLocator.Requests[2])

    @allure.step ('После скролла ждем появление необходимого элемента')
    def wait_show_up_element(self):
        self.waiting_visibility_element(MainPageLocator.Requests[2])



    @allure.step('Нажимаем на кнопку Логотип Яндекса')
    def click_logo_yandex(self):
        self.click_element(BasePageLocator.button_logo_yandex)

    @allure.step('Ждем появление страницы Дзен после нажатия на лого Яндекса')
    def wait_headline_dzen(self):
        self.wait_headline_on_top('Дзен')
        if self.waiting_clickable_element(BasePageLocator.exit_button_in_extra_window_dzen):
            self.click_element(BasePageLocator.exit_button_in_extra_window_dzen)
        return self.get_current_url

    @allure.step('Нажимаем на кнопку Логотип Самокат')
    def click_logo_samokat(self):
        self.click_element(BasePageLocator.button_logo_samokat)

    @allure.step('Ждем появление страницы Самоката после нажатия на лого Самоката')
    def wait_headline_scooter(self):
        self.wait_headline_on_top('Самокат')

    @allure.step('Переключаем драйвер на новое окно')
    def switch_driver(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Нажимаем на кнопку Заказать в заголовке страницы')
    def order_button_in_header_click(self):
        self.click_element(BasePageLocator.order_button_high)

    @allure.step('Нажимаем на кнопку Заказать внизу страницы')
    def order_button_in_bottom_click(self):
        self.click_element(BasePageLocator.order_button_bottom)