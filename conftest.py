import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, fr, ru, en, etc.")


@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра language из командной строки
    user_language = request.config.getoption("language")
    
    # Инициализируем опции Chrome
    options = Options()
    
    # Устанавливаем язык браузера
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language
    })
    
    # Инициализируем браузер с указанными опциями
    print(f"\nStarting browser with language: {user_language}")
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    # Закрываем браузер после завершения теста
    print("\nClosing browser...")
    browser.quit()