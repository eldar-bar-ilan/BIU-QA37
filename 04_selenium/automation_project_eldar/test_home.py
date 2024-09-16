import unittest
from selenium import webdriver
# options let you add arguments on how to start the browser
from selenium.webdriver.chrome.options import Options
import os
import time


class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # initial operation - open browser...
        # for maximized browser - create an Option object and add argument for maximized
        options = Options()
        options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=options)
        # set the base url for all files if you want to write less code in the test methods
        cls.base_url = f'file://{os.getcwd()}/web/'

    @classmethod
    def tearDownClass(cls):
        # final operations - closing browser, closing selenium driver, etc.
        time.sleep(3)
        cls.driver.quit()

    #    test methods

    def test_page_title(self):
        # use selenium to open the home page and get the title
        self.driver.get(f"{self.base_url}home.html")
        # use unittest to test the title
        expected = "Automation Project"
        actual = self.driver.title
        self.assertEqual(expected, actual)

