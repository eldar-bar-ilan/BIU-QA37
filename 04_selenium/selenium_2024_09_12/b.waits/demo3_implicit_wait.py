from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(f'file://{os.getcwd()}/../web/waits.html')

try:
    # locate the element with implicit wait
    input_element = driver.find_element(By.ID, 'first')
    input_element.send_keys('Yaakov')
except Exception as e:
    print('input element not found')
else:
    time.sleep(3)
finally:
    driver.quit()

print('end of program')
