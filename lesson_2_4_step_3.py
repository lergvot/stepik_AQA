from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
  #Открыть страницу http://suninjuly.github.io/wait1.html
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/wait1.html")

  #ожидание загрузки
  browser.implicitly_wait(5)
  #time.sleep(1)

  #Нажать на кнопку "Verify"
  button = browser.find_element(By.ID, "verify")
  button.click()

  #Проверить, что появилась надпись "Verification was successful!"
  message = browser.find_element(By.ID, "verify_message")
  assert "successful" in message.text
  print("OK!")
finally:
  time.sleep(10)
  browser.close()

#NoSuchElementException - нет такого элемента
#StaleElementReferenceException - после find_element, элемент пропал
#ElementNotVisibleException - элемент невидимый, по нему не кликнуть