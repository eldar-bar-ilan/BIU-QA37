from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get(f'file://{os.getcwd()}/../web/select.html')
time.sleep(3)
select_element = driver.find_element(By.ID, 'color')
select = Select(select_element)

# list of option objects of the select
options = select.options
# iterate all options and print their text
for opt in options:
    print(opt.text)

# select an option - by index
select.select_by_index(2)
time.sleep(3)

driver.quit()
