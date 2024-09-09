from selenium import webdriver


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/cats.html")

    button = browser.find_element_by_id("button")

finally:
    browser.quit()

