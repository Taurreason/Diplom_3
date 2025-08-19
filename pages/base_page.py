import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликабельность элемента')
    def check_element_is_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.find_element_with_wait(locator)
    
    @allure.step('Отображение элемента')
    def element_is_displayed(self, locator):
        return self.find_element_with_wait(locator).is_displayed()
    
    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Добавление текста в элемент')   
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)
    
    @allure.step('Ожидание исчезновения элемента из видимости')
    def wait_invisible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
  
    @allure.step("Дождаться, пока номер заказа в модалке станет реальным (не 9999)")
    def wait_for_real_order_id(self, locator, timeout=30, poll=0.5):
        end = time.time() + timeout
        while time.time() < end:
            value = self.get_text_from_element(locator).strip()
            if value.isdigit() and value != "9999":
                return int(value)  # уберёт нули
            time.sleep(poll)
        raise AssertionError("Не дождался реального номера заказа")

    def scroll_into_view(self, locator):
        el = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        return el

    def _sleep(self, sec=0.2):
        time.sleep(sec)

    @allure.step('Ожидание для закрытия скрытого мадального окна')
    def wait_for_modal_closed(self, driver, locator):
        wait = WebDriverWait(driver, 2)
        try:
            return wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            print("Modal did not close within the expected time")

    @allure.step('Клик по кнопке для скрытых модальных окон')
    def js_click(self, target):
        if isinstance(target, tuple):
            el = self.find_element_with_wait(target)
        elif isinstance(target, WebElement):
            el = target
        else:
            raise TypeError("js_click expects locator or WebElement")
        self.driver.execute_script("arguments[0].click();", el)

    @allure.step("Проверяем наличие элемента в DOM")
    def is_present(self, locator, timeout=0):
        try:
            if timeout:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
                return True
            return len(self.driver.find_elements(*locator)) > 0
        except TimeoutException:
            return False

    @allure.step('Скролл до элемента')
    def scroll_into_view_js(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Ожидаем исчезновения элемента из DOM")
    def wait_gone(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.find_elements(*locator)) == 0
        )

    def drag_and_drop(self, source_locator, target_locator):
        src = self.find_element_with_wait(source_locator)
        dst = self.find_element_with_wait(target_locator)
        js_script = """
                    function simulateDragDrop(sourceNode, targetNode) {
                        var EVENT_TYPES = {
                            DRAG_END: 'dragend',
                            DRAG_START: 'dragstart',
                            DROP: 'drop',
                            DRAG_OVER: 'dragover'
                        };
                        function createCustomEvent(type) {
                            var event = new CustomEvent("CustomEvent");
                            event.initCustomEvent(type, true, true, null);
                            event.dataTransfer = {
                                data: {},
                                setData: function(type, val) {
                                    this.data[type] = val;
                                },
                                getData: function(type) {
                                    return this.data[type];
                                }
                            };
                            return event;
                        }
                        function dispatchEvent(node, type, event) {
                            if (node.dispatchEvent) {
                                return node.dispatchEvent(event);
                            }
                            if (node.fireEvent) {
                                return node.fireEvent("on" + type, event);
                            }
                        }
                        var event = createCustomEvent(EVENT_TYPES.DRAG_START);
                        dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event);
                        var dropEvent = createCustomEvent(EVENT_TYPES.DROP);
                        dropEvent.dataTransfer = event.dataTransfer;
                        dispatchEvent(targetNode, EVENT_TYPES.DROP, dropEvent);
                        var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END);
                        dragEndEvent.dataTransfer = event.dataTransfer;
                        dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent);
                    }
                    simulateDragDrop(arguments[0], arguments[1]);
                """
        self.driver.execute_script(js_script, src, dst)
