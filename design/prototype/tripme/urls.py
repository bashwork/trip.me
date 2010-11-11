from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'splash.html'}),
    (r'^api/v1/', include('tripme.api.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
)

#------------------------------------------------------------------------------ 
# use django to serve static files while debugging
#------------------------------------------------------------------------------ 
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT }),
    )
