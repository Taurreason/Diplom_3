import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


@allure.epic("Раздел 'Лента заказов'")
class TestOrderFeed:

    @allure.title("Открытие деталей заказа по клику")
    def test_order_details_popup(self, driver):

        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)
        main_page.go_to_feed()

        feed_page.click_to_order()

        composition_header = feed_page.get_order_composition_title()
        assert composition_header.is_displayed()


    @allure.title("Заказ из истории виден в ленте заказов")
    def test_user_order_visible_in_feed(self, driver, create_user_and_delete):
 
        email, password, _ = create_user_and_delete
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_login_button()
        login_page.login(email, password)
        account_page.close_modal_for_ff()
        main_page.create_order()
        main_page.close_new_order_modal()

        account_page.go_to_account()
        account_page.go_to_history()

        history_order_id = account_page.get_order_id_in_history()
        main_page.go_to_feed()
        feed_order_id = order_feed_page.check_order_id_in_feed()

        assert int(history_order_id) == int(feed_order_id)

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_total_done_counter_increases(self, driver, create_user_and_delete):
        
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_login_button()
        email, password, _ = create_user_and_delete
        login_page.login(email, password)
        account_page.close_modal_for_ff()
        account_page.close_modal_for_chrome()
        main_page.go_to_feed()
        before_order = order_feed_page.get_orders_count_all_time()

        main_page.click_constructor_link()
        main_page.create_order()
        main_page.close_new_order_modal()
        account_page.close_modal_for_ff()
        account_page.close_modal_for_chrome()
        main_page.go_to_feed()
        after_order = order_feed_page.get_orders_count_all_time()        

        assert int(before_order) < int(after_order)

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_done_counter_increases(self, driver, create_user_and_delete):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)

        main_page.click_login_button()
        email, password, _ = create_user_and_delete
        login_page.login(email, password)
        account_page.close_modal_for_ff()
        account_page.close_modal_for_chrome()
        main_page.go_to_feed()
        before_order = order_feed_page.get_orders_count_today()

        main_page.click_constructor_link()
        main_page.create_order()
        main_page.close_new_order_modal()
        account_page.close_modal_for_ff()
        account_page.close_modal_for_chrome()
        main_page.go_to_feed()
        after_order = order_feed_page.get_orders_count_today()

        assert int(before_order) < int(after_order)

    @allure.title("Номер нового заказа появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, driver, create_user_and_delete):
        
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_login_button()
        email, password, _ = create_user_and_delete

        login_page.login(email, password)
        account_page.close_modal_for_ff()

        main_page.create_order()
        id_in_modal = order_feed_page.wait_and_get_order_id()
        main_page.close_new_order_modal()

        main_page.go_to_feed()
        id_in_progress = order_feed_page.wait_and_get_order_in_progress()

        assert id_in_modal == id_in_progress

