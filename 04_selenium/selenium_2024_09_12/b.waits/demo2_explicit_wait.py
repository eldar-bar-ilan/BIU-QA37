from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
# import class WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
# import expected_conditions module
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
driver.get(f'file://{os.getcwd()}/../web/waits.html')

# create the wait object
wait = WebDriverWait(driver, 5)
# locate the element with explicit wait
input_element = wait.until(ec.presence_of_element_located((By.ID, 'first')))
input_element.send_keys('Yaakov')
time.sleep(3)
driver.quit()
