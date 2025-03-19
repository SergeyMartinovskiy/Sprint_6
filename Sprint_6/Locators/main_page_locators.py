from selenium.webdriver.common.by import By

class MainPageLocator:

    #FAQ. Сколько это стоит? И как оплатить?
    faq_price = (By.XPATH, '//div[@id="accordion__heading-24"]')
    faq_price_answer = (By.XPATH,"//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]")
    #FAQ.Хочу сразу несколько самокатов! Так можно?
    faq_number_of_scooter = (By.XPATH, "//div[@id='accordion__heading-25']")
    faq_number_of_scooter_answer = (By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — "
                                              "один самокат. Если хотите покататься с друзьями, можете "
                                              "просто сделать несколько заказов — один за другим.')]")
    #FAQ. Как рассчитывается время аренды?
    faq_rent_time = (By.XPATH, "//div[@id='accordion__heading-26']")
    faq_rent_time_answer = (By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привозим "
                                            "самокат 8 мая в течение дня. Отсчёт времени аренды начинается "
                                             "с момента, когда вы оплатите заказ курьеру. Если мы привезли "
                                             "самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]")
    # FAQ. Можно ли заказать самокат прямо на сегодня?
    faq_order_today = (By.XPATH, "//div[@id='accordion__heading-27']")
    faq_order_today_answer = (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]")
    # FAQ. Можно ли продлить заказ или вернуть самокат раньше?
    faq_extend_order = (By.XPATH, "//div[@id='accordion__heading-28']")
    faq_extend_order_answer = (By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное "
                                         "— всегда можно позвонить в поддержку по красивому номеру 1010.')]")
    # FAQ. Вы привозите зарядку вместе с самокатом?
    faq_charge_scooter = (By.XPATH, "//div[@id='accordion__heading-29']")
    faq_charge_scooter_answer = (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. "
                                           "Этого хватает на восемь суток — даже если будете кататься без передышек "
                                           "и во сне. Зарядка не понадобится.')]")
    # FAQ. Можно ли отменить заказ?
    faq_cancel_order =  (By.XPATH, "//div[@id='accordion__heading-30']")
    faq_cancel_order_answer = (By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, "
                                         "объяснительной записки тоже не попросим. Все же свои.')]")
    # FAQ. Я жизу за МКАДом, привезёте?
    faq_faraway_delivery = (By.XPATH, "//div[@id='accordion__heading-31']")
    faq_faraway_delivery_answer = (By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, "
                                             "и Московской области.')]")