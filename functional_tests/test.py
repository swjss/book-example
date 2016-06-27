#/usr/bin/env python


from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import unittest,time

class NewViewOrTest(LiveServerTestCase):
    def check_item_in_rows(self,item):
        table = self.bowser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text==item for row in rows),"new to-do item did not appear in table\n%s" % table.text)
    def setUp(self):
        self.bowser=webdriver.Firefox()
    def tearDown(self):
        self.bowser.quit()
    def test_can_start_a_list_and_retive_after(self):
        self.bowser.get(self.live_server_url)
        self.assertIn("To-Do",self.bowser.title)
        header_text=self.bowser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        inputbox=self.bowser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
        self.check_item_in_rows("1: Buy peacock feathers")
        inputbox=self.bowser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        self.check_item_in_rows("1: Buy peacock feathers")
        self.check_item_in_rows("2: Use peacock feathers to make a fly")
	
        self.fail("final to test")

#if __name__ == '__main__':
#    unittest.main()

'''
browser=webdriver.Firefox()
browser.get("http://localhost:8000")
assert "To-Do" in browser.title
browser.quit()
'''
