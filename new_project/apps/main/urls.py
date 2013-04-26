# -*- coding: utf-8 -*-
'''
Urls definition for this application.
'''
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.main.views',
    url(r'^$', 'index', name='index'),
)
