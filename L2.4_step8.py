from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calculate(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    x = browser.find_element(By.ID, "input_value").text
    y = calculate(int(x))
    calculate_value = browser.find_element(By.ID, "answer")
    calculate_value.send_keys(y)
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    
    
finally:
    time.sleep(10)
    browser.quit()