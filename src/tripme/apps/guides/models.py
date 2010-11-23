from django.db import models
from django.contrib.auth.models import User

# -------------------------------------------------------- #
# World Locations
# -------------------------------------------------------- #
# These represent the top level location hierarchy that
# users can add to their guides. Right now the data is
# read only, however, in the future users will be able to
# modify the data and add new spots (wiki/versioning)
#
# * description - This will be ReST documentation based on
#   the tabs of the description widget.
#
# * lat/long - Should we have this for country and region
#   so we don't have to use the gmaps api every time?
# -------------------------------------------------------- #
class Country(models.Model):
    '''
    This represents a top level country in the world, ex:

      * United States
      * United Kingdom
    '''
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=4)
    capital = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "countries"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/data/country/%s" % self.id

class Region(models.Model):
    '''
    This represents a sub-region, ex::

      * Missouri, USA
      * England, UK
    '''
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=4)
    country = models.ForeignKey(Country)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.country.name)

    def get_absolute_url(self):
        return "/data/region/%s" % self.id

class City(models.Model):
    '''
    This represents a city in a sub-region, ex::

      * Saint Louis, MO, USA
      * London, England, UK
    '''
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=4)
    region = models.ForeignKey(Region)
    image = models.ImageField(upload_to="img/cities/%Y/%m", null=True, blank=True)
    timezone = models.CharField(max_length=6)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "cities"

    def __unicode__(self):
        return "%s, %s, %s" % (self.name, self.region.name, self.region.country.name)

    def get_absolute_url(self):
        return "/data/city/%s" % self.id

class Spot(models.Model):
    '''
    This represents a location in a given city, ex::

      * Bush Stadium in Saint Louis, MO USA
      * Houses of Parliament, London, England, UK
    '''
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.ForeignKey(City)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)
    image = models.ImageField(upload_to="img/spots/%Y/%m/%d", null=True, blank=True)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return "%s in %s" % (self.name, self.city.name)

    def get_absolute_url(self):
        return "/data/spot/%s" % self.id

    @classmethod
    def get_all_near(lat, long):
        return Spots.objects.raw('''SELECT *,
           SQRT(POW((69.1 * (locations.latitude - 27.950898)) , 2 ) +
                       POW((53 * (locations.longitude - -82.461517)), 2)) AS distance
           FROM locations
           ORDER BY distance ASC
           LIMIT 5''')

# -------------------------------------------------------- #
# User Guides
# -------------------------------------------------------- #
# These will be a collection of the places to visit in
# given cities of the world.
#
# Should a user be able to have an entry at region and
# country level?
# -------------------------------------------------------- #
class Guide(models.Model):
    '''
    This represents user guide, ex::

      * My UK Trip
    '''
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='guides')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('modified',)

    def __unicode__(self):
        return "%s by %s" % (self.name, self.user.get_full_name())

    @models.permalink
    def get_absolute_url(self):
        return ('guides.views.guide_detail', [str(self.id)])

    def get_random_image(self):
        '''
        This will randomly return an image for one
        of the cities that is currently included in this guide

        :returns: A random ImageField or None
        '''
        set = self.entries.exclude(city__image='')
        set = set.order_by('?')
        return None if not any(set) else set[0].city.image.url

class GuideLocationEntry(models.Model):
    '''
    This represents a containing location in a
    user guide, ex::

      * London
      * St. Louis
    '''
    city = models.ForeignKey(City)
    guide = models.ForeignKey(Guide, related_name='entries')

    class Meta:
        verbose_name_plural = "guide Location entries"

    def __unicode__(self):
        return self.city.name

    @models.permalink
    def get_absolute_url(self):
        return ('guides.views.guide_detail_spots', [str(self.guide.id), str(self.id)])

class GuideSpotEntry(models.Model):
    '''
    This represents a specific spot to visit in a
    given containing location, ex::

      * House of Parliament in London
      * The Arch in St. Louis
    '''
    spot = models.ForeignKey(Spot)
    entry = models.ForeignKey(GuideLocationEntry, related_name='spots')

    class Meta:
        verbose_name_plural = "guide spot entries"

    def __unicode__(self):
        return self.spot.name

