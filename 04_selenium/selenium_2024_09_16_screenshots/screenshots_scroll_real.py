from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.save_screenshot('images/01_open_browser.png')

driver.get(f'file://{os.getcwd()}/web/scroll_selenium.html')
driver.save_screenshot('images/02_navigate_to_page.png')

div3 = driver.find_element(By.ID, 'el-3')
driver.execute_script('arguments[0].scrollIntoView()', div3)
driver.save_screenshot('images/03_scroll_to_div3.png')

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
driver.save_screenshot('images/04_page_bottom.png')

driver.quit()
