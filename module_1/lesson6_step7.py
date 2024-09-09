from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random #иморт модуля рандома
import string #иморт модуля строки

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.TAG_NAME, "input")
    letters = string.printable #создание строки из комбинации printable = digits + ascii_letters + punctuation + whitespace

    for element in elements: #цикл
        random_word = ''.join(random.choice(letters) for _ in range(8)) #генерация случайного набора символов
        element.send_keys(random_word) #отправка в инпуты случайного набора символов

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла