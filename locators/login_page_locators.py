from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_PASSWORD_INPUT = (By.XPATH,'//div[contains(@class, "Auth_login")]//div[contains(@class, "input__container")]//input[@type="password" and @name="Пароль"]')    
    LOGIN_EMAIL_INPUT = (By.XPATH,'//div[contains(@class, "Auth_login")]//div[contains(@class, "input__container")]//input[@type="text" and @name="name"]')
    LOGIN_BUTTON = (By.XPATH, '//form[contains(@class, "Auth_form")]//button[text()="Войти"]')
    PASSWORD_RECOVERY_LINK_ON_LOGIN_PAGE = (By.XPATH,'//a[contains(@class, "Auth_link") and text()="Восстановить пароль"]')
    LOGIN_HEADER = (By.XPATH, '//h2[text()="Вход"]')
    