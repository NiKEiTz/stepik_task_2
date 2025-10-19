import time
from selenium.webdriver.common.by import By



def test_add_to_cart_button_presence(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Даем странице время для загрузки
    time.sleep(5)
    
    # Ищем кнопку добавления в корзину через find_element
    # Если кнопка не найдена, выбросится исключение NoSuchElementException
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    # Проверяем, что кнопка отображается на странице
    assert add_to_cart_button.is_displayed(), "Add to cart button is not visible"
    
    # Дополнительная проверка: убедимся, что у кнопки правильный тип
    button_type = add_to_cart_button.get_attribute("type")
    assert button_type == "submit" or button_type == "button", \
        f"Button has unexpected type: {button_type}"