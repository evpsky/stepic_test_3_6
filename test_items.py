import time




class TestFindButton():
    def test_find_add_to_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        # Устанавливаем время ожидания
        time.sleep(30)
        # Ищем кнопку на станице
        add_to_basket_button = browser.find_element_by_css_selector(".btn-primary")
        # с помощью assert проверяем, что кнопка "Добавить в корзину" есть на странице
        assert add_to_basket_button, "Add to basket button is missed"

