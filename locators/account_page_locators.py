from selenium.webdriver.common.by import By

class AccountPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/ancestor::a[1]")
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(@class, "Account_button__") and text()="Выход"]')
    MODAL_FF = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay__']")
    MODAL_CLOSE_FOR_FF = (By.XPATH, '//button[@class="close-modal-button"]')
    HEADER_ACCOUNT_PAGE = (By.XPATH, '//a[contains(@class, "AppHeader_header__link")]')
    ORDERS_HISTORY = (By.XPATH, '//li[contains(@class, "Account_listItem")]/a[contains(@class, "Account_link") and contains(text(), "История заказов")]')
    ORDER_ID_IN_HISTORY = (By.XPATH, './/p[contains(@class, "text") and contains(@class, "text_type_digits-default")]')
