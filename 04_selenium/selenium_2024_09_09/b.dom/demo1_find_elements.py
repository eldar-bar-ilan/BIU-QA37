from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# the [..] notation means - go up one directory
web_dir = os.getcwd() + '/../web'

url = f'{web_dir}/find-element.html'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

# find the input element for first name - BY.ID
web_element = driver.find_element(By.ID,'first-id')
web_element.send_keys("Eldar")
time.sleep(3)

# find the input element for first name - BY.ID
web_element = driver.find_element(By.NAME, 'last')
web_element.send_keys('Bakshi')

time.sleep(5)
driver.quit()

