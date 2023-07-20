from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = int(browser.find_element(By.ID, "num1").text)
    number2 = int(browser.find_element(By.ID, "num2").text)
    sum = number1 + number2
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()
    
        
finally:
    time.sleep(10)
    browser.quit()
