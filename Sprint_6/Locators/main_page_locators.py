from selenium.webdriver.common.by import By
from Locators.base_page_locator import BasePageLocator

class MainPageLocator(BasePageLocator):
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
