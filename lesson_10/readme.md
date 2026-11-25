# Автотесты: калькулятор и SauceDemo

UI-тесты на Python + Selenium + Pytest. Отчёты формируются через Allure Report.

Проект содержит два набора тестов:
- `lesson_10/Calc_test/` — тесты медленного калькулятора
- `lesson_10/Shop_test/` — тесты оформления заказа на saucedemo.com

## Запуск тестов с формированием отчёта

**Выполните из корня проекта**

pytest --alluredir=allure-results

Тесты запустятся, а результаты сохранятся в папку allure-results.

**Чтобы запустить только один набор, укажите папку**

pytest lesson_10/Calc_test --alluredir=allure-results
pytest lesson_10/Shop_test --alluredir=allure-results

### Просмотр отчёта ###

**После выполнения тестов в терминале прописать**

allure serve allure-results
Команда соберёт отчёт из папки allure-results и откроет его в браузере.