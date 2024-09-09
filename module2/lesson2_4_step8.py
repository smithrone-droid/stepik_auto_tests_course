import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    book = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book.click()

    browser.execute_script("window.scrollBy(0, 10)", "")
    number = browser.find_element_by_id("input_value")
    x = int(number.text)
    y = calc(x)
    answer_input = browser.find_element_by_id("answer").send_keys(y)
    submit_button = browser.find_element_by_id("solve").click()

finally:
    time.sleep(30)
    browser.quit()




