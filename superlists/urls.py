from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'list.views.home_page', name='home_page'),
    url(r'^list/the-only-list-in-the-world/$','list.views.view_list',name = 'view_list')
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
