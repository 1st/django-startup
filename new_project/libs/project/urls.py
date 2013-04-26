# -*- coding: utf-8 -*-
'''
Urls definition for this project (full site map).

We load url mapping from `apps` section in `config.yaml` file.
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# add user apps that defined in config.yaml
for app_path, url_prefix in settings.APPS_WITH_URLS:
    app_name = app_path.split('.')[-1]
    url_prefix = (url_prefix or '').lstrip('/')
    urlpatterns += patterns(
        '',
        url(r'^{}'.format(url_prefix),
            include('{}.urls'.format(app_path), namespace=app_name, app_name=app_name)),
    )
