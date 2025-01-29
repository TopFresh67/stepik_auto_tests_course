from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.ID, "treasure")
    x2 = x1.get_attribute("valuex")
    x = x2
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    checkBox = browser.find_element(By.ID, "robotCheckbox")
    checkBox.click()
    radioButton = browser.find_element(By.ID, "robotsRule")
    radioButton.click()
    buttonSend = browser.find_element(By.CSS_SELECTOR, ".btn btn-default")
    buttonSend.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла