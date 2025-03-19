from selenium.webdriver.common.by import By

class HeaderPageLocator:
    #Логотип Самоката
    button_logo_samokat = (By.XPATH, "//img[@alt='Scooter']")
    # Логотип Яндекса
    button_logo_yandex = (By.XPATH, "//img[@alt='Yandex']")
