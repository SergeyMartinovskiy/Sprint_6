import allure
import pytest
import data

from Pages.main_page import MainPage


class TestMainPageFAQ:
    @allure.title('Проверка аккордеона FAQ - Вопрос/Ответ')
    @pytest.mark.parametrize('question', data.ANSWERS)
    def test_click_faq_and_get_answer(self, driver, question):
        position, question = question
        home_page = MainPage(driver)
        home_page.click_button_accept_cookie()
        home_page.scrolling_to_block_of_elements()
        home_page.wait_show_up_element()
        home_page.click_and_get_answer(position)
        assert home_page.click_and_get_answer(position).text == question










