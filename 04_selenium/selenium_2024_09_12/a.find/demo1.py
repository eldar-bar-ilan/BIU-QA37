from selenium import webdriver
# the By class has a list of finding ways
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.get(f'file://{os.getcwd()}/../web/find_by_name.html')
input_elements = driver.find_elements(By.TAG_NAME, 'input')
time.sleep(1)
input_elements[0].send_keys('Eldar')
time.sleep(1)
input_elements[1].send_keys('123')
time.sleep(3)
# input_elements[2].click()
input_elements[3].click()
time.sleep(3)
driver.quit()
