from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(f'file://{os.getcwd()}/../web/waits.html')
# first screenshot - open page
driver.save_screenshot('../screenshots/01_open page.png')

try:
    # locate the element with implicit wait
    input_element = driver.find_element(By.ID, 'first')
    input_element.send_keys('Yaakov')
    # second screenshot - input filled
    driver.save_screenshot('../screenshots/02_input_filled.png')
except Exception as e:
    print('input element not found')
finally:
    driver.quit()

print('end of program')
