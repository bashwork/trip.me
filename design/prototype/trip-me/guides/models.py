from django.db import models
from django.contrib.auth.models import User

# -------------------------------------------------------- #
# Locations
# -------------------------------------------------------- #

class City(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cities/%Y/%m")
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "cities"

    def __unicode__(self):
        return "%s, %s %s" % (self.name, self.state, self.country)

class Spot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.ForeignKey(City)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)
    image = models.ImageField(upload_to="spots/%Y/%m/%d")
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return "%s in %s" % (self.name, self.city.name)

# -------------------------------------------------------- #
# User Guides
# -------------------------------------------------------- #

class Guide(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, unique=True)

    class Meta:
        ordering = ('pub_date',)

    def __unicode__(self):
        return "%s by %s" % (self.name, self.user.get_full_name())

class GuideCityEntry(models.Model):
    city = models.ForeignKey(City)
    spots = models.ForeignKey(Guide)

    class Meta:
        verbose_name_plural = "guide city entries"

    def __unicode__(self):
        return self.city.name

class GuideSpotEntry(models.Model):
    spot = models.ForeignKey(Spot)
    entry = models.ForeignKey(GuideCityEntry)

    class Meta:
        verbose_name_plural = "guide spot entries"

    def __unicode__(self):
        return self.spot.name

