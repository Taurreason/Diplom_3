from selenium.webdriver.common.by import By

class MainPageLocators:
    INGREDIENT_BUN = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    HEADER_DETAIL_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[contains(@class, "AppHeader_header__") and .//p[contains(text(), "Конструктор")]]')
    HEADER_CONSTRUCTOR = (By.XPATH, "//h1[text()='Соберите бургер']")
    HEADER_FEED = (By.XPATH, "//h1[text()='Лента заказов']")
    INGREDIENT_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # # --- новый универсальный счётчик ---
    # COUNTER_ANY_NUM = (By.XPATH, '//div[contains(@class,"counter_counter__") and contains(@class,"counter_default__")]//p[contains(@class,"counter_counter__num__")]')

    SEARCH_COUNTER_INGREDIENT_NOT_ADDED = (By.XPATH, '//div[contains(@class, "counter_counter__") and contains(@class, "counter_default__")]/p[contains(@class, "counter_counter__num__") and text()="0"]')
    SEARCH_COUNTER_INGREDIENT_ADDED = (By.XPATH, '//div[contains(@class, "counter_counter__") and contains(@class, "counter_default__")]/p[contains(@class, "counter_counter__num__") and text()="2"]')

    SEARCH_SAUCES_SECTION = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Соусы"]')

    SEARCH_ORDER_ID_TEXT = (By.XPATH, '//p[contains(text(), "идентификатор заказа")]')

    LOGIN_BUTTON_AUTH_MAINPAGE = (By.XPATH, '//section[2]//button[contains(text(), "Войти в аккаунт")]')
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay__']")
    FEED_BUTTON_ON_MAIN_PAGE = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href="/feed" and .//p[contains(text(), "Лента Заказов")]]')
    SEARCH_CLOSE_MADE_ORDER_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    MODAL_CONTAINER = (By.CSS_SELECTOR, "div[class*='Modal_modal__container']")
    INGREDIENT_FIRST_BUN = (By.XPATH, '//ul[contains(@class, "BurgerIngredients")][1]/a[contains(@class, "BurgerIngredient")][1]')
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    ORDER_ID_LABEL = (By.XPATH,
        '//p[contains(@class,"text_type_main-medium") and contains(@class,"mb-15")'
        ' and contains(normalize-space(.),"идентификатор заказа")]')
    