from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 

try:
    #Открыть страницу http://suninjuly.github.io/file_input.html.
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    #Заполнить текстовые поля: имя, фамилия, email
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Имя")

    first = browser.find_element(By.NAME, "lastname")
    first.send_keys("Фамилия")

    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("test@mail.com")

    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    #Нажать кнопку "Submit"
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    time.sleep(10)
