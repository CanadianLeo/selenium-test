from typing_extensions import Self
from unittest import TestCase
from unittest import main as unittest_main
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

RESULT = "Congratulations! You have successfully registered!"

class Test(TestCase):
    def test1(self: Self) -> None:
        result = test("http://suninjuly.github.io/registration1.html")
        self.assertEqual(result, RESULT)


    def test2(self: Self) -> None:
        result = test("http://suninjuly.github.io/registration2.html")
        self.assertEqual(result, RESULT)
        


def test(link: str) -> str:
    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_element = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input_element.send_keys("123")

        input_element = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input_element.send_keys("123")

        input_element = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input_element.send_keys("123")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        return welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest_main()
