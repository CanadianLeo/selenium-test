
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("1")

    name = browser.find_element(By.NAME, "lastname")
    name.send_keys("1")

    name = browser.find_element(By.NAME, "email")
    name.send_keys("1")

    file_field = browser.find_element(By.NAME, "file")
    file_field.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()