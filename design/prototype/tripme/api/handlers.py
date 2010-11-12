from piston.handler import BaseHandler
from tripme.guides.models import *

class CountryHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('code','pub_date', 'last_modified')
    model = Country

    def read(self, request, id=None, name=None):
        return api_query_helper(request, model=Country, id=id, name=name)

class RegionHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('pub_date', 'last_modified')
    model = Region
    __max__ = 100

    def read(self, request, id=None, name=None):
        result = api_query_helper(request, model=Region, id=id, name=name)
        return result[:self.__max__]

class CityHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('code','pub_date', 'last_modified')
    #fields = ('id', 'description', 'name', 'image','latitude','longitude','country_id','region_id')
    model = City
    __max__ = 20

    def read(self, request, id=None, name=None):
        result = api_query_helper(request, model=City, id=id, name=name)
        return result[:self.__max__]

class SpotHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Spot
    __max__ = 20

    def read(self, request, id=None, name=None):
        result = api_query_helper(request, model=Spot, id=id, name=name)
        return result[:self.__max__]

class GuideHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Guide
    fields = ('id', 'description', 'name', 'last_modified',('user',('id','username')))
    __max__ = 20

    def read(self, request, id=None, name=None):
        result = api_query_helper(request, model=Guide, id=id, name=name)
        return result[:self.__max__]

class UserHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Guide
    #fields = ('id', 'description', 'name', 'last_modified',('user',('id','username')))
    __max__ = 20

    def read(self, request, id=None, name=None):
        result = api_query_helper(request, model=UserProfile, id=id, name=name)
        return result[:self.__max__]

#------------------------------------------------------------------------------ 
# helper methods
#------------------------------------------------------------------------------ 
def api_query_helper(request, **kwargs):
    id = kwargs.get('id',None)
    name = kwargs.get('name', None)
    model = kwargs.get('model')

    if id != None: results = model.objects.filter(id=id)
    elif not name: results = model.objects.all()
    else: results = model.objects.filter(name__icontains=name)
    return results
