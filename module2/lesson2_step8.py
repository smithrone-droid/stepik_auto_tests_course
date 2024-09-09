from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")

    first_name = browser.find_element_by_name("firstname").send_keys("test1")
    last_name = browser.find_element_by_name("lastname").send_keys("test2")
    email = browser.find_element_by_name("email").send_keys("teset@test.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    choose_file = browser.find_element_by_css_selector("[type='file']").send_keys(file_path)
    button_submit = browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    time.sleep(20)
    browser.quit()




# directory = "/home/user/stepik/Chapter2/"
#
# # имя файла, который будем загружать на сайт
# file_name = "file_example.txt"
#
# # собираем путь к файлу
# file_path = os.path.join(directory, file_name)
# # отправляем файл
# element.send_keys(file_path)
# 3.путь автоматизатора.
# если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# # импортируем модуль
# import os
# # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
# current_dir = os.path.abspath(os.path.dirname(__file__))
#
# # имя файла, который будем загружать на сайт
# file_name = "file_example.txt"
#
# # получаем путь к file_example.txt
# file_path = os.path.join(current_dir, file_name)
# # отправляем файл
# element.send_keys(file_path)

