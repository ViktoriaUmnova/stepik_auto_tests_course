from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    button2 = browser.find_element(By.ID, "book")

    button = WebDriverWait(browser, 1000).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
   
    button2.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)    

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


