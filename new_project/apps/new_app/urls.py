'''
Urls definition for this application.

Replace "new_app" to your application name.
'''
from django.conf.urls import patterns, url


urlpatterns = patterns('apps.new_app.views',
    url(r'^$', 'index', name='index'),
)
