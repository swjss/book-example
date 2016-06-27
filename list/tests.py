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
from  .models import Item
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
    def test_home_page_can_save_a_POST_request(self):
        request=HttpRequest()
        request.method="POST"
        request.POST['item_text']='A new list item'

        response=home_page(request)
        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

 #       self.assertIn('A new list item',response.content.decode())

        
#        text_html=render_to_string('home.html',{'new_item_text':request.POST['item_text']})
#        self.assertIn('A new list item',text_html)


class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item.text,'Item the second')
class HomepageTest(TestCase):
    def test_home_page_only_saves_items_when_necessary(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'
        response=home_page(request)

        self.assertEqual(Item.objects.count(),1)
    def test_home_page_redirects_after_POST(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'
        response=home_page(request)
        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/list/the-only-list-in-the-world')



class ListViewTest(TestCase):
    
    def test_uses_list_template(self):
        response = self.client.get('/list/the-only-list-in-the-world/')
        self.assertTemplateUsed(response,'list.html')

    def test_display_all_item(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        
        response = self.client.get('/list/the-only-list-in-the-world/')

        self.assertContains(response,'itemey 1')
        self.assertContains(response,'itemey 2')


