from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(5)
driver.get('http://www.google.com')
time.sleep(5)
driver.get('https://www.python.org/')
time.sleep(5)


driver.quit()

