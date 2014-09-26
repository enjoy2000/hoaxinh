# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
	(r'^image/', include('image.urls')),
	(r'^blog/', include('blog.urls')),
	(r'^accounts/', include('registration.backends.default.urls')),
	(r'^$', RedirectView.as_view(url='/image/')),  # Just for ease of use.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
