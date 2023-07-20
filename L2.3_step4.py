from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calculate(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_button = browser.find_element(By.CLASS_NAME, 'btn')
    first_button.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x = browser.find_element(By.ID, "input_value").text
    calculate_value = browser.find_element(By.ID, "answer")
    calculate_value.send_keys(calculate(int(x)))
    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()
    
finally:
    time.sleep(15)
    browser.quit()
