from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Посчитать сумму заданных чисел
    num1_spam = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = num1_spam.get_attribute("innerHTML")

    num2_spam = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = num2_spam.get_attribute("innerHTML")

    print(num1, num2)
    num = int(num1) + int(num2)
    num = str(num)
    print(num)

    #Выбрать в выпадающем списке значение равное расчитанной сумме
    browser.find_element(By.CSS_SELECTOR, "#dropdown").click()
    
    #Выбираем ответ
    browser.find_element(By.CSS_SELECTOR, "[value='" + num + "']").click()

    #Нажать на кнопку Submit.
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(5)
    browser.quit()