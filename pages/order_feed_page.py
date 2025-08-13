import allure
import time
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):


    @allure.step('Клик на заказ для открытия попапа с деталями заказа')
    def click_to_order(self):
        self.check_element_is_clickable(OrderFeedPageLocators.SEARCH_MADE_ORDER)
        self.click_on_element(OrderFeedPageLocators.SEARCH_MADE_ORDER)

    @allure.step('Получить элемент заголовка "Cостав"')
    def get_order_composition_title(self):
        return self.find_element_with_wait(OrderFeedPageLocators.ORDER_COMPOSITION_TITLE)

    @allure.step('Проверить открытие модального окна с деталями заказа')
    def get_order_details_text(self):
        return self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_DETAILS_TEXT)

    @allure.step('Проверить наличие номера заказа в ленте')
    def check_order_id_in_feed(self):
        element_text =  self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_ID_IN_FEED)
        return element_text.lstrip('#')

    @allure.step('Получить количество заказов за все время')
    def get_orders_count_all_time(self):
        all_element = self.get_text_from_element(OrderFeedPageLocators.COUNTER_OF_ALL_TIME_IN_FEED)
        return all_element
    
    @allure.step('Получить количество заказов за сегодня')
    def get_orders_count_today(self):
        self.scroll_into_view(OrderFeedPageLocators.COUNTER_TODAY_IN_FEED)
        today_element = self.get_text_from_element(OrderFeedPageLocators.COUNTER_TODAY_IN_FEED)
        return today_element
    
    @allure.step("Получить id заказа")
    def check_order_id(self):
        element_text = self.get_text_from_element(
            OrderFeedPageLocators.ORDER_ID_MODAL
        )
        return element_text
    
    @allure.step("Получить реальный номер заказа из модалки")
    def wait_and_get_order_id(self, timeout=10):
        return self.wait_for_real_order_id(OrderFeedPageLocators.ORDER_ID_MODAL, timeout)

    @allure.step("Дождаться появления номера заказа в колонке 'В работе' и вернуть его")
    def wait_and_get_order_in_progress(self, timeout=30, poll=0.5):
        end = time.time() + timeout
        last_texts = []

        while time.time() < end:
            try:
                items = self.driver.find_elements(*OrderFeedPageLocators.IN_PROGRESS_ITEMS)
                last_texts = [i.text.strip() for i in items if i.text.strip()]
                for text in last_texts:
                    if text.isdigit() and text != "9999":
                        return int(text)  # <-- приводим к int, уберёт ведущие нули
            except Exception:
                pass
            time.sleep(poll)

        raise AssertionError(
            f"Не дождался номера в 'В работе' за {timeout}s. Последний список: {last_texts}"
        )
        