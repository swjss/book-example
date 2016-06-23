#/usr/bin/env python


from selenium import webdriver
import unittest,time

class NewViewOrTest(unittest.TestCase):
    def setUp(self):
        self.bowser=webdriver.Firefox()
    def tearDown(self):
        self.bowser.quit()
    def test_can_start_a_list_and_retive_after(self):
        self.bowser.get("localhost:8000")
        self.assertIn("To-Do",self.bowser.title)
        self.fail("fail to test")
if __name__ == '__main__':
    unittest.main()

'''
browser=webdriver.Firefox()
browser.get("http://localhost:8000")
assert "To-Do" in browser.title
browser.quit()
'''
