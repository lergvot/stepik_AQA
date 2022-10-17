from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    #Нажать на кнопку
    button1 = browser.find_element(By.CLASS_NAME, "btn")
    button1.click()

    #Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    value = browser.find_element(By.ID, "input_value")
    value = value.get_attribute("innerHTML")
    print(value)

    imput = browser.find_element(By.NAME, "text")
    imput.send_keys(calc(value))
    button2 = browser.find_element(By.CLASS_NAME, "btn")
    button2.click()
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    time.sleep(15)
