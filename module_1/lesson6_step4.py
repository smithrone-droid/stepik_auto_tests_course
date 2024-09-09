from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#модуль 1, раздел 1.6, урок 4

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.TAG_NAME, "input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")
    city = browser.find_element(By.CLASS_NAME, "form-control.city")
    city.send_keys("Smolensk")
    country = browser.find_element(By.ID, "country")
    country.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла