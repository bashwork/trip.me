from django.conf.urls.defaults import *

# -------------------------------------------------------- #
# thanks and a beer to:
# http://peyman-django.blogspot.com/2010/03/full-easy-authentication-using.html 
# django-registration
# -------------------------------------------------------- #

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login',
        {'template_name':'accounts/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name':'accounts/logout.html'}),

    (r'^password/change/$', 'django.contrib.auth.views.password_change',
        {'template_name':'accounts/password_change.html'}),
    (r'^password/change/done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name':'accounts/password_change_done.html'}),

    (r'^password/reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name':'accounts/password_reset.html'}),
    (r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name':'accounts/password_reset_done.html'}),

    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'accounts/password_reset_confirm.html'}),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'accounts/password_reset_complete.html'}),

    (r'^signup/$', 'tripme.accounts.views.signup',
        {'template_name':'accounts/signup.html'}),
    (r'^signup/done/$', 'tripme.accounts.views.signup_done',
        {'template_name':'accounts/signup_done.html'}),

    (r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'mysite.accounts.views.signup_confirm'),
    (r'^signup/complete/$', 'mysite.accounts.views.signup_complete',
        {'template_name': 'accounts/signup_complete.html'}),
)
