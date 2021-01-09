from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # этот момент можно сократить до
    #y = calc(browser.find_element_by_id("treasure").get_attribute("valuex"))
    x_element = browser.find_element_by_id("treasure")
    x_value = x_element.get_attribute("valuex")
    #print(type(x_value))#запомните твари .get_attribute() возвращает тип str
    y = calc(x_value)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
