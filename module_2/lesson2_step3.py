from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
#num1=webdriver.Chrome().get('http:/suninjuly.github.io/selects1.html').find_element_by_id("num1").text

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1=browser.find_element_by_id("num1").text
    num2=browser.find_element_by_id("num2").text
    summa = str(int(num1)+int(num2))
    ##рабочая тема с текстом, потом перевести в интежер , нихуя не понятно какой тип данных получаем от .get_attribute("value")
    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector("[value='" + summa + "']").click()   #<-ВОТ ЗДЕСЯ
    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value(summa) # ищем элемент с текстом "Python"
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
