from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  #Открыть страницу http://suninjuly.github.io/explicit_wait2.html
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
  # говорим Selenium проверять в течение 7 секунд, пока кнопка не станет кликабельной
  price = WebDriverWait(browser, 7).until(
          EC.text_to_be_present_in_element((By.ID, "price"), "100")) #element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False
  
  #Нажать на кнопку "Book"
  button = browser.find_element(By.ID, "book")
  button.click()
  #Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
  value = browser.find_element(By.ID, "input_value")
  value = value.get_attribute("innerHTML")
  answer = browser.find_element(By.ID, "answer")
  answer.send_keys(calc(value))

  solve = browser.find_element(By.ID, "solve")
  solve.click()

finally:
  time.sleep(30)
  browser.quit()
