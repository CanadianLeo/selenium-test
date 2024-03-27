import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.ID, "input_value").text

    value = calc(x_value)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(value)

    checkbox_field = browser.find_element(By.ID, "robotCheckbox")
    checkbox_field.click()

    radio_field = browser.find_element(By.ID, "robotsRule")
    radio_field.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()