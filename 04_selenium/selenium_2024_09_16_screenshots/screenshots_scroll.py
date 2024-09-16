from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()
driver.get(f'file://{os.getcwd()}/web/scroll_selenium.html')
time.sleep(2)
div3 = driver.find_element(By.ID, 'el-3')
driver.execute_script('arguments[0].scrollIntoView()', div3)
time.sleep(2)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(2)
driver.quit()
