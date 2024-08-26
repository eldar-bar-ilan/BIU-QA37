from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com')
title = driver.title
print(title)

input('press enter to quit: ')
driver.quit()