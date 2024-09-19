import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestHomePage(unittest.TestCase):
    driver = None
    base_url = 'https://alistapart.com/events/'

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_page_title(self):
        self.driver.get(self.base_url)
        h1_list = self.driver.find_elements(By.TAG_NAME, 'h1')
        # בדיקה שיש כותרת h1 אחת בלבד
        self.assertEqual(1, len(h1_list))
        # בדיקה שהכותרת מכילה את הטקסט המצופה
        self.assertEqual('Events', h1_list[0].text)
