from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def sum_numbers (x, y):
    return str(x + y)

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    sum1 = browser.find_element(By.ID, "num1")
    sum2 = browser.find_element(By.ID, "num2")
    x = int(sum1.text)
    y = int(sum2.text)
    z = sum_numbers (x, y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()


finally:
    time.sleep(30)
    browser.quit()
