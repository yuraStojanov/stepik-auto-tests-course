from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
print('#############')
price=WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
print(price)
print('#############')
browser.find_element_by_id("book").click()
time.sleep(1)
y = calc(int(browser.find_element_by_id("input_value").text))
print(y)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
# Отправляем заполненную форму
button = browser.find_element_by_id("solve")
button.click()

