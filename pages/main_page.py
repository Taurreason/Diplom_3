import allure
from selenium.common.exceptions import ElementClickInterceptedException

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import *
import time


class MainPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    @allure.step("Переход в Конструктор")
    def go_to_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход в Ленту заказов")
    def go_to_feed(self):
        # подстраховка: дождаться, что оверлей и контейнер модалки исчезли
        try:
            self.wait_gone(MainPageLocators.MODAL_OVERLAY, timeout=2)
            self.wait_invisible(MainPageLocators.MODAL_CONTAINER, timeout=2)
        except Exception:
            pass
        self.check_element_is_clickable(MainPageLocators.FEED_BUTTON_ON_MAIN_PAGE)
        self.click_on_element(MainPageLocators.FEED_BUTTON_ON_MAIN_PAGE)

    @allure.step("Собрать заказ и нажать «Оформить»")
    def create_order(self) -> None:
        self.drag_and_drop_bun()
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Открыть модалку с деталями ингредиента")
    def get_ingredient_details_modal(self):
        self.check_element_is_clickable(MainPageLocators.INGREDIENT_BUN)
        self.click_on_element(MainPageLocators.INGREDIENT_BUN)

    @allure.step("Закрыть модалку деталей ингредиента")
    def close_ingredient_modal(self):
        self.check_element_is_clickable(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        self.click_on_element(MainPageLocators.INGREDIENT_MODAL_CLOSE)

    @allure.step('Получить заголовок модалки "Детали ингредиента"')
    def get_ingredient_detail_header(self):
        return self.find_element_with_wait(MainPageLocators.HEADER_DETAIL_INGREDIENT)
    
    @allure.step('Клик по первому ингредиенту в разделе "Булки"')
    def click_first_bun_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT_BUN)

    @allure.step("Проверить колличество ингредиентов до добавления в корзину")
    def check_count_before_ingredient_added(self):
        return int(self.get_text_from_element(MainPageLocators.SEARCH_COUNTER_INGREDIENT_NOT_ADDED))
    
    @allure.step("Проверить, что модалка с деталями закрылась")
    def check_ingredient_details_modal_closed(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_SAUCES_SECTION)

    @allure.step("Получить текст заголовка модалки подтверждения заказа")
    def check_order_id_text(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_ORDER_ID_TEXT)

    @allure.step("Получить текущее значение счётчика ингредиента")
    def get_ingredient_counter_value(self):
        """
        Считает число из любого видимого счётчика. Если на карточке
        нет счётчика — возвращает 0.
        """
        # 1) пробуем универсальный локатор (любое число)
        try:
            text = self.get_text_from_element(MainPageLocators.COUNTER_ANY_NUM)
            return int(text) if text.isdigit() else 0
        except Exception:
            # 2) совместимость со старыми локаторами (0/2)
            for loc in (
                MainPageLocators.SEARCH_COUNTER_INGREDIENT_ADDED,
                MainPageLocators.SEARCH_COUNTER_INGREDIENT_NOT_ADDED,
            ):
                try:
                    text = self.get_text_from_element(loc)
                    if text and text.isdigit():
                        return int(text)
                except Exception:
                    continue
        return 0
    
    @allure.step("Проверить количество ингредиентов после добавления в корзину")
    def check_count_after_ingredient_added(self):
        return self.get_ingredient_counter_value()
       
    @allure.step("Дождаться увеличения счётчика")
    def wait_counter_increase(self, before: int, timeout=10):
        end_time = time.time() + timeout
        while time.time() < end_time:
            current = self.get_ingredient_counter_value()
            if current > before:
                return
            time.sleep(0.2)

    @allure.step("Закрыть модалку 'Заказ оформлен'")
    def close_new_order_modal(self):
        # self.find_element_with_wait(
        #     MainPageLocators.SEARCH_CLOSE_MADE_ORDER_BUTTON
        # )
        self.js_click(MainPageLocators.SEARCH_CLOSE_MADE_ORDER_BUTTON)

    @allure.step("Клик по кнопке «Войти в аккаунт» на главной")
    def click_login_button(self):
        self.check_element_is_clickable(MainPageLocators.LOGIN_BUTTON_AUTH_MAINPAGE)
        self.click_on_element(MainPageLocators.LOGIN_BUTTON_AUTH_MAINPAGE)

    @allure.step("Клик по ссылке перехода в Конструктор (с подстраховкой)")
    def click_constructor_link(self):
        element = self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_BUTTON)
        # Прокрутка элемента в видимую область
        self.scroll_into_view_js(element)

        try:
            if element.is_displayed():
                self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        except ElementClickInterceptedException:
            # Если элемент не кликается, можно подождать и повторить
            time.sleep(1)
            try:
                self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
            except ElementClickInterceptedException:
                self.js_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перетащить первую булку в корзину конструктора")
    def drag_and_drop_bun(self):
            self.drag_and_drop(MainPageLocators.INGREDIENT_FIRST_BUN, MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step("Проверяем, что открыт Конструктор")
    def is_constructor_header_visible(self) -> bool:
        return self.element_is_displayed(MainPageLocators.HEADER_CONSTRUCTOR)

    @allure.step("Проверяем, что открыта Лента заказов")
    def is_feed_header_visible(self) -> bool:
        return self.element_is_displayed(MainPageLocators.HEADER_FEED)

    @allure.step('Проверяем, что открыта модалка "Детали ингредиента"')
    def is_ingredient_detail_header_visible(self) -> bool:
        return self.element_is_displayed(MainPageLocators.HEADER_DETAIL_INGREDIENT)
    
    @allure.step('Проверяем, что видна подпись "идентификатор заказа" в модалке')
    def is_order_id_label_visible(self) -> bool:
        return self.element_is_displayed(MainPageLocators.ORDER_ID_LABEL)
    