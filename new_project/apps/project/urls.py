# -*- coding: utf-8 -*-
'''
Urls definition for this project (full site map).

When you crate new application, you need to do:
 - create copy of last "url(...)" statement
 - replace "new_app" to real name of your application.
 - uncomment this line (delete initial "#" symbol)

To reverse url use syntax:
 - in python code "from django.core.urlresolvers import reverse"
   and "url = reverse('action_name', current_app='new_app')"
 - in templates "{% url new_app:action_name %}"
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'apps.project.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# add user apps that defined in config.yaml
for app_path, url_prefix in settings.APPS_WITH_URLS:
    app_name = app_path.split('.')[-1]
    urlpatterns += patterns(
        '',
        url(r'^{}'.format(url_prefix or ''),
            include('{}.urls'.format(app_path)),
            name=app_name),
    )
