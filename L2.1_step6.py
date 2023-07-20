from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_rule = browser.find_element(By.ID, "peopleRule")
    people_checked = people_rule.get_attribute("checked")
    print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == 'true', "People radio is not selected by default"
    
    robot_rule = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robot_checked = robot_rule.get_attribute("checked")
    print("value of robot radio: ", robot_checked)
    
    time.sleep(15)
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submin_disabled = submit_button.get_attribute("disabled")
    print("submit_button is disabled: ", submin_disabled)
    

finally:
    browser.quit()