from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    input3.send_keys("ip@m.ru")
    
    add_file = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    add_file.send_keys(file_path)
    
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()
    
finally:
    time.sleep(15)
    browser.quit()