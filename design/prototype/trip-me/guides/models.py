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
    description = models.TextField()
    code = models.CharField(max_length=4)
    capital = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "countries"

    def __unicode__(self):
        return self.name

class Region(models.Model):
    '''
    This represents a sub-region, ex::

      * Missouri, USA
      * England, UK
    '''
    name = models.CharField(max_length=50)
    description = models.TextField()
    code = models.CharField(max_length=4)
    country = models.ForeignKey(Country)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.country.name)

class City(models.Model):
    '''
    This represents a city in a sub-region, ex::

      * Saint Louis, MO, USA
      * London, England, UK
    '''
    name = models.CharField(max_length=50)
    description = models.TextField()
    code = models.CharField(max_length=4)
    region = models.ForeignKey(Region)
    country = models.ForeignKey(Country)
    image = models.ImageField(upload_to="cities/%Y/%m", null=True, blank=True)
    timezone = models.CharField(max_length=6)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "cities"

    def __unicode__(self):
        return "%s, %s, %s" % (self.name, self.region.name, self.country.name)

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
    image = models.ImageField(upload_to="spots/%Y/%m/%d", null=True, blank=True)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return "%s in %s" % (self.name, self.city.name)

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
    user = models.ForeignKey(User, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('pub_date',)

    def __unicode__(self):
        return "%s by %s" % (self.name, self.user.get_full_name())

class GuideLocationEntry(models.Model):
    '''
    This represents a containing location in a
    user guide, ex::

      * London
      * St. Louis
    '''
    city = models.ForeignKey(City)
    spots = models.ForeignKey(Guide)

    class Meta:
        verbose_name_plural = "guide Location entries"

    def __unicode__(self):
        return self.city.name

class GuideSpotEntry(models.Model):
    '''
    This represents a specific spot to visit in a
    given containing location, ex::

      * House of Parliament in London
      * The Arch in St. Louis
    '''
    spot = models.ForeignKey(Spot)
    entry = models.ForeignKey(GuideLocationEntry)

    class Meta:
        verbose_name_plural = "guide spot entries"

    def __unicode__(self):
        return self.spot.name

