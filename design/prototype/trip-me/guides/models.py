from django.db import models

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
        return self.name

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
        return self.name

# ------------------------------------------------------- # 
# To add
# ------------------------------------------------------- # 
# - rank (either +/- score or votes + total stars)
# - guides
# ------------------------------------------------------- # 
