from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import *

# -------------------------------------------------------- #
# authentication
# -------------------------------------------------------- #
auth = HttpBasicAuthentication(realm="trip.me realm")
ad   = { 'authentication' : auth }

urlpatterns = []
# -------------------------------------------------------- #
# country api references
# -------------------------------------------------------- #
country_handler_resource = Resource(CountryHandler)
urlpatterns += patterns('',
    url(r'^country/$', country_handler_resource),
    url(r'^country/search/(?P<name>[^/]+)/', country_handler_resource),
    url(r'^country/show/(?P<id>[^/]+)/', country_handler_resource),
)

# -------------------------------------------------------- #
# region api reference
# -------------------------------------------------------- #
region_handler_resource = Resource(RegionHandler)
urlpatterns += patterns('',
    url(r'^region/$', region_handler_resource),
    url(r'^region/search/(?P<name>[^/]+)/', region_handler_resource),
    url(r'^region/show/(?P<id>[^/]+)/', region_handler_resource),
)

# -------------------------------------------------------- #
# city api references
# -------------------------------------------------------- #
city_handler_resource = Resource(CityHandler)
urlpatterns += patterns('',
    url(r'^city/$', city_handler_resource),
    url(r'^city/search/(?P<name>[^/]+)/', city_handler_resource),
    url(r'^city/show/(?P<id>[^/]+)/', city_handler_resource),
)

# -------------------------------------------------------- #
# spot api references
# -------------------------------------------------------- #
spot_handler_resource = CsrfExemptResource(SpotHandler)
urlpatterns += patterns('',
    url(r'^spot/$', spot_handler_resource),
    url(r'^spot/search/(?P<name>[^/]+)/', spot_handler_resource),
    url(r'^spot/show/(?P<id>[^/]+)/', spot_handler_resource),
)

# -------------------------------------------------------- #
# guide api references
# -------------------------------------------------------- #
guide_handler_resource = CsrfExemptResource(GuideHandler)
urlpatterns += patterns('',
    url(r'^guide/$', guide_handler_resource),
    url(r'^guide/search/(?P<name>[^/]+)/', guide_handler_resource),
    url(r'^guide/show/(?P<id>[^/]+)/', guide_handler_resource),
)

# -------------------------------------------------------- #
# user api references
# -------------------------------------------------------- #
user_handler_resource = CsrfExemptResource(UserHandler)
urlpatterns += patterns('',
    url(r'^user/$', user_handler_resource),
    url(r'^user/search/(?P<name>[^/]+)/', user_handler_resource),
    url(r'^user/show/(?P<id>[^/]+)/', user_handler_resource),
)

# -------------------------------------------------------- #
# markup api references
# -------------------------------------------------------- #
markup_handler_resource = CsrfExemptResource(MarkupHandler)
urlpatterns += patterns('',
    url(r'^markup/$', markup_handler_resource),
    url(r'^markup/(?P<type>[^/]+)/', markup_handler_resource),
)

# -------------------------------------------------------- #
# proxy api references
# -------------------------------------------------------- #
foursquare_proxy_resource = Resource(FoursquareProxy)
urlpatterns += patterns('',
    url(r'^proxy/foursquare/', foursquare_proxy_resource),
)
