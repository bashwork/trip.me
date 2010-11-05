from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import *

# -------------------------------------------------------- #
# Resources
# -------------------------------------------------------- #
city_handler_resource = Resource(CityHandler)
spot_handler_resource = Resource(SpotHandler)

# -------------------------------------------------------- #
# Url Patterns
# -------------------------------------------------------- #
urlpatterns = patterns('',
    url(r'^city/*$', city_handler_resource),
    url(r'^city/(?P<name>[^/]+)/', city_handler_resource),
    url(r'^spot/*$', spot_handler_resource),
    url(r'^spot/(?P<name>[^/]+)/', spot_handler_resource),
)
