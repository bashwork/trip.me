from piston.handler import BaseHandler
from tripme.guides.models import *

class CountryHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('code','pub_date', 'last_modified')
    model = Country

    def read(self, request, id=None, name=None):
        '''
        '''
        if id != None: countries = Country.objects.get(id=id)
        elif not name: countries = Country.objects.all()
        else: countries = Country.objects.filter(name__icontains=name)
        return countries

class RegionHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('pub_date', 'last_modified')
    model = Region
    __max__ = 100

    def read(self, request, id=None, name=None):
        '''
        '''
        if id != None: regions = Region.objects.get(id=id)
        elif not name: regions = Region.objects.all()[:self.__max__]
        else: regions = Region.objects.filter(name__icontains=name)[:self.__max__]
        return regions

class CityHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('code','pub_date', 'last_modified')
    #fields = ('id', 'description', 'name', 'image','latitude','longitude','country_id','region_id')
    model = City
    __max__ = 20

    def read(self, request, id=None, name=None):
        '''
        '''
        if id != None: cities = City.objects.get(id=id)
        elif not name: cities = City.objects.all()[:self.__max__]
        else: cities = City.objects.filter(name__icontains=name)[:self.__max__]
        return cities

class SpotHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Spot
    __max__ = 20

    def read(self, request, id=None, name=None):
        '''
        '''
        if id != None: spots = Spot.objects.get(id=id)
        elif not name: spots = Spot.objects.all()[:self.__max__]
        else: spots = Spot.objects.filter(name__icontains=name)[:self.__max__]
        return spots

class GuideHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Guide
    fields = ('id', 'description', 'name', 'last_modified',('user',('id','username')))
    __max__ = 20

    def read(self, request, id=None, name=None):
        '''
        '''
        if id != None: guides = Guide.objects.get(id=id)
        elif not name: guides = Guide.objects.all()[:self.__max__]
        else: guides = Guide.objects.filter(name__icontains=name)[:self.__max__]
        return guides
