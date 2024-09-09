from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

#заполнение обязательный полей и проверка наличия определенного набора полей

    labels = browser.find_elements(By.TAG_NAME, 'label')
    first_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    last_name.send_keys("Petrov")
    email = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    email.send_keys("test@test.ru")
    phone = browser.find_element(By.XPATH, "//html/body/div/form/div[2]/div[2]/input")
    address = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    time.sleep(10)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = browser.find_element_by_tag_name("h1").text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
