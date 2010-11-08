from piston.handler import BaseHandler
from tripme.guides.models import *

class CountryHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Country

class RegionHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Region

class CityHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = City

class SpotHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Spot
