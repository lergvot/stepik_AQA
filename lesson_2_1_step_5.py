from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    #Посчитать математическую функцию от x (код для этого приведён ниже).
    y = calc(x)

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