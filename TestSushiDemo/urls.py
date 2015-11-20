from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings

from TestSushiDemo.views import index
from TestSushiDemo.views import loadMenu
from TestSushiDemo.views import product

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TestSushiDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/$', index),

    url(r'^product2/$', product),

    url(r'^loadMenu/$', loadMenu),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
