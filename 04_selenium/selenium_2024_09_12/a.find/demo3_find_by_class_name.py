from selenium import webdriver
# the By class has a list of finding ways
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.get(f'file://{os.getcwd()}/../web/find_by_name.html')

# get all inputs with user info - belong to a class
user_info_inputs = driver.find_elements(By.CLASS_NAME, 'user-info')
user_info_inputs[0].send_keys('Moshe')
user_info_inputs[1].send_keys('123')
time.sleep(2)
driver.quit()
