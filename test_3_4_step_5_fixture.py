import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")

#scope='function'
#Выполняется один раз для каждой функции теста. Часть setup запускается перед каждым тестом с помощью fixture. 
#Часть teardown запускается после каждого теста с использованием fixture. 
#Это область используемая по умолчанию, если параметр scope не указан.

#scope='class'
#Выполняется один раз для каждого тестового класса, независимо от количества тестовых методов в классе.

#scope='module'
#Выполняется один раз для каждого модуля, независимо от того, 
#сколько тестовых функций или методов или других фикстур при использовании модуля.

#scope='session'
#Выполняется один раз за сеанс. Все методы и функции тестирования, 
#использующие фикстуру области сеанса, используют один вызов setup и teardown.