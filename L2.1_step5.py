from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"

def calculate(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calculate(int(x))
    calculate_value = browser.find_element(By.ID, "answer")
    calculate_value.send_keys(y)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    robot_rule = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robot_rule.click()
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
    
    