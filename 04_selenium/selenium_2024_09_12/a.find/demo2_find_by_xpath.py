from selenium import webdriver
# the By class has a list of finding ways
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.get(f'file://{os.getcwd()}/../web/find_by_name.html')

# //*[@id="login_form"]/input[2]

pass_element = driver.find_element(By.XPATH, '//*[@id="login_form"]/input[2]')
pass_element.send_keys('secret')

driver.quit()
