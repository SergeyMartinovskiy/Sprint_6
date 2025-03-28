import allure


from pages.main_page import MainPage
from URLS import URL_Scooter, URL_Dzen


class TestRedirects:
    @allure.title('Тест: Переход на страницу Дзена при нажатии на лого Яндекса в заголовке страницы Самокат')
    def test_redirects_yandex(self, driver):
        home_page = MainPage(driver)
        home_page.click_button_accept_cookie()
        home_page.click_logo_yandex()
        home_page.switch_driver()
        home_page.wait_url_until_not_about_blank()
        home_page.get_current_url()
        current_url = home_page.wait_headline_dzen()

        assert 'dzen' in current_url

    @allure.title('Тест: Переход на главную страницу Самоката при нажатии на лого Самоката')
    def test_redirects_scooter(self, driver):
        home_page = MainPage(driver)
        home_page.click_button_accept_cookie()
        home_page.order_button_in_header_click()
        home_page.click_logo_samokat()
        assert URL_Scooter == home_page.get_current_url()






