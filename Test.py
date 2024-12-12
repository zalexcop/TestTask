from playwright.sync_api import sync_playwright  # type: ignore

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Запуск браузера
    page = browser.new_page() # Открытие пустой вкладки 
    page.goto('https://www.google.com')  # Переход на страницу Google
    page.fill('textarea', 'Тест') # Заполняем поисковую строку текстом запроса
    page.press('textarea', 'Enter') # Нажимаем кнопку поиска
    page.wait_for_selector('h3') # Ожидаем загрузки страницы
    page.screenshot(path='screenshots/google_search_result.png') # Делаем скриншот
    browser.close() #