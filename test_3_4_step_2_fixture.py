from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

#Запускает setup перед всеми тестами, после запускает teardown
class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite (setup_class)..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite (teardown_class)..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

#Запускает setup перед каждым тестом, после каждого теста запускает teardown
class TestMainPage2():

    def setup_method(self):
        print("start browser for test (setup_method)..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test (teardown_method)..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

