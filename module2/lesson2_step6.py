from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")

    number = browser.find_element(By.ID, "input_value")
    x = int(number.text)
    y = calc(x)

    answer_input = browser.find_element(By.ID,"answer").send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    browser.execute_script("window.scrollBy(0, 150)", "")
    radiobutton = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CLASS_NAME,"btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()


