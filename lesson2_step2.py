from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.ID, "num1")
    x2 = x1.text
    x = int(x2)
    z1 = browser.find_element(By.ID, "num2")
    z2 = z1.text
    z = int(z2)
    y = x + z
    y = str(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)
    buttonSend = browser.find_element(By.CSS_SELECTOR, ".btn btn-default")
    buttonSend.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла