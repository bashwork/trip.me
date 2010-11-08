from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import *

# -------------------------------------------------------- #
# Resources
# -------------------------------------------------------- #
country_handler_resource = Resource(CountryHandler)
region_handler_resource = Resource(RegionHandler)
city_handler_resource = Resource(CityHandler)
spot_handler_resource = Resource(SpotHandler)

# -------------------------------------------------------- #
# Url Patterns
# -------------------------------------------------------- #
urlpatterns = patterns('',
    url(r'^country/*$', country_handler_resource),
    url(r'^country/(?P<name>[^/]+)/', country_handler_resource),

    url(r'^region/*$', region_handler_resource),
    url(r'^region/(?P<name>[^/]+)/', region_handler_resource),

    url(r'^city/*$', city_handler_resource),
    url(r'^city/(?P<name>[^/]+)/', city_handler_resource),

    url(r'^spot/*$', spot_handler_resource),
    url(r'^spot/(?P<name>[^/]+)/', spot_handler_resource),
)
