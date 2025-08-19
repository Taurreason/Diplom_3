import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    def login(self, email, password):
        self.email_enter(email)
        self.password_enter(password)
        self.login_button_click()
        
    @allure.step('Ввести email пользователя')
    def email_enter(self, email):
        self.set_text_to_element(LoginPageLocators.LOGIN_EMAIL_INPUT, email)

    @allure.step('Ввести пароль пользователя')
    def password_enter(self, password):
        self.set_text_to_element(LoginPageLocators.LOGIN_PASSWORD_INPUT, password)

    @allure.step('Кликнуть по кнопке входа на сайт')
    def login_button_click(self):
        self.check_element_is_clickable(LoginPageLocators.LOGIN_BUTTON)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Получить поле ввода Email на странице логина")
    def get_email_input_field(self):
        return self.find_element_with_wait(LoginPageLocators.LOGIN_HEADER)
    
    @allure.step('Кликнуть по ссылке восстановления пароля')
    def click_to_recovery_password_link(self):
        self.check_element_is_clickable(LoginPageLocators.PASSWORD_RECOVERY_LINK_ON_LOGIN_PAGE)
        self.click_on_element(LoginPageLocators.PASSWORD_RECOVERY_LINK_ON_LOGIN_PAGE)

    @allure.step("Проверяем, что заголовок страницы логина отображается")
    def is_header_visible(self) -> bool:
        return self.element_is_displayed(LoginPageLocators.LOGIN_HEADER)
    