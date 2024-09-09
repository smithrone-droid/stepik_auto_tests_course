from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

#будь, сука, внимателен

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")

    picture = browser.find_element(By.ID, "treasure")
    picture_attribute = picture.get_attribute ("valuex")
    x = picture_attribute
    y = calc(x)

    input_math = browser.find_element(By.ID, 'answer')
    input_math.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()

    radiobutton = browser.find_element(By.ID, 'robotsRule').click()

    submit_button = browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()


finally:
    time.sleep(30)
    browser.quit()




