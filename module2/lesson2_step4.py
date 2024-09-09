from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    first_button = browser.find_element_by_class_name("btn.btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()
    number = browser.find_element_by_id("input_value")
    x = int(number.text)
    y = calc(x)
    answer_input = browser.find_element_by_id("answer").send_keys(y)
    submit_button = browser.find_element_by_class_name("btn.btn-primary").click()



finally:
    time.sleep(30)
    browser.quit()




