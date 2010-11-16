from django.conf.urls.defaults import *
from django.views.generic import list_detail
from guides.models import *
from guides.views import *

# -------------------------------------------------------- #
# list details
# -------------------------------------------------------- #
guide_list_detail = {
    'queryset'      : Guide.objects.all(),
    'allow_empty'   : True,
    'paginate_by'   : 9,
    #'template_name' : 'guides/guide_list.html'
}
guide_detail = {
    'queryset'      : Guide.objects.all(),
}

# -------------------------------------------------------- #
# guide get urls
# -------------------------------------------------------- #
urlpatterns = patterns('guides.views',
    url(r'^$', list_detail.object_list,
        guide_list_detail, name='guide_list'),
    url(r'^create/$', 'create_guide'),
    url(r'^(?P<id>\d+)/$', 'guide_detail'),
    url(r'^(?P<id>\d+)/spots/$', 'guide_detail_spots'),
)
