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
        #她按回车的时候被带进一个新的url
        #这个页面代办事项显示了 1: Buy peacock feathers

        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
        edith_list_url = self.bowser.current_url
        self.check_item_in_rows("1: Buy peacock feathers")
        self.assertRegex(edith_list_url,'/list/.+')
        # 页面显示了一个文本框可以接收新的待办事项
        inputbox=self.bowser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        time.sleep(10)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
        self.check_item_in_rows("1: Buy peacock feathers")
        self.check_item_in_rows("2: Use peacock feathers to make a fly")
        	
        time.sleep(10)
        # 现在一个叫弗朗西斯的人访问首页

        ##我们使用一个新的游览器回话
        ##保证伊迪斯的信息不会从cookie中泄露出来
        self.bowser.quit()
        self.bowser=webdriver.Firefox()
        #弗朗西斯访问首也
        #页面中看不到伊迪斯的清单
        self.bowser.get(self.live_server_url)
        page_text = self.bowser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #弗朗西斯输入了一个新的办事清单
        #他不像伊迪斯那么兴趣盎然
        inputbox = self.bowser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)


        # 弗朗西斯货到了他的唯一url
        francis_list_url = self.bowser.current_url
        self.assertRegex(francis_list_url,'/list/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        #ok 完成
        self.fail("final to test")

#if __name__ == '__main__':
#    unittest.main()

'''
browser=webdriver.Firefox()
browser.get("http://localhost:8000")
assert "To-Do" in browser.title
browser.quit()
'''
