# Arslanova_skypro_Python_DZ
## Мои домашние задания в блоке "Автоматизация тестирования на Python"

Ветка lesson1 - домашнее и тренировочное задание №1 урока "Знакомство с языком Python"

Ветка lesson2 - домашнее задание №2 урока "Базовые алгоритмы на Python"

Ветка lesson3 - домашнее задание №3 урока "ООП в Python"

Ветка lesson4 - домашнее задание №4 урока "Знакомство с Pytest"

Ветка lesson5 - домашнее задание №5 урока "Учимся писать автоматизированные UI-тесты"

Ветка lesson6 - домашнее задание №6 урока "Расширенные практики Selenium"

Ветка lesson6K - домашнее задание №7 урока "Контрольная работа"

Ветка lesson7 - домашнее задание №8 урока "PageObject"

Ветка lesson8 - домашнее задание №8 урока "Знакомство с библиотекой Requests"

Ветка lesson10 - домашнее задание №8 урока "Отчетность в Allure"




## Инструкция для работы с веткой lesson10
Для запуска тестов сперва открываем "Terminal". Следующие шаги выполняем в терминале (при учете того, что все настройки и приложения были настроены):
1. Сперва переходим в папку "lesson_10" командой "cd lesson_10"
2. Дальше вводим команду "pytest --alluredir=./allure_result". Т.е. результаты тестов будут загружены в созданную папку "allure_result" в текущей папке "lesson_10". Папка "allure_result" будет автоматически создана сама.
3. Дальше вводим команду "allure serve allure_result". Автоматически откроется страница с отчетом.

Следующие шаги выполняем в отчете Allure:
1. В открытом отчете на главной странице "Overview" в блоке "Allure Report" можно посмотреть дату и время выполнения тестов. Там также можно увидеть общую ситуацию с выполнением всех тестов, а именно какой процент успешных тестов и общое количество тестов.
2. На главной странице "Overview" есть блок "Suites", где можно также увидеть разбивку на количество тестов в каждом сьюте. В этом блоке если нажать на какую-нибудь строку, то можно упасть на иерархию сьюетов с тестами. При раскрытии уровней и нажатия на название теста можно увидеть информацию по тесту: шаги, подшаги, описание теста, критичность, общее время выполнения теста и время каждого шага.
3. На главной странице "Overview" есть блок "Features by stories" где можно также увидеть разбивку на количество тестов в каждом эпике. В этом блоке если нажать на какую-нибудь строку, то можно упасть на иерархию: эпик - фича - аннотация - тесты. При раскрытии уровней и нажатия на название теста можно увидеть информацию по тесту: шаги, подшаги, описание теста, критичность, общее время выполнения теста и время каждого шага.
4. Также если есть не успешные тесты, то можно увидеть по ним информацию в блоке "Categories" (проблема в тесте или дефект в проверяемой веб-странице)
5. Информацию из блоков "Suites" и "Categories" можно также увидеть на соответствующих вкладках "Suites" и "Categories".
6. На вкладке "Graphs" можно увидеть результаты выполнения тестов графически в разрезе разных атрибутов.
7. Информацию из блока "Features by stories" можно также увидеть на вкладке "Behaviors".
