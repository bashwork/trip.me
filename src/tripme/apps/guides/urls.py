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

# -------------------------------------------------------- #
# guide get urls
# -------------------------------------------------------- #
urlpatterns = patterns('guides.views',
#    (r'^create/$', 'create_guide_view'),
    (r'^/$', list_detail.object_list, guide_list_detail),
    (r'^(?P<object_id>\d+)/$', list_detail.object_detail, guide_list_detail),
)
