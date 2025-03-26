from Pages.base_page import BasePage
import allure
from Locators.main_page_locators import MainPageLocator
from Locators.base_page_locator import BasePageLocator

ANSWERS = [
    (0,'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
    (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, '
        'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
    (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
]

@allure.step ('По номеру возвращается локатор из блока вопросов')
def requests_position(question_index):
    return MainPageLocator.Requests[question_index]

@allure.step ('По номеру возвращается локатор из блока ответов')
def responses_position(question_index):
    return MainPageLocator.Responses[question_index]

class MainPage(BasePage):

    @allure.step('Ищем блок FAQ, раскрываем вопросы и ответы')
    def click_and_get_answer(self, question_index):
        self.waiting_clickable_element(requests_position(question_index)).click()
        self.waiting_visibility_element(responses_position(question_index))
        return self.driver.find_element(*responses_position(question_index))

    @allure.step('Скроллим до необходимого элемента')
    def scrolling_to_block_of_elements(self):
        self.waiting_visibility_element(MainPageLocator.Requests[2])
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