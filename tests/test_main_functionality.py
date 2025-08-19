import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.epic("Проверка основного функционала")
class TestMainFunctionality:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_feed()
        main_page.go_to_constructor()

        assert main_page.is_constructor_header_visible()


    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_feed()
        
        assert main_page.is_feed_header_visible()

    @allure.title("Открытие всплывающего окна ингредиента")
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_bun_ingredient()

        assert main_page.is_ingredient_detail_header_visible()

    @allure.title("Закрытие всплывающего окна ингредиента")
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.get_ingredient_details_modal()
        main_page.close_ingredient_modal()

        assert main_page.check_ingredient_details_modal_closed() == "Соусы"

    @allure.title("Добавление ингредиента увеличивает счётчик")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        before = main_page.check_count_before_ingredient_added()
        main_page.drag_and_drop_bun()
        
        main_page.wait_counter_increase(before)
        after = main_page.check_count_after_ingredient_added()
        assert after > before

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_logged_in_user_can_order(self, driver, create_user_and_delete):
        email, password, _ = create_user_and_delete

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.click_login_button()

        login_page.login(email, password)
        main_page.create_order()
        
        assert main_page.is_order_id_label_visible()
