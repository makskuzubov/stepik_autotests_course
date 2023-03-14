from select import select
import selectors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
        browser.find_element(By.ID, "book").click()

       
        browser.execute_script("window.scrollBy(0, 100);")

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)

        input1 = browser.find_element(By.ID, "answer")
        input1.send_keys(y) 

     # Отправляем заполненную форму
        button3 = browser.find_element(By.ID, "solve")
        button3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


