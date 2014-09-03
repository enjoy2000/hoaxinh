# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('hoaxinh.image.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^add/$', 'add', name='add'),
    url(r'^delete/$', 'delete', name='delete'),
    url(r'^clear/$', 'clear', name='clear'),
    url(r'^ajaxload/$', 'ajaxload', name='ajaxload'),
    url(r'^$', 'index', name='index'),
)
