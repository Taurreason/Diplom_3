import allure

from helpers import *
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators

class PasswordRecoveryPage(BasePage):

    @allure.step('Ввести email, на который придет код для восстановления пароля')
    def enter_email_to_recovery_password(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.PASSWORD_RECOVERY_EMAIL_INPUT_FOCUSED)
        self.click_on_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_EMAIL_INPUT_FOCUSED)
        self.set_text_to_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_EMAIL_INPUT_FOCUSED, generate_random_email(5))
        self.click_on_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_EMAIL_INPUT_FOCUSED)

    @allure.step('Проверить наличие поля для ввода пароля на странице восстановления пароля')
    def check_password_recovery_field(self):
        return self.get_text_from_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_NEW_PASSWORD_INPUT)

    @allure.step('Скрыть вводимый пароль')
    def click_password_make_visible_hidden(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.PASSWORD_RECOVERY_SHOW_PASSWORD_ICON)
        self.click_on_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_SHOW_PASSWORD_ICON)

    @allure.step('Ввести новый пароль')
    def enter_new_password(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.PASSWORD_RECOVERY_NEW_PASSWORD_INPUT_FOCUSED)
        self.click_on_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_NEW_PASSWORD_INPUT_FOCUSED)
        self.set_text_to_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_NEW_PASSWORD_INPUT_FOCUSED, generate_random_string(9))

    @allure.step('Проверить, что пароль скрыт')
    def check_password_visible(self):
        return self.element_is_displayed(PasswordRecoveryLocators.PASSWORD_RECOVERY_PASSWORD_FIELD_ACTIVE)

    @allure.step('Проверить, что пароль виден')
    def check_password_hidden(self):
        return self.element_is_displayed(PasswordRecoveryLocators.PASSWORD_RECOVERY_PASSWORD_FIELD_INACTIVE)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_password_recovery_submit_button(self):
        self.click_on_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_SUBMIT_BUTTON)

    @allure.step("Проверить, что отображается поле 'Введите код из письма'")
    def is_password_recovery_code_label_displayed(self) -> bool:
        return self.element_is_displayed(PasswordRecoveryLocators.PASSWORD_RECOVERY_CODE_LABEL)
    