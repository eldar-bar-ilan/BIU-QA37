from selenium import webdriver
# the By class has a list of finding ways
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.get(f'file://{os.getcwd()}/../web/find_by_css.html')

# find the paragraph usint CSS selector
piska = driver.find_element(By.CSS_SELECTOR, 'p.content')
# print the inner html of the paragraph
text = piska.get_attribute('innerHTML')
print(text)

time.sleep(2)
driver.quit()
