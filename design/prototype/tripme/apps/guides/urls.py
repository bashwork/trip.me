from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from guides.models import *

# -------------------------------------------------------- #
# guide get urls
# -------------------------------------------------------- #
urlpatterns = patterns('guides.views',
    (r'^/$', ListView.as_view(model=Guide,
        context_object_name='latest_guide_list',
        template_name='guides/guide_list.html')),

    (r'^(?P<pk>\d+)/$', DetailView.as_view(model=Guide,
        template_name='guides/guide_detail.html')),
)
