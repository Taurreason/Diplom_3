from selenium.webdriver.common.by import By

class OrderFeedPageLocators:


    SEARCH_MADE_ORDER = (By.XPATH, '//li[.//a[contains(@href, "/feed/") and .//p[starts-with(text(), "#")] and .//h2[contains(@class, "text_type_main-medium")]]]')
    SEARCH_ORDER_DETAILS_TEXT = (By.XPATH, '//p[contains(@class, "text") and contains(@class, "text_type_main-medium")'
                                           ' and contains(@class, "mb-8") and text()="Cостав"]')
    SEARCH_ORDER_ID_IN_FEED = (By.XPATH,  '//ul/li//p[contains(@class, "text") and contains(@class, "text_type_digits-default")]')
    COUNTER_OF_ALL_TIME_IN_FEED = (By.XPATH,
                                          '//div[p[contains(@class, "text_type_main-medium") and text()="Выполнено за все время:"]]/p[contains(@class, "OrderFeed_number")]')
    COUNTER_TODAY_IN_FEED = (By.XPATH, '//div[p[contains(@class, "text_type_main-medium") and text()="Выполнено за сегодня:"]]/p[contains(@class, "OrderFeed_number")]')
    ORDER_ID_MODAL = (By.XPATH,'.//h2[contains(@class, "Modal_modal__title_shadow")]')
    IN_PROGRESS_ITEMS = (By.CSS_SELECTOR,"ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li")
    ORDER_COMPOSITION_TITLE = (By.XPATH, '//p[@class="text text_type_main-medium mb-8" and text()="Cостав"]')
