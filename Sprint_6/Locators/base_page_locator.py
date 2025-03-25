from selenium.webdriver.common.by import By

class BasePageLocator:
    #Кнопка Заказать сверху
    order_button_high = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    #Кнопка Заказать снизу
    order_button_bottom = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # Кнопка Куки
    button_cookie = (By.XPATH, '//*[@id="rcc-confirm-button"]')
    # Логотип Самоката
    button_logo_samokat = (By.XPATH, "//img[@alt='Scooter']")
    # Логотип Яндекса
    button_logo_yandex = (By.XPATH, "//img[@alt='Yandex']")
    # Закрытие окна в окне поверх Дзена
    exit_button_in_extra_window_dzen = (By.XPATH, './/span[@tabindex = "0"]')
