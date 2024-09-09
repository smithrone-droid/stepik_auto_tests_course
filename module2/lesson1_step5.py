from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_math = browser.find_element(By.ID,'answer' )
    input_math.send_keys(y)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    radio2 = browser.find_element(By.ID, "robotsRule")
    radio2.click()

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

