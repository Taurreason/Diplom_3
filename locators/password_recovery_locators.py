from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:


    # Кнопка "Восстановить" на форме восстановления пароля
    PASSWORD_RECOVERY_SUBMIT_BUTTON = (By.XPATH,
    '//form[contains(@class, "Auth_form")]//button[contains(@class, "button_button") and contains(@class, "button_button_type_primary") and text()="Восстановить"]')
    # Поле ввода нового пароля на странице восстановления
    PASSWORD_RECOVERY_NEW_PASSWORD_INPUT = (By.XPATH, '//div[contains(@class, "input_type_password") and .//label[text()="Пароль"]]')
    # Поле ввода email в фокусе на форме восстановления
    PASSWORD_RECOVERY_EMAIL_INPUT_FOCUSED = (By.XPATH, '//div[contains(@class, "input") and contains(@class, "input_type_text")]//input[@type="text" and @name="name"]')
    # Иконка "Показать пароль" в форме восстановления
    PASSWORD_RECOVERY_SHOW_PASSWORD_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    # Поле ввода нового пароля (в фокусе) в форме восстановления пароля
    PASSWORD_RECOVERY_NEW_PASSWORD_INPUT_FOCUSED = (By.XPATH, '//div[contains(@class, "input_type_password")]//input[@type="password"]')
    # Активное поле ввода нового пароля
    PASSWORD_RECOVERY_PASSWORD_FIELD_ACTIVE = (By.XPATH,  '//label[text()="Пароль"]/parent::div[contains(@class,''"input_status_active")]')
    # Неактивное поле ввода пароля (скрытый пароль)
    PASSWORD_RECOVERY_PASSWORD_FIELD_INACTIVE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class,''"input_type_password")]')
    # Лейбл поля ввода кода из письма при восстановлении пароля
    PASSWORD_RECOVERY_CODE_LABEL = (By.XPATH,'//label[contains(@class, "input__placeholder") and text()="Введите код из письма"]')
