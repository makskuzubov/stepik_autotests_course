from select import select
import selectors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # name_element = "Maks"
    # name = name_element.text 
    # lastname_element = "Kuzubov"
    # lastname = lastname_element.text 
    # email_element = "max.kuzubvoua@gmail.com"
    # email = email_element.text

    # Ваш код, который заполняет обязательные поля 
   
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Maks")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Kuzubov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("max.kuzubvoua@gmail.com")

    element = browser.find_element(By.ID, "file")

    import os
    current_dir = os.path.abspath(os.path.dirname('__2.2_step7.py__'))
    file_path = os.path.join(current_dir, 'file.txt') 
    element.send_keys(file_path)
 
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


