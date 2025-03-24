from selenium.webdriver.common.by import By

class OrderPageLocator:

    # Поле имя
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    # Поле фамилия
    surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Поле адрес
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Поле выбора станции метро
    box_set_metro = (By.XPATH, "//div[@class='select-search']")
    #Сокольники
    set_metro_one = (By.XPATH, "//input[@value='Сокольники']")
    # Черкизовская
    set_metro_two = (By.XPATH, "//input[@value='Черкизовская']")
    # Поле ввода номера телефона
    phone_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка далее
    button_next = (By.XPATH, "//button[contains(text(),'Далее')]")
    # Поле ввода даты
    date_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Поле выбора срока аренды
    rent_time_field = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    # Срок аренды 1 день
    rent_time_one_day = (By.XPATH, './/div[text()="сутки"]')
    # Срок аренды 2 дня
    rent_time_two_days = (By.XPATH, './/div[text()="двое суток"]')
    # Цвет самоката - черный
    black_color_scooter = (By.XPATH, '//input[@id="black"]')
    # Цвет самоката - серый
    grey_color_scooter = (By.XPATH, '//input[@id="grey"]')
    # Кнопка заказать
    button_order = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    # Кнопка Да (подтверждение заказа)
    button_yes = (By.XPATH, '//button[contains(text(),"Да")]')

    # Текст Заказ Оформлен
    order_booking = (By.XPATH,'//div[@class="Order_ModalHeader__3FDaJ"]')

