from django.conf.urls.defaults import *
import guides.signals

# -------------------------------------------------------- #
# user management urls
# -------------------------------------------------------- #
urlpatterns = patterns('guides.views',
#    (r'^account/login/$', 'django.contrib.auth.view.login', {'template_name':'guides/login.html'}),
#    (r'^account/logout/$', 'django.contrib.auth.view.logout', {'template_name':'guides/logout.html'}),
)
