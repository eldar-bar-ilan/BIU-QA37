from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome()
driver.get('https://www.tel-aviv.gov.il/Pages/HomePage.aspx')
time.sleep(2)
in_tel_aviv = driver.find_element(By.NAME, 'ctl00$PlaceHolderMain$ctl01$txtSearchHomepage')
in_tel_aviv.send_keys('ארועים')
in_tel_aviv.send_keys(Keys.ENTER)

# where are we now - url
current_url = driver.current_url
print(current_url)

time.sleep(5)
driver.back()

time.sleep(10)
