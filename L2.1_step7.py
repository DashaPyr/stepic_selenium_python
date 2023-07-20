from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calculate(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    treasure = browser.find_element(By.ID, "treasure")
    treasure_value = treasure.get_attribute("valuex")
    x = int(treasure_value)
    y = calculate(x)
 #   print("submit_button is disabled: ", treasure_value)
 #   print("calculate value: ", y)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    robot_rule = browser.find_element(By.ID, "robotsRule")
    robot_rule.click()
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()
    
    
finally:
    time.sleep(15)
    browser.quit()
