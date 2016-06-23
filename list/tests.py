# coding=utf-8
"""
   首要的目的就是测试home_page ，也就是 /
"""
from django.test import TestCase
from django.core.urlresolvers import resolve 
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
        

