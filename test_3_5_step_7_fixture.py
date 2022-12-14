# Отметьте ниже только те тестовые методы, которые будут найдены и выполнены PyTest при запуске следующей команды: 
# pytest -v -m "smoke and not beta_users" test_task_run_1.py

import pytest


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True

"""Маркировка тестов и пропуск тестов

# Запустится только smoke:
@pytest.mark.smoke 
pytest -s -v -m smoke test_fixture.py

# Запуска всех тестов, не отмеченных как smoke:
@pytest.mark.smoke 
pytest -s -v -m "not smoke" test_fixture.py

# Запуск тестов с разными маркировками:
@pytest.mark.smoke
@pytest.mark.regression 
pytest -s -v -m "smoke or regression" test_fixture.py

# Запуск тестов имеющих несколько маркировок:
@pytest.mark.smoke
@pytest.mark.win10 
pytest -s -v -m "smoke and win10" test_fixture.py

# Пропуск тестов:
@pytest.mark.skip 
pytest -s -v  test_fixture.py

# Помечать тест как ожидаемо падающий(пометка:XFAIL):
# упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный
# Когда баг починят, мы это узнаем, так как тест будет отмечен как XPASS
@pytest.mark.xfail 
pytest -rx -v test_fixture.py

# reason - Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rX
@pytest.mark.xfail(reason="fixing this bug right now") 
pytest -rX -v test_fixture.py

# Параметр strict
# Ни XFAIL, ни XPASS по умолчанию не приводят к падению всего набора тестов.
# Но это можно изменить, установив параметру strict значение True:
# В этом случае, если тест будет неожиданно пройден (XPASS),
# то это приведет к падению всего тестового набора
@pytest.mark.xfail(strict=True) 
pytest -rX -v test_fixture.py"""