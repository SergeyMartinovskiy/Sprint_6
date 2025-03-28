from selenium.webdriver.common.by import By


class MainPageLocator:
    Requests = [
            (By.XPATH, '//div[@id="accordion__heading-0"]'),
            (By.XPATH, "//div[@id='accordion__heading-1']"),
            (By.XPATH, "//div[@id='accordion__heading-2']"),
            (By.XPATH, "//div[@id='accordion__heading-3']"),
            (By.XPATH, "//div[@id='accordion__heading-4']"),
            (By.XPATH, "//div[@id='accordion__heading-5']"),
            (By.XPATH, "//div[@id='accordion__heading-6']"),
            (By.XPATH, "//div[@id='accordion__heading-7']")
        ]

    Responses = [
            (By.XPATH, '//p[contains(text(),"Сутки — 400 рублей. Оплата курьеру — наличными или картой")]'),
            (By.XPATH, '//p[contains(text(),"Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")]'),
            (By.XPATH, '//p[contains(text(),"Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")]'),
            (By.XPATH, '//p[contains(text(),"Только начиная с завтрашнего дня. Но скоро станем расторопнее.")]'),
            (By.XPATH, '//p[contains(text(),"Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")]'),
            (By.XPATH, '//p[contains(text(),"Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.")]'),
            (By.XPATH, '//p[contains(text(),"Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.")]'),
            (By.XPATH, '//p[contains(text(),"Да, обязательно. Всем самокатов! И Москве, и Московской области.")]')
        ]

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
