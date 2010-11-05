from piston.handler import BaseHandler
from guides.models import City,Spot

class CityHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = City

    #def read(self, request, name=None):
    #    pass

class SpotHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Spot

    #def read(self, request, spot=None):
    #    pass

class CitySpotHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Spot

    #def read(self, request, name, spot=None):
    #    pass
