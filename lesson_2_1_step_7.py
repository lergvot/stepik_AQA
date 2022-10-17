from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    image = browser.find_element(By.CSS_SELECTOR, "[id=\"treasure\"]")

    #Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    image_value = image.get_attribute("valuex")

    #Посчитать математическую функцию от x (сама функция остаётся неизменной).
    y = calc(image_value)

    #Ввести ответ в текстовое поле.
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    #Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "[type=\"checkbox\"]")
    option1.click()

    #Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "[value=\"robots\"]")
    option2.click()

    #Нажать на кнопку Submit.
    option3 = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    option3.click()

finally:
    time.sleep(10)
    browser.quit()