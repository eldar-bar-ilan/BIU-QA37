from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(2)
in_google = driver.find_element(By.NAME, 'q')
in_google.send_keys('python')
in_google.send_keys(Keys.ENTER)

time.sleep(10)
