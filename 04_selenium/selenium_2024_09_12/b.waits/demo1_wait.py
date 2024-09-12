from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()
driver.get(f'file://{os.getcwd()}/../web/waits.html')

# this is not a good way to wait - waste of time
time.sleep(4)
input_element = driver.find_element(By.ID, 'first')
input_element.send_keys('Yaakov')
time.sleep(3)

driver.quit()
