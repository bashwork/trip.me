from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from tripme.apps.guides.feeds import LatestGuidesFeed

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'splash.html'}),
    (r'^accounts/', include('registration.backends.simple.urls')),
    # the following uses emails to perform secure registration
    #(r'^accounts/', include('registration.backends.default.urls')),
    (r'^users/', include('profiles.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^guides/', include('tripme.apps.guides.urls')),
    (r'^api/v1/', include('tripme.apps.api.urls')),
    (r'^feeds/', include('tripme.apps.guides.feeds')),
)

#------------------------------------------------------------------------------ 
# use django to serve static files while debugging
#------------------------------------------------------------------------------ 
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT }),
    )
