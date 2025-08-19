import allure
import data
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators

class AccountPage(BasePage):


    @allure.step("Клик по кнопке перехода в личный кабинет пользователя")
    def go_to_account(self):
        # подстраховка: дождаться, что оверлей и контейнер модалки исчезли
        try:
            self.wait_gone(MainPageLocators.MODAL_OVERLAY, timeout=5)
            self.wait_invisible(MainPageLocators.MODAL_CONTAINER, timeout=5)
        except Exception:
            pass

        # кликаем именно по <a>, не по <p>
        try:
            self.click_on_element(AccountPageLocators.ACCOUNT_BUTTON)
        except Exception:
            # фоллбэк — JS клик
            self.js_click(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step('Перейти в раздел истории заказов пользователя')
    def go_to_history(self):
        self.check_element_is_clickable(AccountPageLocators.ORDERS_HISTORY)
        self.click_on_element(AccountPageLocators.ORDERS_HISTORY)

    @allure.step("Получить элемент вкладки 'История заказов'")
    def get_orders_history_tab(self):
        return self.find_element_with_wait(AccountPageLocators.ORDERS_HISTORY)
    
    @allure.step('Выйти из аккаунта пользователя')
    def logout(self):
        self.click_on_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Получить id заказа из истории заказов в профиле пользователя')
    def get_order_id_in_history(self):
        self.element_is_displayed(AccountPageLocators.ORDER_ID_IN_HISTORY)
        element_text =  self.get_text_from_element(AccountPageLocators.ORDER_ID_IN_HISTORY)
        return element_text.lstrip('#')

    @allure.step('Закрыть скрытое модальное окно')
    def close_modal(self):
        try:
            self.find_element_with_wait(AccountPageLocators.MODAL_FF)
            if self.element_is_displayed(AccountPageLocators.MODAL_FF):
                close_button = self.find_element_with_wait(AccountPageLocators.MODAL_CLOSE_FOR_FF)
                self.click_on_element(close_button)
                self.wait_for_modal_closed(self.driver, AccountPageLocators.HEADER_ACCOUNT_PAGE)
        except Exception as e:
            print(f"Error closing modal: {e}")

    @allure.step('Закрыть скрытое модальное окно в firefox')
    def close_modal_for_ff(self):
        if data.DRIVER_NAME == data.browser_firefox:
            self.close_modal()

    @allure.step('Закрыть модальное окно в chrome')
    def close_modal_for_chrome(self):
        if data.DRIVER_NAME == data.browser_chrome:
            self.close_modal()
            