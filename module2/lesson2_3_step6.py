from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser =webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")
    troll_submit = browser.find_element_by_class_name("trollface.btn.btn-primary").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    number = browser.find_element_by_id("input_value")
    x = int(number.text)
    y = calc(x)
    answer_input = browser.find_element_by_id("answer").send_keys(y)
    submit_button = browser.find_element_by_class_name("btn.btn-primary").click()


finally:
    time.sleep(30)
    browser.quit()

