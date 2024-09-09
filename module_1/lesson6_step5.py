from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


#модуль 1, раздел 1.6, урок 4

link = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000))) #готовая математическая формула
    link.click()

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
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


