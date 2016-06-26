# coding=utf-8
"""
   首要的目的就是测试home_page ，也就是 /
"""
from django.test import TestCase
from django.core.urlresolvers import resolve 
from django.http import HttpRequest
from django.template.loader import render_to_string
"""
    这个resolve的作用就是解析url根据解析结果返回views里面的函数
"""
from  list.views import home_page
# 这个home_page 就是/的处理函数


# Create your tests here.
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
        u_html=render_to_string('home.html')
        self.assertEqual(response.content.decode(),u_html)
    def test_home_page_can_save_a_POST_request(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'

        response=home_page(request)

        self.assertIn('A new list item',response.content.decode())

#        text_html=render_to_string('home.html',{'new_item_text':request.POST['item_text']})
#        self.assertIn('A new list item',text_html)
