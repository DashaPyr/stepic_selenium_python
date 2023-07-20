from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://SunInJuly.github.io/execute_script.html'

def calculate(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = calculate(int(x))
    calculate_value = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", calculate_value)
    calculate_value.send_keys(y)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()
    robot_rule = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
    robot_rule.click()
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()