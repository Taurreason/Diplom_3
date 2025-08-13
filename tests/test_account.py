import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage

from helpers import *
from data import *


@allure.epic("Личный кабинет")
class TestAccount:

    @allure.title("Переход в Личный кабинет после авторизации")
    def test_go_to_account(self, driver, create_user_and_delete):

        account_page = AccountPage(driver)
        login_page = LoginPage(driver)

        account_page.go_to_account()
        email, password, _ = create_user_and_delete
        login_page.login(email, password)      
        
        account_page.go_to_account()
        history_tab = account_page.get_orders_history_tab()
        assert history_tab.is_displayed()

    @allure.title("Переход в раздел История заказов")
    def test_go_to_order_history(self, driver, create_user_and_delete):
   
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)

        account_page.go_to_account()
        email, password, _ = create_user_and_delete
        login_page.login(email, password)

        account_page.go_to_account()
        account_page.go_to_history()

        assert driver.current_url == ORDER_HISTORY_URL

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, create_user_and_delete):
        
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)

        account_page.go_to_account()
        email, password, _ = create_user_and_delete
        login_page.login(email, password)

        account_page.go_to_account()
        account_page.logout()

        assert login_page.is_header_visible()
