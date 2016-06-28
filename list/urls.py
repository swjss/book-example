from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'list.views.home_page', name='home_page'),
    #url(r'^the-only-list-in-the-world/$','list.views.view_list',name = 'view_list'),
    url(r'^new$','list.views.new_list',name='new_list'),
    url(r'^(\d+)/$','list.views.view_list',name='view_list'),
    url(r'^(\d+)/add_item','list.views.add_item',name='add_item')
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
