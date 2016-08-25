# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list
from myproject.myapp.views import viewTag



urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^list/(?P<username>[\w\-]+)/(?P<requestedTag>[\w\-]+)/$', viewTag, name='view')
]