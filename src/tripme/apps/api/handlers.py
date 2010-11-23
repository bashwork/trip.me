from django.views.decorators.csrf import csrf_exempt
from piston.handler import BaseHandler
from apps.guides.models import *
from apps.users.models  import UserProfile
from piston.resource import Resource
import urllib, urllib2, simplejson

# -------------------------------------------------------- #
# csrf exempt resource
# -------------------------------------------------------- #
class CsrfExemptResource(Resource):

    def __init__(self, handler, authentication=None):
        super(CsrfExemptResource, self).__init__(handler, authentication)
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)

# -------------------------------------------------------- #
# api handler
# -------------------------------------------------------- #
class CountryHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('code','created', 'modified')
    model = Country

    def read(self, request, id=None, name=None):
        return api_query_helper(request, model=Country, id=id, name=name)

class RegionHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('created', 'modified')
    model = Region
    __max__ = 100

    def read(self, request, id=None, name=None):
        result = api_query_helper(request, model=Region, id=id, name=name)
        return result[:self.__max__]

class CityHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('code','created', 'modified')
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
    allowed_methods = ('GET','DELETE')
    model = Guide
    fields = ('id', 'description', 'name', 'modified',('user',('id','username')))
    __max__ = 20

    def read(self, request, id=None, name=None):
        result = api_query_helper(request, model=Guide, id=id, name=name)
        return result[:self.__max__]

class UserHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = UserProfile
    #fields = ('id', 'description', 'name', 'modified',('user',('id','username')))
    __max__ = 20

    def read(self, request, id=None, name=None):
        result = uapi_query_helper(request, model=UserProfile, id=id, name=name)
        return result[:self.__max__]

import markdown
class MarkupHandler(BaseHandler):
    allowed_methods = ('POST',)

    def create(self, request, type='markdown'):
        print request.raw_post_data
        content = markdown.markdown(request.raw_post_data)
        return {'content' : content, 'length' : len(content) }

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

def uapi_query_helper(request, **kwargs):
    id = kwargs.get('id',None)
    name = kwargs.get('name', None)
    model = kwargs.get('model')

    if id != None: results = model.objects.filter(id=id)
    elif not name: results = model.objects.all()
    else: results = model.objects.filter(user__username__icontains=name)
    return results

#------------------------------------------------------------------------------ 
# proxy methods
#------------------------------------------------------------------------------ 
class FoursquareProxy(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        query = request.path.split('/')[-1]
        params = dict((a,b) for a,b in request.GET.items())
        return _foursquare_request(query, params)

def _foursquare_request(query, params=None):
    query_url = 'http://api.foursquare.com/v1/' + query

    if params:
        params.pop('callback')
        data = urllib.urlencode(params)
        request = urllib2.Request('%s?%s' % (query_url, data) )
    else:
        request = urllib2.Request(query_url)

    try:
        result = simplejson.load(urllib2.urlopen(request))
    except IOError, e:
        result = simplejson.load(e)
    return result
