# coding=utf-8
"""
   首要的目的就是测试home_page ，也就是 /
"""
from django.test import TestCase
from django.core.urlresolvers import resolve 
from django.http import HttpRequest
"""
    这个resolve的作用就是解析url根据解析结果返回views里面的函数
"""
from  list.views import home_page
# 这个home_page 就是/的处理函数


# Create your tests here.
'''
class sometest(TestCase):
    def test_some_method(self):
        self.assertEqual(1+1,3)
'''
class sometest(TestCase):
    def test_resolve_root_url_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
    def test_home_page_return_html(self):
        request=HttpRequest()
        """
        用户在游览器中请求网页时，django看到的就是这么个对象
        """
        response=home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b"<title>To-Do lists</title>",response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

