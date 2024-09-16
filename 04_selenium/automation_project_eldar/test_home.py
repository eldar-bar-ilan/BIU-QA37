import unittest


class TestHomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # initial operation - open browser...
        pass

    @classmethod
    def tearDownClass(cls):
        # final operations - closing browser, closing selenium driver, etc.
        pass

    #    test methods

    def test_page_title(self):
        # use selenium to open the home page and get the title
        # use unittest to test the title
        pass