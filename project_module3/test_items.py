import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def is_element_present(browser):
	try:
		browser.implicitly_wait(10)
		browser.find_element_by_css_selector("button.btn-add-to-basket")
		return True
	except:
		return False


def test_link(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#	link = "https://selenium-python.readthedocs.io/waits.html"
	browser.get(link)
	assert is_element_present(browser)==True, "-------->NO BASKET<-----------"
	time.sleep(10)
