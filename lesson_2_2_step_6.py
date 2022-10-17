from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    #Открыть страницу http://SunInJuly.github.io/execute_script.html.
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    #Считать значение для переменной x.
    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value")
    num = input_value.get_attribute("innerHTML")

    #Посчитать математическую функцию от x.
    num = calc(int(num))

    #Проскроллить страницу вниз.
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    #Ввести ответ в текстовое поле.
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(num)

    #Выбрать checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "[type=\"checkbox\"]")
    option1.click()

    #Переключить radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "[value=\"robots\"]")
    option2.click()

    #Нажать на кнопку "Submit".
    option3 = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    option3.click()
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
