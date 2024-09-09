from selenium import webdriver
import time

# open a browser
driver = webdriver.Chrome()

# pause the program for 5 seconds
time.sleep(5)

# close the browser
driver.quit()

