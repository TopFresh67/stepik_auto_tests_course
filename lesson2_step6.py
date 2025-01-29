from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    buttonSend = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    buttonSend.click()

    Redirect_page = browser.window_handles[1]
    browser.switch_to.window(Redirect_page)

    x1 = browser.find_element(By.ID, "input_value")
    x = x1.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    buttonSend1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    buttonSend1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла