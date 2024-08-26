import unittest
from selenium import webdriver


class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_google_title(self):
        self.driver.get("https://www.google.com")
        title = self.driver.title
        self.assertEqual('Google', title, 'the page title is wrong')
