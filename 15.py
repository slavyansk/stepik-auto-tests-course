from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    if button:
        book = browser.find_element_by_id("book")
        book.click()

    num1 = browser.find_element_by_id("input_value")
    x = calc(num1.text)
    
    # Ваш код, который заполняет обязательные поля
    input = browser.find_element_by_id("answer")
    input.send_keys(x)
    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# тест для работы с git