import allure
import pytest

from Pages.main_page import ANSWERS, MainPage
from conftest import driver

class TestMainPageFAQ:
    @allure.title('Проверка аккордеона FAQ - Вопрос/Ответ')
    @pytest.mark.parametrize('question', ANSWERS)
    def test_click_faq_and_get_answer(self, driver, question):
        question_index, expected_answers = question
        home_page = MainPage(driver)
        home_page.click_button_accept_cookie()
        home_page.scrolling_to_block_of_elements()
        home_page.wait_show_up_element()

        actuaul_answers = home_page.click_and_get_answer(question_index).text
        assert actuaul_answers == expected_answers










