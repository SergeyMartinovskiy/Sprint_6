from selenium.webdriver.common.by import By

class BasePageLocator:
    #Кнопка Заказать сверху
    order_button_high = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    #Кнопка Заказать снизу
    order_button_bottom = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # Кнопка Куки
    button_cookie = (By.XPATH, '//*[@id="rcc-confirm-button"]')