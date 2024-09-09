from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    radiobutton = browser.find_element_by_id("peopleRule")
    radiobutton_attribute = radiobutton.get_attribute("checked")
    assert radiobutton is not None, "People radio is not selected by default"

finally:
    # успеваем скопировать код за 30 секунд
    # закрываем браузер после всех манипуляций
    browser.quit()


