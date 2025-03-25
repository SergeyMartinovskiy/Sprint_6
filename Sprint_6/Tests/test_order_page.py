import allure
import pytest

from Pages.order_page import OrderPage

class TestOrderPage:
    @allure.title('Заполнение полей формы заказа Самоката')
    @pytest.mark.parametrize('order_button', ['order_button_high', 'order_button_bottom'])
    def test_fill_form_order_page(self, driver, order_button):
        order_page = OrderPage(driver)
        order_page.click_button_accept_cookie()
        order_button_choose = getattr(order_page, order_button)
        order_button_choose()
        order_page.enter_name_in_field()
        order_page.enter_surname_in_field()
        order_page.enter_address_in_field()
        order_page.find_metro_field()
        order_page.choose_metro_station()
        order_page.enter_phone_field()
        order_page.click_continue_button()
        order_page.enter_date_delivery()
        order_page.enter_rental_period()
        order_page.click_order_button()
        order_page.click_button_yes_in_confirm()

        assert order_page.order_confirmed()





