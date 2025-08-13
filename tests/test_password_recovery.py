import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage
from helpers import *


@allure.epic("Восстановление пароля")
@allure.feature("Восстановление пароля")
class TestResetPassword:


    @allure.title("Проверяем, что пароль можно восстановить")
    def test_password_recovery(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_login_button()    
        login_page.click_to_recovery_password_link()

        password_recovery_page.enter_email_to_recovery_password()
        password_recovery_page.click_password_recovery_submit_button()

        assert password_recovery_page.is_password_recovery_code_label_displayed()

    @allure.title("Проверяем видимость пароля")
    def test_password_is_visible(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_login_button()
        login_page.click_to_recovery_password_link()

        password_recovery_page.enter_email_to_recovery_password()
        password_recovery_page.click_password_recovery_submit_button()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()

        assert password_recovery_page.check_password_visible()

    @allure.title("Проверяем, что вводимый пароль скрывается")
    def test_password_is_hidden(self, driver):
        main_page = MainPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        login_page = LoginPage(driver)

        main_page.click_login_button()     
        login_page.click_to_recovery_password_link()

        password_recovery_page.enter_email_to_recovery_password()
        password_recovery_page.click_password_recovery_submit_button()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()
        password_recovery_page.click_password_make_visible_hidden()

        assert password_recovery_page.check_password_hidden()
